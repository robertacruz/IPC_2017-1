# Na usina de Angra dos Reis, os técnicos analisam a perda de massa de um material
# radioativo. Sabendo-se que este perde 25% de sua massa a cada 30 segundos. Criar um
# algoritmo em PORTUGOL que calcule iterativamente e imprima o tempo necessário
# para que a massa deste material se torne menor que 0,10 grama. O algoritmo pode
# calcular o tempo para várias massas.

while 1:
    massa = float(input("Informe massa do material em gramas: "))
    tempo = 0
    if massa > 0.1:
        while massa > 0.1:
            massa = massa * 0.25
            tempo = tempo + 30
        print("Massa Final = %.2f gramas\nTempo = %i segundos" % (massa, tempo))
    else:
        print("Massa inferior a 0,1")
    op = 'p'
    while 1:
        op = input("Deseja continuar?\t[s]Sim\t[n]Nao\nOpção: ")
        if op == 's' or op == 'S':
            break
        elif op == 'n' or op == 'N':
            exit(0)
        else:
            print("Opção invalida. Tente novamente!!")
