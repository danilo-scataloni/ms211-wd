import matplotlib.pyplot as plt
import numpy as np
import math
# Definindo as funções
def f(x):
    return 1 / x  # Função f(x) = 1/x
def g(x):
    return 1 + np.power(x, 3)  # Função g(x) = 1 + x^3
# Função h(x) = f(x) - g(x) para encontrar a interseção entre f(x) e g(x)
def h(x):
    return f(x) - g(x) # Função h(x) = f(x) - g(x)  

# Derivada de h(x)
def dh(x):
    return (-1 / np.power(x, 2)) - 3 * np.power(x, 2)  # Derivada de h(x)
#Valor Inicial
x0 = 2  # Valor inicial (positivo)

# Método de Newton-Raphson para encontrar a interseção
def newton_raphson(h, dh, x0, eps1, eps2, maxiter):
    iter = 0
    lista = [x0]  # Lista para armazenar os pontos
    print("Tabela de Resultados:")
    print(f"Valor Inicial:",x0)
    print(f"Iteração {iter}: x = {x0:.5f} | f(x) = {f(x0):.5f} | g(x) = {g(x0):.5f} |  h(x) = {h(x0):.5f}")
    while iter <= maxiter:
        xk = x0 - h(x0) / dh(x0)  # Fórmula de Newton-Raphson
        lista.append(xk)
        iter += 1
        print(f"Iteração {iter}: x = {xk:.5f} | f(x) = {f(xk):.5f} | g(x) = {g(x0):.5f} |  h(x) = {h(xk):.5f}")
        if (math.fabs(h(x0)) < eps1) or (math.fabs(xk - x0) < eps2):
            break
        else:
            x0 = xk
    return xk, iter, lista

# Parâmetros para o método de Newton-Raphson
eps1 = 1e-6  # Tolerância para |h(x)|
eps2 = eps1  # Tolerância para |x_k - x_{k-1}|
maxiter = 20  # Número máximo de iterações

# Encontrando a interseção
xk, iter, lista = newton_raphson(h, dh, x0, eps1, eps2, maxiter)

# Definindo o intervalo de x para o gráfico
x = np.arange(0.1, 10, 0.01)  # Intervalo (visualização)

# Plotando o gráfico de f(x) e g(x)
plt.figure()
plt.grid()
plt.plot(x, f(x), 'b--', label='f(x) = 1/x')  # Gráfico de f(x)
plt.plot(x, g(x), 'g--', label='g(x) = 1 + x^3')  # Gráfico de g(x)
plt.plot(x,h(x),'b-',label='h(x) = f(x) - g(x)') # Gráfico de h(x)


# Plotando os pontos gerados pelo método de Newton-Raphson
cont = 0
for x_point in lista:
    plt.plot(x_point, h(x_point), 'ro')  # Pontos em vermelho
    name = f'$x_{cont}$'
    plt.text(x_point, 0.1 * f(x_point), name, fontsize=12)  # Rótulos dos pontos
    cont += 1

# Plotando o ponto de interseção
plt.plot(xk, f(xk), 'ko', label='Interseção')  # Ponto de interseção
plt.text(xk, f(xk), f'Interseção: ({xk:.5f}, {f(xk):.5f})', fontsize=12)

# Ajustando os limites dos eixos para melhor visualização
plt.xlim(0.1, 10)
plt.ylim(-10, 10)

# Exibindo o gráfico
plt.xlabel('x')
plt.ylabel('f(x) e g(x)')
plt.title('Interseção entre f(x) = 1/x e g(x) = 1 + x^3')
plt.legend()
plt.show()

# Resultados finais
print(f'\nInterseção encontrada:')
print(f'x = {xk:.5f}')
print(f'f(x) = g(x) = {f(xk):.5f}')
print(f'Número de iterações: {iter}')
