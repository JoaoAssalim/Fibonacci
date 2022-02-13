length = input('Enter a length to fibonacci: ')
if length.isdigit():
    fibonacci = [0, 1]
    
    counter = 2 # counter receives 2 because there are 2 numbers in fibonacci list
    while counter <= int(length):
        counter += 1
        next_number = fibonacci[-2] + fibonacci[-1]
        fibonacci.append(next_number)

    print(fibonacci)
