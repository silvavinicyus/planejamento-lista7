from scipy import stats
import numpy as np
from math import sqrt

tamanho = [128, 256, 384, 512, 640, 768, 896, 1024]
obMedia = [384.66,826.33, 1580.33, 3131.33, 6722.33, 13970, 27719, 51468.33]

m, b, r_value, p_value, std_err = stats.linregress(tamanho, obMedia)

b0 = b
b1 = m

# Calculos valores para o intervalo de confiança

somXY = 0
somYquad = 0
somXQuad = 0
somY = np.sum(obMedia)

for i in tamanho:
  somXQuad += (i * i) 

for i in obMedia:
  somYquad += (i * i) 

for i in range(0, 8): 
  somXY += (tamanho[i]*obMedia[i])

#Calculando o SSE

SSE = somYquad - (b0 * somY) - (b1 * somXY)


#Calculando se

se = sqrt(SSE/6)

print(se)


#Calculando sb0 e sb1

xmean = np.mean(tamanho)

sb0 = se * ((1/8) + (xmean*xmean)/(somXQuad - (8 * (xmean*xmean)))) ** 1/2

sb1 = se / (somXQuad - (8 * (xmean*xmean)))**1/2

print("sb0 = ", sb0)
print("sb1 = ", sb1)

#Achando o intervalo de confiança

limiteInferiorb0 = b0 - ((1.943)*sb0)
limiteSuperiorb0 = b0 + ((1.943)*sb0)


limiteInferiorb1 = b1 - ((1.943)*sb1)
limiteSuperiorb1 = b1 + ((1.943)*sb1)

print("Limites para b0: ")
print("["+str(limiteInferiorb0)+",  "+str(limiteSuperiorb0)+"]")

print("Limites para b1: ")
print("["+str(limiteInferiorb1)+",  "+str(limiteSuperiorb1)+"]")