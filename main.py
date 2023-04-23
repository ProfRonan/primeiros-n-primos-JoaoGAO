n = int(input("Digite um número inteiro: "))

def é_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

count = 0
num = 2

while count < n:
    if é_primo(num):
        print(num)
        count += 1
    num += 1