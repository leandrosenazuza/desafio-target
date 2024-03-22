# Regra da sequência de Fibonacci: Primeiro e segundo termo igual a 1
def geradorSequencia(n):
    fibonacciSequencia = [0, 1]
    while fibonacciSequencia[-1] <= n:
        fibonacciSequencia.append(fibonacciSequencia[-1] + fibonacciSequencia[-2])
    return fibonacciSequencia[:-1]

def verificaSePertence(n):
    fibonacciSequencia = geradorSequencia(n)
    if n in fibonacciSequencia:
        return True
    else:
        return False

def verificaPrimeirosValores(numero):
    if numero == 1:
        return True

numero = int(input("Entre com um número: "))

if verificaPrimeirosValores(numero):
    print("\nValor digitado pode ser o primeiro ou segundo termo da sequência.")
if verificaSePertence(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
