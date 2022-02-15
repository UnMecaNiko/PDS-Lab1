function funcion_graficas(NombreArchivo,freq,fase)
%se leen los datos y se dejan en un vector columna
[A,delimiterOut]=importdata(NombreArchivo);
A=double(A');
figure

%se saca una cantidad de datos para que se pueda observar ls señles
num=100;
nmuestras=num/200;

%se normaliza la señal leida
for c=1:1:1000
    A(c)=A(c)./max(A);
end

%se sacaban los N numeros que se querian graficar de todas
for c=1:1:num
    B(c)=A(c);
end


%se genera los datos en el eje x para luego grficar
x=0:1/200:nmuestras-1/200;
plot(x,B)
xlabel("tiempo(seg)")
ylabel("voltaje(V)")
hold on

%se sacaba la frecuencia angular y se define la señal ideal
w=2*pi()*freq;
y=1.5*sin(w*x+fase);

%se le coloca un offset de 1.5 para que queden los datos positivos
for c=1:1:num
    y(c)=y(c)+1.5;
end

%se normaliza la señal y se grafica
for c=1:1:num
    y(c)=y(c)./max(y);
end
plot(x,y)
grid on

%calculo de el psnr y error cuadratico medio
Valor_psnr=psnr(B,y)
Error_cuadratico_edio=immse(B,y)

%calcul de la media
media_teorica=mean(y)
media_experimental=mean(B)
Error_de_estimacion=(abs(media_teorica-media_experimental))/media_teorica

%calculo de la varianza
varianzaE=var(B)
varianzaT=var(y)
ErrorDeLasVarianzas=(abs(varianzaT-varianzaE))/varianzaT

end