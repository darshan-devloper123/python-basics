#while loop

i = 1
while i <= 5:
    print(i)
    i += 1


#decrement while loop
print("decrement loop")
i = 100
while i >= 1:
    print(i)
    i -= 1

#odd numbers
print("ODD numbers:")
d = 1
while d <= 10:
    print(d)
    d += 2



#Even Numbers
print("Even numbers: ")
d = 2
while d <= 50:
    print(d)
    d += 2


#while break statement
print("break statement")
Ball = 1
while Ball <= 11:
    print(Ball)
    if Ball == 10:
        break
    Ball += 1


#while continue statement
print("continue statament")
batters = 0
while batters <= 11:
    if batters == 4:
        batters += 1
        continue
    print(f" Form Batters {batters}")
    batters += 1




#for loops

print("for looping statments: ")
name = "Darshan"
for letter in name:
    print(letter)


#range functions
print("Range function: " )

print("start function:")    #strart
i = 0
for i in range(5):
    print(i)

print("stop function")

i = 0                    #stop
for i in range(5,80):
    print(i)


print("step function: ")  

i = 0                      #step
for i in range(5,50,3):
    print(i)



print("Enumerate for loop: ")

name = "virat","rahul","rohit"
for index, name in enumerate(name):
    print(index,name)


print("for break statement: ")

names = ["virat","arjun","darshan"]
for name in names:
    if name == "virat":
        print(f"virat is no1 batter {names}")
        break
    print(names)



print("Continue statement: ")

names = "viart","kishan","rahul"
for name in names:
    if name == "kishan":
        continue

    print(names)