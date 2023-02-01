print("Sejam Bem Vindos ao Python Quiz!")

playing = input("Você quer jogar? ")

if playing.lower() != "sim":
    quit()

print("Beleza! Bora jogar!")
score = 0

answer = input("Qual o nome da linguagem de programação muito utilizada no Front-end? ")
if answer.lower() == "javascript":
    print('Acertou!')
    score += 1
else:
    print("Errou!")

answer = input("Quem é mais rápido e dá menos gargalo? HD ou SSD? ")
if answer.lower() == "ssd":
    print('Acertou!')
    score += 1
else:
    print("Errou!")

answer = input("Qual o significado da sigla RAM? ")
if answer.lower() == "random acess memory":
    print('Acertou!')
    score += 1
else:
    print("Errou!")

answer = input("Em qual Hardware é feito o armazenamento da memória primária? ")
if answer.lower() == "ram":
    print('Acertou!')
    score += 1
else:
    print("Errou!")

answer = input("Em qual Hardware é feito o armazenamento da memória secundária? ")
if answer.lower() == "hd":
    print('Acertou!')
    score += 1
else:
    print("Errou!")

print("Você acertou " + str(score) + " questões!")
print("Você acertou " + str((score / 5) * 100) + "%.")