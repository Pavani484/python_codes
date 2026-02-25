print("hello pavani")
a=10
b=20
print(a+b)
#.............
class Calculator:
    def sum(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mult(self, a, b):
        return a * b
    def div(self, a, b):
        return a / b
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
o = int(input("Enter option: "))
c = Calculator()
a, b = map(int, input("Enter two numbers: ").split())
if o == 1:
    print("Addition:", c.sum(a, b))
elif o == 2:
    print("Subtraction:", c.sub(a, b))
elif o == 3:
    print("Multiplication:", c.mult(a, b))
elif o == 4:
    print("Division:", c.div(a, b))
else:
    print("Invalid option")