# PDS-Lab1
Proyecto de comunicación serial entre un microcontrolador que lee sensores
análogos y GUI desarrollada en python para ver resultados en tiempo real.


En grupos de máximo 3 personas, realice las siguientes actividades:

-Ahora habilitado para trabajar de forma remota y conjunta

● Usando el generador de ondas disponible en el laboratorio, proceda a
obtener señales sinusoidales. Verifique que conoce y maneja el equipo
mencionado de forma que pueda configurar los diferentes parámetros
(amplitud, frecuencia y nivel DC) de la señal. La frecuencia de las señales
generadas deben variar entre 10 a 100 ciclos por segundo.

● Diseñar e implementar un dispositivo para digitalización de señales:
Mediante un micro-controlador (STM32), realizar la digitalización de la señal
análoga proveniente del generador de ondas de acuerdo con el punto
anterior. Debe ajustar la frecuencia de muestreo a 200 muestras/segundo,
verifique la frecuencia de muestreo mediante la generación de un pulso en
un pin de salida que ocurra en cada instante de muestreo, verifique con el
osciloscopio el tiempo. La información digitalizada debe ser enviada al PC
hacia una aplicación que le permita visualizar los datos que llegan (valores
numéricos de los datos transmitidos).

● Desarrolle un programa propio en algún lenguaje apropiado (Java, C/C++,
Python) que permita guardar los valores de voltaje en un archivo en el disco
duro del computador. Esto con el fin de poder comparar su datos
experimentales con simulaciones realizadas en matlab.


● Utilizando el hardware implementado realice lo siguiente:

■ Desde el generador de señales y con ayuda del osciloscopio obtenga
señales sinusoidales con frecuencias entre 10 a 100 Hz en pasos de
10 Hz. Observe los datos digitalizados en el computador, determine
los valores de frecuencia y realice una tabla donde relacione el valor
de frecuencia de la señal análoga y el correspondiente valor de
frecuencia normalizada de la señal digitalizada.

■ Configure la frecuencia de la señal generada a 100 Hz. Haga la
medición de frecuencia. Observe la señal digitalizada y determine la
frecuencia normalizada de la misma. Realice varias mediciones
reiniciando el dispositivo de adquisición, describa cómo se afecta la
señal en cada medición realizada.

■ A partir del punto anterior empiece a disminuir el periodo (aumentar la
frecuencia) de la señal análoga, observe la señal digitalizada en el
computador, observe y compare los valores con la tabla que realizó
antes. Indique si encuentra coincidencias en el valor de la frecuencia
normalizada de las señales digitalizadas. Explique qué ocurre con los
datos capturados en el PC cuando la frecuencia de la señal análoga
es igual o mayor a 100 Hz.


Ejercicio en matlab:

● Escribir un programa en Matlab donde se simulen las señales análogas
periódicas obtenidas desde el generador de señal: Realice la simulación del
proceso de muestreo de la señal análoga, tenga en cuenta que los
parámetros como la frecuencia de la señal simulada y la frecuencia de
muestreo, deben ser los mismos tanto en el sistema de adquisición como
en la simulación.

● Estimación de la fidelidad del sistema de adquisición: Escriba una función
que cargue los datos capturados desde el hardware de digitalización,
Calcule el PSNR y MSE entre los capturados y los datos simulados (utilice
la ayuda de matlab para el uso de las funciones respectivas). Obtenga el
máximo valor de PSNR y mínimo de MSE ajustando la fase de la señal
generada con la simulación. Tenga en cuenta que los datos capturados
(reales del sistema de adquisición) y los datos simulados deben estar
almacenados en arreglos del mismo tamaño (igual número de muestras).
Teniendo en cuenta los valores alcanzados, ¿Puede considerar que su
sistema es de alta fidelidad?

● Estimación del error de cuantificación: Con los datos obtenidos de la
digitalización de la señal análoga desde el generador de ondas y los datos
de la simulación ajustada en fase, calcule el error de cuantificación
comparando los resultados de la simulación (valor teórico) con el valor
observado de la digitalización de la señal real (valor experimental).
Determine entre los datos de simulación y los reales, Media y Varianza del
error.

● Modifique en el microcontrolador el número de bits utilizados por el C A/D,
repita el cálculo de los parámetros estadísticos del error de cuantificación
(Media y varianza del error).

● Con estos resultados, ¿Qué puede afirmar sobre el error de cuantificación?
¿Las características observadas reflejan la teoría?
