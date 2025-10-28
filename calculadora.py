#Projeto basico de calculadora simples para estudo de testes unitários.

def verificaNumeral(a):
    if isinstance(a, (int, float, complex)):
        return True
    else:
        raise ValueError("A entrada precisa ser um número")

def somar(a, b):
    if verificaNumeral(a) and verificaNumeral(b):
        return a + b

def subtrair(a, b):
    if verificaNumeral(a) and verificaNumeral(b):
        return a - b

def multiplicar(a, b):
    if verificaNumeral(a) and verificaNumeral(b):
        return a * b

def dividir(a, b):
    if verificaNumeral(a) and verificaNumeral(b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b

def potencia(base, expoente):
    if verificaNumeral(base) and verificaNumeral(expoente):
        #ESTA CÓDIGO ESTA ERRADO, para execução do teste unitário
        #Código correto : return base ** expoente
        return base * (expoente ** 2)
        #outro bug, é que não trata se o expoente for 0
