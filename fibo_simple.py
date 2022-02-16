length = input('Enter a length to fibonacci: ')
if length.isdigit():
    prox, anterior = 0, 1
    for i in range(int(length)):
        prox, anterior = prox+anterior, prox
        print(soma)
