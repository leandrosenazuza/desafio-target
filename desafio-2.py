# Regra da sequência de Fibonacci: Primeiro e segundo termo igual a 1
def geradorSequencia(numero):
    fibonacciSequencia = [1, 1]
    while fibonacciSequencia[-1] <= numero:
        fibonacciSequencia.append(fibonacciSequencia[-1] + fibonacciSequencia[-2])
    return fibonacciSequencia[:-1]

def verificaSePertence(numero):
    fibonacciSequencia = geradorSequencia(numero)
    if numero in fibonacciSequencia:
        return True
    else:
        return False

def verificaPrimeirosValores(numero):
    if numero == 1:
        return True
def verificaPosicao(numero):
    fibonacciSequencia = geradorSequencia(numero)
    return fibonacciSequencia.index(numero)



#inicio da execucao, sem main
numero = int(input("Entre com um número: "))

if verificaPrimeirosValores(numero):
    print(f"Valor digitado pode ser o primeiro ou segundo termo da sequência.")
if verificaSePertence(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
    print(f"O número {numero} está na posição {verificaPosicao(numero)}")

else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
