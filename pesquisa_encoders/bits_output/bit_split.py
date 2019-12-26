import numpy

w = 1920
h = 1080

yuvi = open('D:/Rafael/Pesquisa_Mestrado/ref_tb/ParkScene_1920x1080_24.yuv','rb')

yuv = numpy.fromfile(yuvi, dtype=numpy.uint8, count = w*h)
numpy.savetxt( "entradas_n4.txt", yuv.reshape(-1,12), delimiter = " ", fmt = '%d')
numpy.savetxt("entradas_n8.txt", yuv.reshape(-1,16), delimiter = " ", fmt = '%d')
numpy.savetxt( "entradas_n16.txt", yuv.reshape(-1,24), delimiter = " ", fmt = '%d')
numpy.savetxt("entradas_n32.txt", yuv.reshape(-1,40), delimiter = " ", fmt = '%d')
numpy.savetxt( "entradas_n64.txt", yuv.reshape(-1,72), delimiter = " ", fmt = '%d')
