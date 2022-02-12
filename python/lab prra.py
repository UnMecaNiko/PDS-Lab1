from tkinter import Tk, Frame, Button, Label, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.lines import Line2D
import serial
import collections
from threading import Thread

# ---------------Variables-----------------------------------------------
global LED1
global LED2
global LED3
LED1 = 0
LED2 = 0
LED3 = 0

global B1
global B2
global B3
B1 = 0
B2 = 0
B3 = 0

global i
i=0

samples = 60  # numero de muestras

graphs = []
data = []

# ---------------Puerto serial--------------------------------------------

try:
    serialConnection = serial.Serial('COM4', 9600)
except:
    print('No se pudo conectar al puerto')

for i in range(3):   # El rango es el numero de sensores
    data.append(collections.deque([0] * samples, maxlen=samples))
    graphs.append(Line2D([], [], color='blue'))

# -----------Funciones----------------------------------------------------

def getSerialData():  ###DIFERENTE
    global i
    while True:
        for f in range(3):
            for c in range(59):
                data[f][c] = float(data[f][c+1])

        value = serialConnection.readline().decode('utf-8')

        data[i][59] = value
        #print(data[i])
        i = i + 1
        if i == 3:
            i = 0

def button1():
    global B1
    global B2
    global B3
    B1 = 1
    B2 = 0
    B3 = 0

def button2():
    global B1
    global B2
    global B3
    B1 = 0
    B2 = 1
    B3 = 0

def button3():
    global B1
    global B2
    global B3
    B1 = 0
    B2 = 0
    B3 = 1

def button4():
    global B1
    global B2
    global B3
    B1 = 1
    B2 = 1
    B3 = 1

def graphData1(*args):
    global B1
    if B1 == 1:
        graphs[0].set_data(range(samples), data[0])

def graphData2(*args):
    global B2
    if B2 == 1:
        graphs[1].set_data(range(samples), data[1])

def graphData3(*args):
    global B3
    if B3 == 1:
        graphs[2].set_data(range(samples), data[2])

def SendLed1():
    global LED1
    if LED1 == 0:
        serialConnection.write(b'1')
        LED1 = 1
        return 0

    if LED1 == 1:
        serialConnection.write(b'2')
        LED1 = 0
        return 0

def SendLed2():
    global LED2
    if LED2 == 0:
        serialConnection.write(b'3')
        LED2 = 1
        return 0

    if LED2 == 1:
        serialConnection.write(b'4')
        LED2 = 0
        return 0

def SendLed3():
    global LED3
    if LED3 == 0:
        serialConnection.write(b'5')
        LED3 = 1
        return 0

    if LED3 == 1:
        serialConnection.write(b'6')
        LED3 = 0
        return 0

# --------Ventana---------------------------------------------------------

window = Tk()  # Ventana principal
window.geometry('700x700')
window.wm_title('Sensado de datos')
window.minsize(width=700, height=700)

# ---------------Grafica 1---------------------------------------------

fig = plt.figure(figsize = (4,2))
lim = plt.axes(xlim=(0, samples), ylim=(0,6))  #Limites X y Y de la grafica 1
plt.title('POTENCIOMETRO')
plt.grid()
lim.set_xlabel('Num muestras')
lim.set_ylabel('Voltaje (V)')
graphs[0]=lim.plot([],[])[0]

canvas = FigureCanvasTkAgg(fig, master=window)
canvas._tkcanvas.grid(row=0, column=0, pady=15, padx=10)

# ---------------Grafica 2---------------------------------------------

fig2 = plt.figure(figsize = (4,2))
lim2 = plt.axes(xlim=(0, samples), ylim=(0,40))  #Limites X y Y de la grafica 1
plt.title('DISTANCIA')
plt.grid()
lim2.set_xlabel('Num muestras')
lim2.set_ylabel('Distancia (cm)')
graphs[1]=lim2.plot([],[])[0]

canvas2 = FigureCanvasTkAgg(fig2, master=window)
canvas2._tkcanvas.grid(row=1, column=0, pady=15, padx=10)

# ---------------Grafica 3---------------------------------------------

fig3 = plt.figure(figsize = (4,2))
lim3 = plt.axes(xlim=(0, samples), ylim=(0,50))  #Limites X y Y de la grafica 1
plt.title('TEMPERATURA')
plt.grid()
lim3.set_xlabel('Num muestras')
lim3.set_ylabel('Grados (°C)')
graphs[2]=lim3.plot([],[])[0]

canvas3 = FigureCanvasTkAgg(fig3, master=window)
canvas3._tkcanvas.grid(row=2, column=0, pady=15, padx=10)

Linea = Thread(target=getSerialData)
Linea.start()

#-----------------Animacion graficas-----------------------

anim = animation.FuncAnimation(fig, graphData1, fargs=(graphs), interval=samples)
anim2 = animation.FuncAnimation(fig2, graphData2, fargs=(graphs), interval=samples)
anim3 = animation.FuncAnimation(fig3, graphData3, fargs=(graphs), interval=samples)

#------------------Frames----------------------------------

frame4 = Frame(window, bd=1)  # Frame para el boton
frame4.grid(column=2, row=0)

frame5 = Frame(window, bd=1)  # Frame para los leds
frame5.grid(column=2, row=1)

# --------Botones-------------------------------------------------------------

but1 = Button(text='B1', width=15, bg='white', fg='black',
              command=button1).grid(column=1, row=0, pady=5, padx=10)  # Boton 1

but2 = Button(text='B2', width=15, bg='white', fg='black',
              command=button2).grid(column=1, row=1, pady=5, padx=10)  # Boton 2

but3 = Button(text='B3', width=15, bg='white', fg='black',
              command=button3).grid(column=1, row=2, pady=5, padx=10)  # Boton 3

but4 = Button(frame4, text='B4', width=15, bg='white', fg='black',
              command=button4).grid(column=0, row=0, pady=5, padx=8)  # Boton 4

but5 = Button(frame5, text='LED 1', width=15, bg='red', fg='black',
              command=SendLed1).grid(column=0, row=0, pady=5, padx=8)  # LED 1

but6 = Button(frame5, text='LED 2', width=15, bg='red', fg='black',
              command=SendLed2).grid(column=0, row=1, pady=5, padx=8)  # LED 2

but7 = Button(frame5, text='LED 3', width=15, bg='red', fg='black',
              command=SendLed3).grid(column=0, row=2, pady=5, padx=8)  # LED 3

window.mainloop()
serialConnection.close()  # cerrar el puerto