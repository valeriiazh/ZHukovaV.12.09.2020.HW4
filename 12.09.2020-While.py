def my_function(a, b, c):
    print(a, b, c)
    while a < b:
        a = (a + c)
        if a >= b:
            break
    print('The result is', a)


print('Please, enter three numbers below')
n1 = int(input('Number1: '))
n2 = int(input('Number2: '))
n3 = int(input('Number3: '))

my_function(n1, n2, n3)
