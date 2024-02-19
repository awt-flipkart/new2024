import sys

num1 = int(sys.argv[1])
operation = sys.argv[2]
num2 = int(sys.argv[3])
 
def addition(num1,num2):
    add = num1 + num2
    return add

def subtr(num1, num2):
    s = num1 - num2
    return s
 
def mul(num1, num2):
    m = num1 * num2
    return m


if operation == "add":
    output = addition(num1,num2)
    print(output)
    
    