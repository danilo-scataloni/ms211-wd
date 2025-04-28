import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd  

# Definindo a função
def f(x):
    return np.power(x, 3) - (2 * x) + 2  # Função f(x) = x^3 - 2x + 2

# Derivada da função f(x)
def df(x):
    return 3 * np.power(x, 2) - 2  # Derivada de f(x)

# Método de Newton-Raphson para encontrar a raiz de f(x)
def newton_raphson(f, df, x0, eps, maxiter):
    iter = 0
    lista = [x0]  # Lista para armazenar os pontos
    while iter <= maxiter:
        xk = x0 - f(x0) / df(x0)  # Fórmula de Newton-Raphson
        lista.append(xk)
        iter += 1
        if (math.fabs(f(x0)) < eps) or (math.fabs(xk - x0) < eps):
            break
        else:
            x0 = xk
    return xk, iter, lista

# Parâmetros para o método de Newton-Raphson
x0 = 5 # Valor inicial 
eps = 1e-6  # Tolerância
maxiter = 50 # Número máximo de iterações

# Encontrando a raiz
xk, iter, lista = newton_raphson(f, df, x0, eps, maxiter)

# Definindo o intervalo de x para o gráfico
x = np.arange(-5, 6, 0.01)  # Intervalo (visualização)

# Plotando o gráfico de f(x)
plt.figure()
plt.grid()
plt.plot(x, f(x), 'b-', label='f(x) = x^3 - 2x + 2')  # Gráfico de f(x)

# Criar uma tabela com os resultados das iterações
tabela_resultados = pd.DataFrame({
    'Iteração': range(len(lista)),
    'x_n': lista,
    'f(x_n)': [f(x) for x in lista]
})

# Exibir a tabela no console
print("\nTabela de Resultados:")
print(tabela_resultados)

# Exibir os resultados finais
print(f'\nRaiz encontrada:')
print(f'x = {xk:.5f}')
print(f'f(x) = {f(xk):.5f}')
print(f'Número de iterações: {iter}')

# Plotando os pontos gerados pelo método de Newton-Raphson
cont = 0
for x_point in lista:
    plt.plot(x_point, f(x_point), 'ro')  # Pontos em vermelho
    name = f'$x_{cont}$'
    plt.text(x_point, f(x_point), name, fontsize=12)  # Rótulos dos pontos
    cont += 1

# Plotando o ponto da raiz
plt.plot(xk, f(xk), 'ko') # Ponto da raiz

# Ajustando os limites dos eixos para melhor visualização
plt.xlim(-5, 6)
plt.ylim(-6, 10)

# Exibindo o gráfico
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método de Newton-Raphson para f(x) = x^3 - 2x + 2')
plt.legend()
plt.show()