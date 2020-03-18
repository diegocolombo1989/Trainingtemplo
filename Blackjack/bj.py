


# import random

# print('\t-'*20)
# print('\n')
# cab ='''                                                                   BLACKJACK                                        \n'''    
# print(cab)
# print('\t-'*20)
# print('\n'*2)

# jogadores = int(input('\nInforme a quantidade de jogadores: '))


# cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


# def embaralhar(cartas):
#     lista_embaralha = []
#     dealer = random.choice(cartas)
    
#     for dealer in cartas:
#         print(dealer)
#     return lista_embaralha
    
# print(embaralhar(dealer))

import random

print('\t-'*20)
print('\n')
cab ='''                                                                   BLACKJACK                                        \n'''    
print(cab)
print('\t-'*20)
print('\n'*2)


cartas  = ["A", "2", "3", "4","5", "6","7", "8", "9","10","J", "Q","K"]
def embaralhar(cartas):
    lista = []
    for e in range(len(cartas)):
        dealer = random.choice(cartas)
        #print(dealer)
        if 'A' in dealer[0] and lista == []:
            lista.append(11)
            #lista.remove(lista['A'])
            continue
        if dealer == 'A' or dealer == 'J' or dealer == 'Q' or dealer == 'K':
            lista.append(10)
            #lista.remove(lista['A'], lista['J'], lista['Q'], ista['K'])
            continue
     
    return lista


#print(embaralhar(cartas))

jogadores = int(input('Informe a quantidade de jogadores: \t'))

vira_carta = (f"A sua carta virada foi:{embaralhar(cartas)} \t")
somar_cartas = (f"A sua mão é de: {embaralhar(sum(cartas))} pontos\t")
print('Deseja continuar?\t'*2)
print('SIM\t NÃO\t')                             