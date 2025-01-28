print (3 + 2)

#F-strings
print(f"3 + 2 = {3 + 2}")
print(f"5 - 1 = {5 - 1}")
print(f"3 * 4 = {3 * 4}")
print(f"10 / 5 = {10 / 5}")
print(f"35 % 3 = {35 % 3}")
print(f"2 ** 4 = {2 ** 4}")

#Comparison operators
print(5 > 1)
print(f"5 == 1: {5 == 1}")
print(f"5 != 1: {5 != 1}")
print(f"5 > 1: {5 > 1}")
print(f"5 >= 1: {5 >= 1}")
print(f"5 < 1: {5 < 1}")
print(f"5 <= 1: {5 <= 1}")

#Variable assignment
my_name = "John Brooksby"
print(my_name)

#Input
# name = input("What's Your Name: ")
# print(f'Hello {name*10}')
# print(f'Hello {name}'*10)
# num1 = input("Enter A Number: ")
# num2 = input("Enter Another Number: ")
# print(f'{num1} + {num2} = {int(num1)+int(num2)}')

#IF / ELIF / ELSE
x = input("Guess a number ")
print (x)
if int(x) == 41:
    print("X Does in fact equal 41!")
elif int(x) > 41:
    print("Too high!")
else:
    print("Too low")