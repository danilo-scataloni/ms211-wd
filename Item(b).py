import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

#Valores iniciais
b = math.pi
x0 = 0.7 #Valor a ser alterado para mudanças
reciproco_pi = 1/b


def x_n_mais_um(x_n):
    return x_n*(2-b*x_n)
#Metodo de Newthon simplificado

#Iterações
x_n = x0
valores_iteracao = [x0]
valores_x_n = []
max_iter = 10

while (True):
    iteracao = x_n_mais_um(x_n)
    valores_iteracao.append(iteracao)
    valores_x_n.append(x_n)
    x_n = iteracao

    if len(valores_iteracao) == max_iter:
        break


#Mostrar em tabelas as interações
df = pd.DataFrame({
    'x_n': valores_x_n,
    'x_n+1': valores_iteracao[1:]
})
print(df)


# Criar gráfico da sequência x_n por x_n_+1
#O gráfico abaixo mostra as evoluções de x_n com as iteracoes tomando como referência o valor conhecido 1/pi
plt.figure(figsize=(8, 5))
plt.plot(range(len(valores_x_n)), valores_x_n, marker='o', linestyle='-'))
plt.axhline(y=reciproco_pi, color='r', linestyle='--', label='1/π (valor real)')
plt.title("Convergência de x_n para 1/π")
plt.xlabel("Iteração")
plt.ylabel("x_n")
plt.legend()
plt.grid()

# Exibir o gráfico
plt.show()