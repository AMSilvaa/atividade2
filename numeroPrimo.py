def eh_primo(numero):
    if numero <= 1:
        return False 

    for i in range(2, numero):
        if numero % i == 0:
            return False  

    return True 

for num in range(1, 101):
    if eh_primo(num):
        print(num, "é primo")
