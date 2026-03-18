operation = input("Choose the operation you wanna do... + ,- ,* ,/ ")
num_1 = int(input("Choose a number:  "))
num_2 = int(input("Another one:  "))
 
if operation == "+":
     print(num_1 + num_2)
elif operation == "-":
     print(num_1 - num_2)
elif operation == "*":
     print(num_1 * num_2)
elif operation == "/":
     print(num_1 / num_2)
else:
     print("Invalid Operation")