from tkinter import Tk, Frame, Button, Label, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import serial
import collections
import matplotlib.pyplot as plt
import matplotlib.animation as animaciones
from matplotlib.lines import Line2D
from threading import Thread

global L1, L2, L3, Boton1,Boton2,Boton3,c
Muestras = 70; graficas = [];datos = [];
#Window
window = Tk()  #interfaz principal
window.geometry('900x900')
window.wm_title('Laboratorio 1 Comunicaciones ')
window.minsize(width=900, height=900)
try:
    SerialC = serial.Serial('COM6', 9600)
except:
    print('Error en conexion Serial')

for c in range(3):
    datos.append(collections.deque([0] * Muestras, maxlen=Muestras))
    graficas.append(Line2D([], [], color='magenta'))
def getSDatos():
    global c
    while True:
        for f in range(3):
            for j in range(59):
                datos[f][j] = float(datos[f][j+1])

        valor = SerialC.readline().decode('utf-8')
        datos[c][69] = valor
        c = c + 1
        if c == 3:
            c = 0

def Click1():
    global Boton1,Boton2,Boton3
    Boton1=1;Boton2=0;Boton3=0
def Click2():
    global Boton1, Boton2, Boton3
    Boton1 = 0; Boton2 = 1; Boton3 = 0
def Click3():
    global Boton1, Boton2, Boton3
    Boton1 = 0;    Boton2 = 0; Boton3 = 1
def Click4():
    global Boton1, Boton2, Boton3
    Boton1 = 1; Boton2 = 1; Boton3 = 1

def Graficos():
    global Boton1, Boton2, Boton3
    if Boton1 == 1:
        graficas[0].set_data(range(Muestras), datos[0])
    if Boton2 == 1:
        graficas[1].set_data(range(Muestras), datos[1])
    if Boton3 == 1:
        graficas[2].set_data(range(Muestras), datos[2])
def LED1():
    global L1
    L1 = 1
    Leds()
def LED2():
    global L2
    L2 = 1
    Leds()
def LED3():
    global L3
    L3 = 1
    Leds()
def Leds():
    global L1,L2,L3
    if L1 == 0:
        SerialC.write(b'1')
        L1 = 1
        return 0
    if L1 == 1:
        SerialC.write(b'2')
        L1 = 0
        return 0
    if L2 == 0:
        SerialC.write(b'3')
        L2 = 1
        return 0
    if L2 == 1:
        SerialC.write(b'4')
        L2 = 0
        return 0
    if L3 == 0:
        SerialC.write(b'5')
        L3 = 1
        return 0
    if L3 == 1:
        SerialC.write(b'6')
        L3 = 0
        return 0
# ---------------Grafica 1---------------------------------------------

fig1 = plt.figure(figsize = (4, 2))
Ejes = plt.axes(xlim=(0, Muestras), ylim=(0, 6))  #Limites X y Y de la grafica 1
plt.title('POTENCIOMETRO')
plt.grid()
Ejes.set_xlabel('Num muestras')
Ejes.set_ylabel('Voltaje (V)')
graficas[0] = Ejes.plot([], [])[0]

canvas = FigureCanvasTkAgg(fig1, master=window)
canvas._tkcanvas.grid(row=0, column=0, pady=15, padx=10)

# ---------------Grafica 2---------------------------------------------

fig2 = plt.figure(figsize = (4,2))
Ejes2 = plt.axes(xlim=(0, Muestras), ylim=(0,40))  #Limites X y Y de la grafica 1
plt.title('DISTANCIA')
plt.grid()
Ejes2.set_xlabel('Num muestras')
Ejes2.set_ylabel('Distancia (cm)')
graficas[1]=Ejes2.plot([],[])[0]

canvas2 = FigureCanvasTkAgg(fig2, master=window)
canvas2._tkcanvas.grid(row=1, column=0, pady=15, padx=10)

# ---------------Grafica 3---------------------------------------------

fig3 = plt.figure(figsize = (4,2))
ejes3 = plt.axes(xlim=(0, Muestras), ylim=(0,50))  #Limites X y Y de la grafica 1
plt.title('TEMPERATURA')
plt.grid()
ejes3.set_xlabel('Num muestras')
ejes3.set_ylabel('Grados (°C)')
graficas[2]=ejes3.plot([],[])[0]

canvas3 = FigureCanvasTkAgg(fig3, master=window)
canvas3._tkcanvas.grid(row=2, column=0, pady=15, padx=10)

Linea = Thread(target=getSDatos())
Linea.start()

#-----------------Animacion graficas-----------------------

anim = animaciones.FuncAnimation(fig1, Graficos(), fargs=(graficas), interval=Muestras)
anim2 = animaciones.FuncAnimation(fig2, Graficos, fargs=(graficas), interval=Muestras)
anim3 = animaciones.FuncAnimation(fig3, Graficos, fargs=(graficas), interval=Muestras)

#------------------Frames----------------------------------

frame4 = Frame(window, bd=1)  # Frame para el boton
frame4.grid(column=2, row=0)

frame5 = Frame(window, bd=1)  # Frame para los leds
frame5.grid(column=2, row=1)

# --------Botones-------------------------------------------------------------

but1 = Button(text='B1', width=15, bg='white', fg='black',
              command=Click1()).grid(column=1, row=0, pady=5, padx=10)  # Boton 1

but2 = Button(text='B2', width=15, bg='white', fg='black',
              command=Click2()).grid(column=1, row=1, pady=5, padx=10)  # Boton 2

but3 = Button(text='B3', width=15, bg='white', fg='black',
              command=Click3()).grid(column=1, row=2, pady=5, padx=10)  # Boton 3

but4 = Button(frame4, text='B4', width=15, bg='white', fg='black',
              command=Click4()).grid(column=0, row=0, pady=5, padx=8)  # Boton 4

but5 = Button(frame5, text='LED 1', width=15, bg='red', fg='black',
              command=LED1()).grid(column=0, row=0, pady=5, padx=8)  # LED 1

but6 = Button(frame5, text='LED 2', width=15, bg='red', fg='black',
              command=LED2()).grid(column=0, row=1, pady=5, padx=8)  # LED 2

but7 = Button(frame5, text='LED 3', width=15, bg='red', fg='black',
              command=LED3()).grid(column=0, row=2, pady=5, padx=8)  # LED 3

window.mainloop()
SerialC.close()  # cerrar el puerto