# Adalysa Rosales
# Lab5
# 4/13/21

def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n - 1)

num = int(input('Enter a positive integer: '))
if num<=0:
    print('You cannot do that')
else:
    print('The sum is',sum(num))
