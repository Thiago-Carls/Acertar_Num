import random

min1 = 1
max1 = 100
resposta = random.randint(min1, max1)

chutes = 0
is_running = True

print(f"escolha um numero entre {min1} e {max1}")
while is_running:
    chute = input("chute um numero: ")
    if chute.isdigit():
        chute = int(chute)
        chutes += 1
        if chute < min1 or chute > max1:
            print("fora dos limites")
        elif chute < resposta:
            print("maior")
        elif chute > resposta:
            print("menor")
        elif chute == resposta:
            print("correto")
            print(f"numero de jogadas {chutes}")
            break
    else:
        print("chute invalido")