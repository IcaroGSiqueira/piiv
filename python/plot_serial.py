
import matplotlib.pyplot as plt #sudo apt install python3-matplotlib
import matplotlib.animation as animation #sudo apt install python3-tk
import numpy as np #sudo apt install python3-numpy
import serial #sudo apt install python3-pip #sudo python -m pip install pyserial

ser=serial.Serial('/dev/ttyACM0',9600)

#fig = plt.figure()
#ax = fig.add_subplot(1,1,1)
fig, ax = plt.subplots()

#define o maximo de pontos plotados no grafico
n=60

#valores iniciais
xs = [0.0]
ys = [0.0]
tempo=0

#funcao para animar
def animate(i, xs, ys):
     global tempo
     tempo = tempo + 1

     #recebe o valor da serial
     output= ser.readline()
     print(output)
     output=output[0:-2]
     print(output)
     #incremento do novo valor
     xs.append(tempo)
     ys.append(int(output))

     #mantem grafico dentro do intervalo de n plots
     if tempo > n:
         xs = xs[tempo-(n-1):tempo]
         ys = ys[tempo-(n-1):tempo]

     ax.clear()

     # desenhar x e y
     ax.plot(xs, ys)

     plt.title('Medidor de Tensao PWM')
     plt.ylabel('Volts')
     plt.xlabel('Tempo')

# altere o valor de "interval" para que que o frame seja atualizado de maneira mais rapida
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1)
plt.show()