import matplotlib.pyplot as plt #sudo apt install python3-matplotlib
import matplotlib.animation as animation #sudo apt install python3-tk
import numpy as np #sudo apt install python3-numpy
import serial #sudo python -m pip install pyserial
#sudo apt install python3-pip

ser=serial.Serial('/dev/ttyACM0',9600)

#fig = plt.figure()
#ax = fig.add_subplot(1,1,1)
fig, ax = plt.subplots()

#valores iniciais
xs = [0.0]
ys = [0.0]
tempo=0

#funcao para animar
def animate(i, xs, ys):
     global tempo
     tempo = tempo + 1

     #recebe o valor da serial
     volt= ser.readline()
     volt=volt[:4]
     #incremento do novo valor
     xs.append(tempo)
     ys.append(float(volt))

     #mantem grafico dentro do intervalo de 60 plots
     if tempo > 60:
         xs = xs[tempo-59:tempo]
         ys = ys[tempo-59:tempo]

     ax.clear()

     # desenhar x e y
     ax.plot(xs, ys)

     plt.title('Medidor de Tensao')
     plt.ylabel('Volts')
     plt.xlabel('Tempo')

# altere o valor do interval para que que o frame seja atualizado de maneira mais rapida ou nao
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1)
plt.show()
