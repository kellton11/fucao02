# Crie uma função chamada verificar_paridade
#  que receba um número inteiro como argumento e retorne uma mensagem indicando se o número é par ou ímpar.
def verificar_paridade():
    b = int(input("digite um numero inteiro : "))
    if b %2==0:
        return "par"
    else:
        return "impar"
resultado = verificar_paridade()
print(resultado)
