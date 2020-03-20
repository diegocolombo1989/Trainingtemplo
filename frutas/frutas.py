import random
import time
cab1 = '\t-'*20 
cab2 = '\t-'*20
print(cab1, '\n\t                                                           JOGO ADIVINHA FRUTAS\n', cab2)

frutas = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']
sorteio = random.choice(frutas)

print("\nTemos uma lista de frutas fresquinhas para você sortear, caso acerte a fruta sorteada digitando uma letra que contenha nela, ela será sua.")
print('\nO Jogo começa em 3...2..1.')
time.sleep(3)
print(f"\nA fruta sorteada foi a de número:\t{frutas.index(sorteio)}")

jogador = (str(input("\nInsira a letra que você acha que a fruta contém: \t")))

if jogador in sorteio[0:]:
    print(f"\nParabéns, a letra digitada existe na fruta sorteada que foi -> {sorteio}")
else:
    print(f"\nA letra digitada não existe na fruta sorteada que foi -> {sorteio}")