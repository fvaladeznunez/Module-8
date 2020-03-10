# Fernando Valadez-Nunez
# 03/05/2020

# Write a function that takes two inputs from a user and prints whether the sum
# is greater than 10, less than 10, or equal to 10

x= int(input("What is your first number?"))
y= int(input("What is the second number?"))
x+y>10 or x+y<10 or x+y==10
def sum1(x,y):
    z= x+y
    if x+y>10:
        print(z, 'Is greater than 10')
    if x+y<10:
        print(z, 'Is less than 10')
    if x+y==10:
        print(z, 'Is equal to 10')
sum1(x,y)
