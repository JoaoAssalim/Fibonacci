length = input('Enter a length to fibonacci: ')
if length.isdigit():
    atual, proximo = 0, 1
    for i in range(int(length)):
        atual, proximo = atual+proximo, atual
        print(proximo)
