#operators...

print("Arthmatic operators: " )

a = 10
b = 20

print(f" Addition: {a + b}, Subtraction:  {a- b}, MUltiplication: {a * b}, Modueles:  {a/ b}, Division: {a % b}")

print("Comparsion operators: ")
print(f"Greaterthan: {a > b}, Less than: {a < b}, Equal: {a == b}, Not equal: {a != b}")


print("Assigment operators: ")
a += b
print(f"Add: {a}")

a-= b
print(f" Sub: {a}")

a *= b
print(f"Multiply: {a}")

a/=b
print(f"Modules: {a}")


print("logical operators: ")

print(f"And: {a < b and b > a}, OR: {a > b or b > a}, Not: {not(a < b)}")


print("Membership operators: ")

Bikes = ["honda","scooty","splendor"]

print(f"Bikes: {"honda" not in Bikes}, {"Bullet" not in Bikes}")


