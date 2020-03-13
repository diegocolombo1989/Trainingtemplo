
# import random


# cartas  = ["A", "2", "3", "4","5", "6","7", "8", "9","10","J", "Q","K"]
# def embaralhar(cartas):
#     lista = []
   
#     for e in range(len(cartas)):
#         r = random.choice(cartas)
#         print(r)
#         if lista == [] and r == 'A':
#             lista.append(11)
#             continue
#         if r == 'A' or r == 'J' or r == 'Q' or r == 'K':
#             lista.append(10)

#         else: lista.append(r)
#         cartas.remove(r)

#     return lista


# dealer = print(embaralhar(cartas))


import random

cartas = ["A", "2", "3", "4","5", "6","7", "8", "9","10","J","Q","K"]
print('\t-'*20)
print('\n')
cab ='''                                                                   BLACKJACK                                        \n'''    
print(cab)
print('\t-'*20)
print('\n'*2)

jogadores = int(input('\nInforme a quantidade de jogadores: '))

cartas = ["A", "2", "3", "4","5", "6","7", "8", "9","10","J", "Q","K"]
dealer = cartas

def embaralhar(dealer):
    lista_embaralha = []
    random.choice = dealer
    lista_embaralha.append(dealer)
    return lista_embaralha

print(embaralhar(dealer))
