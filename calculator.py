def add (p, q):
    return p+q

def suptract (p, q):
    return p-q

def multiply (p, q):
    return p*q

def divide (p, q):
    return p/q

print("please select an operater ")
print("a.add")
print("b.subtract")
print("c.multiply")
print("d.divide")
choice = input("please enter your choice(a / b/ c/ d):")

num_1 = int(input("please enter the first number"))
num_2 = int(input("please enter the second number"))

if choice == 'a':
    print(num_1, "+", num_2, "=" add(num_1, num_2))

elif choice == 'b':
    print(num_1, "-", num_2, "=" subtract(num_1, num_2))

elif choice == 'c':
    print(num_1, "*", num_2, "=" multiply(num_1, num_2))

elif choice == 'd':
    print(num_1, "/", num_2, "=" divide(num_1, num_2))