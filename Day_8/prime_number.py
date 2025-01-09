def prime_number(number):
    is_prime = True
    for i in range(2, round(number/2)):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f'{number} is a Prime Number')
    else:
        print(f'{number} is a not Prime Number')

n = int(input('Check this number: '))
prime_number(number=n)