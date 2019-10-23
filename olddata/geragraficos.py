from random import randint
import matplotlib.pyplot as plt #sudo apt install python3-matplotlib
import matplotlib.animation as animation #sudo apt install python3-tk



fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

xs = [1, 2, 3, 4, 5, 6, 7, 8]
ys = [10, 20, 30 ,40 , 50 ,60 , 70, 80]


#incremento partindo dos ultimos valores de cada lista
temperatura=80
tempo=8;

#funcao para animar
def animate(i, xs, ys):
    global temperatura
    global tempo

    #incremento
    #temperatura= temperatura+10
    temperatura= randint(0, 100)
    tempo = tempo + 1

    #append índice do tempo e temperatura
    xs.append(tempo)
    ys.append(temperatura)


    # desenhar x e y
    ax.clear()
    ax.plot(xs, ys)


    plt.title('Temperatura Atual e Tempo')
    plt.ylabel('Temperatura')

# altere o valor do interval para que que o frame seja atualizado de maneira mais rápida ou não
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
