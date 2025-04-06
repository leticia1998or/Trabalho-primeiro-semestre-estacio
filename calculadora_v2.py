saida=""
def adicao(n1,n2):
    return n1+n2

def subtracao(n1,n2):
    return n1-n2

def multiplicacao(n1,n2):
    return n1*n2

def divisao(n1,n2):
    if n1==0 or n2==0:
        print("Não foi possivel realizar a divisão por 0")
    else:
        return n1/n2
    
def calculadora(n1,n2,c3):
    if c3== "adicao" or c3 == "+":
        resultado=adicao(n1,n2)
    elif c3== "subtracao" or c3 == "-":
        resultado=subtracao(n1,n2)
    elif c3== "multiplicacao" or c3 == "*":
        resultado=multiplicacao(n1,n2)
    elif c3== "divisao" or c3 == "/":
        resultado=divisao(n1,n2)

    return resultado

while saida.lower() != "n":
    numero1 = int(input("Digite o primeiro número: "))    
    numero2 = int(input("Digite o segundo número: ")) 
    operacao = input("Digite a operação que deseja realizar: ")
    resultado = calculadora(numero1,numero2,operacao)
    print(f"Resultado da operação: {resultado}")
    saida = input("Deseja continuar? s/n: ")

