import matplotlib.pyplot as plt #sudo apt install python3-matplotlib
import matplotlib.animation as animation #sudo apt install python3-tk
import numpy as np
import serial

ser=serial.Serial('/dev/ttyACM0',9600)

#fig = plt.figure()
#ax = fig.add_subplot(1,1,1)
fig, ax = plt.subplots()

#valores iniciais
xs = [0]
ys = [0]
tempo=0

#funcao para animar
def animate(i, xs, ys):
     global tempo
     tempo = tempo + 1

     #recebe o valor da serial
     volt= ser.readline()

     #incremento do novo valor

     #v=volt
     #v=int(v)
     xs.append(tempo)
     ys.append(volt)

     #mantem grafico dentro do intervalo de 100 plots
     if tempo > 100:
         xs = xs[tempo-99:tempo]
         ys = ys[tempo-99:tempo]

     ax.clear()
     # desenhar x e y
     ax.plot(xs, ys)

     plt.title('Medidor de Tensao')
     plt.ylabel('Volts')
     plt.xlabel('Tempo')

# altere o valor do interval para que que o frame seja atualizado de maneira mais rapida ou nao
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1)
plt.show()
