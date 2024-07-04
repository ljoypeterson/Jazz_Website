#making a function sum
def sum(a, b):
    return (a + b)

while True:  

    a = int(input('Enter 1st number: '))
    b = int(input('Enter 2nd number: '))

    print(f'Sum of {a} and {b} is {sum(a, b)}')
