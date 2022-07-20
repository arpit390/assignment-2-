'''
#ANSWER 1 palindrome program in python¨
s = 'madam'
s1 = s[::-1]
print (s1)
if (s == s1):
    print('palindrome')
else:
    print('no palindrome')

#palindrome program for integer in python¨
s = '1441'
s1 = s[::-1]
print (s1)
if (s == s1):
    print('palindrome')
else:
    print('no palindrome')

#to check number is palendrome or not 
num = int(input("enter the value:"))
temp = num
rev = 0
while(num > 0):
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if (temp == rev):
    print(" palendrome")
else:
    print("not palendrome")


#ANSWER 2 factorial program in python
num = int(input('enter the number:'))
factorial = 1
if (num < 0):
    print('factorial doesnt exit')
elif (num == 0):
    print('the factorial of zero is one')
else:
    for i in range(1 , num+1):
        factorial = factorial * i
    print('factorial of' ,num, 'is' , factorial) 

#ANSWER 3 fibonacci series program 
nterms = int(input('enter the terms the user want to print:'))
count = 0
n1 = 0
n2 = 1
if (nterms<0):
    print('you have to put the positive value sorry!')
elif(nterms==1):
    print(n1)
else:
    print('the fibonacci series of sequence is')
    while(nterms>count):
       print(n1)
       nth =n1 + n2
       n1 = n2
       n2 = nth
       count += 1

# ANSWER 4 CALCULATOR BY USING PYTHON PROGRAM 
def add( p ,q ):
    return (p+q)
def subtract( p,q ):
    return (p-q)
def multiply (p,q):
    return (p*q)
def divide (p,q):
    return (p/q) 
print ('select the opertaion:')
print ('a.addition')
print('b.subtraction')
print('c.multiply')
print('d.division')

choice = input('enter the operation( a,b,c,d ):')
num1 = int(input('enter the first number:'))
num2 = int(input('enter the second number:'))

if(choice=='a'):
    print(num1,'+',num2,'=',add(num1,num2))
if(choice=='b'):
    print(num2,'-',num2,'=',subtract(num1,num2))
if(choice=='c'):
    print(num1,'*',num2,'=',multiply(num1,num2))
if(choice=='d'):
    print(num1,'/',num2,'=',divide(num1,num2))

#ANSWER 6 pattern in python
n = int(input('select the number of rows:'))
for i in range (0,n):
    for j in range (0,i+1):
        print("*", end= '')
    print("")    

#ANSWER 10 program to reverse a list 
l1= [10, 20 , 30 , 40]
l2 = l1[::-1]
print(l2)

#ANSWER 9 program to find area in python
# for rectangle
a= int(input('enter the length of rectangle'))
b = int(input('enter the breadth of rectangle'))
area = a*b
print('area of rectangle is:', area, 'msq') 
# for triangle
a = float(input('enter the base of triangle: '))
b = float(input('enter the height of triangle: '))
area = 1/2*a*b
print('the area of triangle is:',area)

#ANSWER 8 prime number program in python
num = int(input('enter the number ='))
if(num>1):
    for i in range(2,num):
        if(num % i) == 0:
            print(num,'is not a prime number')
            break
        else:
            print(num,'is a prime number')
else:
    print(num, 'is not a prime number')

#ANSWER 11 FIND SUM OF ALL ELEMENTS IN LIST

list = [10,34,54,67,12,4]
total = sum(list)
print('the sum of elements in list is:',total)

#ANSWER 12 FIND AVERAGE,MAX,MIN OF LIST ELEMENTS
#AVERAGE
list = [10,20,30,40,50]
total = sum(list)
average = total / len(list)
print('the average of elements in list are:',average)
#MAXIMUM
list = [10,304,35,87,65,82]
print( 'the largest number in list is:', max(list))'''
#MINIMUM
list = [23,5,6,68,4,35,65]
print('the smallest number in the list is:',min(list))
