import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd  

# Definindo a função
def f(x):
    return np.power(x, 3) - (5 * x)  # Função f(x) = x^3 - 5x

# Derivada da função f(x)
def df(x):
    return 3 * np.power(x, 2) - 5  # Derivada de f(x)

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
x0 = -1 # Valor inicial 
eps = 1e-6  
maxiter = 9  # Número máximo de iterações

# Encontrando a raiz
xk, iter, lista = newton_raphson(f, df, x0, eps, maxiter)

# Definindo o intervalo de x para o gráfico
x = np.arange(-5,5, 0.01)  # Intervalo (visualização)

# Plotando o gráfico de f(x)
plt.figure()
plt.grid()
plt.plot(x, f(x), 'b-', label='f(x) = x^3 - 5x')  # Gráfico de f(x)

# Criar uma tabela com os resultados das iterações
tabela_resultados = pd.DataFrame({
    'Iteração':"--------",
    'x_n  ' : lista,
    'f(x_n)' : [f(x) for x in lista]
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
plt.plot(xk, f(xk), 'ko', label='Raiz encontrada')  # Ponto da raiz
plt.text(xk, f(xk), f'Raiz: ({xk:.5f}, {f(xk):.5f})', fontsize=12)

# Ajustando os limites dos eixos para melhor visualização
plt.xlim(-2.5, 2.5)
plt.ylim(-5, 5)

# Exibindo o gráfico
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método de Newton-Raphson para f(x) = x^3 - 5x')
plt.legend()
plt.show()