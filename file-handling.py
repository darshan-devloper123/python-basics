# file = open("student.txt","w")
# file.write("Name: Darshan\n")
# file.write("Age: 21\n")
# file.write("Course: BCA\n")
# file.close()


# file = open("student.txt","r")

# data = file.read()

# print(data)

# file.close()

file = None

try:

    file = open("employess.txt", "r")
    file.write("\nSharath")

except Exception as e:
    print(f"Eror: {e}")

finally:
    if file:
        file.close()
        print("file closed")


students = ["darshan","virat","rohit"]

with open("class.txt2","w") as file:
    for student in students:
         file.write(f"{student}\n")
        
        
with open("class.txt2","r") as file:
    for line in file:
        print("Student: ", line.strip())





file = open("friends.txt","w")
file.write(f"{"Arjun"}\n")
file.write(f"{"Darshan"}\n")
file.close()


name = input("Enter name to search: ")
file = open("friends.txt","r")

found = False

for line in file:
    if name == line.strip():
        found = True
        break
file.close()

if found:
    print("Found..")
else:
    print("Not found..")

name = input("Enter a name: ")
marks = int(input("Enter a marks: "))


file = open("marks2.txt","a")
file.write(f"{name} - {marks}\n")
file.close()

print("saved succcsfully")