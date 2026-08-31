num = int(input("Enter a num: "))

try:
    print(10/num)

except ZeroDivisionError:
    print("Cannot divide by zero")

except Exception as e:
    print(f"Eror: {e}")


finally:
    print("Program completed..")   


    

    print("catching division by zero")
try:
    a = int(input("Enter a num: "))
    result = 10/a
    print("result:", result)

except ZeroDivisionError:
    print("cannot divide by zero..")
 

print("Handling multiple Exceptions")
try:
    num =int(input("Enter a num: "))
    result = 10/num
    print("Result:", result)

except ZeroDivisionError:
    print("cannot divide by zero")

except ValueError:
    print("please enter valid number")


print("2nd example...")
age = input("Enter a number: ")

try:
    age = int(age)

    if age >= 0 and age <= 80:
        years = 80 - age
        print(f"you will be 80 years old in {years} years")

    else:
        print("please enter valid age between 0 and 100..")


except ValueError:
    print("Invalid input Please enter a valid number..")


print("second Example")
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))


try:
   print("Result", a/b)

except ZeroDivisionError:
   print("cannot divide by zero")

except ValueError:
   print("please enter valid number..")

finally:
   print("program ended")

print("3rd example..")
try:
    file = open("my file.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("file not found..")

finally:
    print("program ended..")
    
        
print("4th example...")       
a = int(input("a: "))
b = int(input("b: "))

try:
    print(a/b)

except Exception as e:
    print(f"Eror: {e}")
    b = int(input("b: "))
    print(a/b)


finally:
    print("program ended..")

print("5th example...")
try:
    boy = input("who do want to marry?")
    if boy.lower() != "darshan":
        raise Exception("you can only marry darshan select him..")
    
except Exception as e:
    print(f"Eror: {e}")

else:
    print("darshan is ready ")