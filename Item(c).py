import matplotlib.pyplot as plt
import numpy as np
import math

# Definindo a função
def f(x):
    return np.power(x, 1/3)  # Função f(x) = x^(1/3)

# Derivada da função f(x)
def df(x):
    return 1 / (3 * np.power(x, 2/3))  # Derivada de f(x)

# Método de Newton-Raphson para encontrar a raiz de f(x)
def newton_raphson(f, df, x0, eps, maxiter):
    iter = 0
    lista = [x0]  
    print(f"Iteração {iter}: x = {x0:.5f}, f(x) = {f(x0):.5f}")
    while iter <= maxiter:
        xk = x0 - f(x0) / df(x0)  # Fórmula de Newton-Raphson
        lista.append(xk)
        iter += 1
        print(f"Iteração {iter}: x = {xk:.5f}, f(x) = {f(xk):.5f}")
        if (math.fabs(f(x0)) < eps) or (math.fabs(xk - x0) < eps):
            break
        else:
            x0 = xk
    return xk, iter, lista

# Parâmetros para o método de Newton-Raphson
x0 = 0.1  # Valor inicial (positivo)
eps = 1e-6  
maxiter = 20  # Número máximo de iterações

# Encontrando a raiz
xk, iter, lista = newton_raphson(f, df, x0, eps, maxiter)

# Definindo o intervalo de x para o gráfico
x = np.arange(-10, 100, 0.01)  # Intervalo (visualização)

# Calculando a reta tangente no ponto x0
def reta_tangente(x, x0, f, df):
    return f(x0) + df(x0) * (x - x0)


# Plotando o gráfico de f(x)
plt.figure()
plt.grid()
plt.plot(x, f(x), 'b-', label='f(x) = x^(1/3)')  # Gráfico de f(x)
# plotando a reta tangente em x0
plt.plot(x, reta_tangente(x, x0, f, df), 'r--', label='Reta tangente em x0')

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
plt.xlim(-1, 20)
plt.ylim(-2, 5)

# Exibindo o gráfico
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método de Newton-Raphson para f(x) = x^(1/3)')
plt.legend()
plt.show()

# Resultados finais
print(f'\nRaiz encontrada:')
print(f'x = {xk:.5f}')
print(f'f(x) = {f(xk):.5f}')
print(f'Número de iterações: {iter}')
