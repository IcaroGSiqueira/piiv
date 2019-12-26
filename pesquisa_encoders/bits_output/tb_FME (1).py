# tb_FME
import numpy as np

def F1 (a0,a1,a2,a3,a4,a5,a6):
	y1 = (-a0 + 4*a1 - 10*a2 + 58*a3 + 17*a4 - 5*a5 + a6 + 32)>>6
	return y1

def F2 (a0,a1,a2,a3,a4,a5,a6,a7):
	y2 = (-a0 + 4*a1 - 11*a2 + 40*a3 + 40*a4 - 11*a5 + 4*a6 - a7 + 32)>>6
	return y2

def F3 (a1,a2,a3,a4,a5,a6,a7):
	y3 = (a1 - 5*a2 + 17*a3 + 58*a4 - 10*a5+ 4*a6 - a7 + 32)>>6
	return y3

def circular_index(array, idx):
	if idx>=len(array):
		return (idx%len(array))
	return idx
	
def circular_element(array, idx):
	return array[circular_index(array, idx)]

###### MAIN ########################

line_integer = []
resultado_1 = []
resultado_2 = []
resultado_3 = []
linha_usada = []
i=1
tam=-1
while i <= 5:
	i=i+1
	arq = open("D:\\Rafael\\Pesquisa_Mestrado\\ref_tb\\entradas_n%s.txt"%(2**i), "r")
	#arq = open("/home/icaro/Documentos/bits_output/entradas_n%s.txt"%(2**i), "r")
	saida = open("D:\\Rafael\\Pesquisa_Mestrado\\ref_tb\\saida_n%s.txt"%(2**i), "w")
	#saida = open("/home/icaro/Documentos/bits_output/saida_n%s.txt"%(2**i), "w")

	lines = arq.readlines()

	j=0
	for line in lines:
		if j == tam:
			break
		j+=1

		line_integer.clear()
		resultado_1.clear()
		resultado_2.clear()
		resultado_3.clear()
		linha_usada.clear()

		resultado_1 = ["F1 = "]
		resultado_2 = ["F2 = "]
		resultado_3 = ["F3 = "]

		line_integer = line.split()

		line_integer = list(map(int,line_integer))

		tam = len(line_integer)

		for x in range((2**i)+1):

			a0 = circular_element(line_integer, x+0)
			a1 = circular_element(line_integer, x+1)
			a2 = circular_element(line_integer, x+2)
			a3 = circular_element(line_integer, x+3)
			a4 = circular_element(line_integer, x+4)
			a5 = circular_element(line_integer, x+5)
			a6 = circular_element(line_integer, x+6)
			a7 = circular_element(line_integer, x+7)
		
			resultado_f2 = F2(a0, a1, a2, a3, a4, a5, a6, a7)
			resultado_f1 = F1(a0, a1, a2, a3, a4, a5, a6)
			resultado_f3 = F3(a1, a2, a3, a4, a5, a6, a7)
			
			resultado_2.append(resultado_f2)
			resultado_1.append(resultado_f1)
			resultado_3.append(resultado_f3)

			resultado_f1 = np.clip(resultado_f1,0,255)
			resultado_f2 = np.clip(resultado_f2,0,255)
			resultado_f3 = np.clip(resultado_f3,0,255)
			
			linha = (a0,a1,a2,a3,a4,a5,a6,a7)
			linha_usada.append(linha)

			print ("x =" + str(x))
			print ("linha = " + str(line_integer))
			print ("linha = " + str(linha))
			print ("F1=" + str(resultado_f1))
			print ("F2=" + str(resultado_f2))
			print ("F3=" + str(resultado_f3))
			print ("===================")
		
		print ("linha = " + str(line_integer), file=saida)
		print ("n = %s"%2**i, file=saida)
		print (linha_usada, file=saida)
		print (resultado_1, file=saida)
		print (resultado_2, file=saida)
		print (resultado_3, file=saida)
		print ("===================", file=saida)
		
arq.close
saida.close
