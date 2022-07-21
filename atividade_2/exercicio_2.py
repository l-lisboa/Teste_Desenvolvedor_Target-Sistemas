n = int(input("Por favor, entre com o número da sequência de Fibonacci: "))
na = 0
nd = 1
soma = 1

if n == 0:
    print("Pertence a sequência de Fibonacci")

else:
    while soma < n:
        soma = nd + na
        na = nd
        nd = soma

    else:
        if soma == n:
            print("Pertence a sequência de Fibonacci")

        else:
            print("Não pertence a sequência de Fibonacci")