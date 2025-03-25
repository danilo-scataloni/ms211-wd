import numpy as np
import matplotlib as plt
import math

#Valores iniciais
b = math.pi
x0_1 = 0.5
x0_2 = 0.7
reciproco_pi = 1/b
erro_maximo = 0.0000001

#Funções:
def f(x):
    return b - 1/x

def x_n_mais_um(x_n):
    return x_n*(2-b*x_n)
#Metodo de Newthon simplificado

#Iterações
x_n = x0_1
valores_iteracao = [x0_1]

while (True):
    iteracao = x_n_mais_um(x_n)
    valores_iteracao.append(iteracao)
    x_n = iteracao

    if (math.fabs(x_n-reciproco_pi)) < erro_maximo:
        break

print(valores_iteracao)