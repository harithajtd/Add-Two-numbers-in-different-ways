#1.To add two numbers without taking user input

n1=24
n2=24.5
sum=n1+n2
print('The sum of {0} and {1} is {2}'.format(n1,n2,sum))

#_____________________________________________________________________


#2. Adding two numbers taking USER INPUT

number1=input('Enter first number:')
number2=input('Enter second number:')

sum=float(number1)+float(number2)

print('The sum of {0} and {1} is {2}'.format(number1,number2,sum))


#_____________________________________________________________________


#3. Adding two numbers using a function

def addTwoNums(n1,n2):
    return n1+n2

a=float(input('Enter first number:'))
b=float(input('Enter second number:'))

#calling Function
c=addTwoNums(a,b)
print(f'Sum of {a} and {b} is {c:.2f}')

