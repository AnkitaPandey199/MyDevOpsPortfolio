x=input("Enter the 1st Number:")
y=input("Enter the 2nd Number:")
z=int(x)+int(y)
print("The sum is:", z)

ch = input("Do you want to continue? (y/n): ")
print(ch[0])
result = eval(input('enter an expression:'))
print (result)


import sys
a= int(sys.argv[1])
b= int(sys.argv[2])
z=a+b
print("The sum od a and b:", z)