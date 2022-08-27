controle = 1 #variavel de controle da repeticao
#laco de controle do menu interativo
while controle == 1:
    num = int(input("Digite quantos elementos você quer imprimir: "))
    a,b = 0,1
    cont = 2 #variavel contadora
    print("Sequência de Fibonacci")
    print(a,b, end=" ") #imprime os dois primeiros valores
    #laco de repeticao para calcular a sequencia
    while cont<num:
        a,b = b, a+b #atualiza os valores da sequencia
        print (b, end=" ") #imprime valor atual da sequencia
        cont+=1 #incrementa a variavel contadora
    print() #quebra de linha
    #menu interativo para repetir o calculo da sequencia
    controle = int(input("Digite 1 para continuar ou 0 para parar: "))
