file = open("Hi.txt" , "r")
print(" Reading First Line ")
print(file.readline())
file.close()

file = open("Hi.txt" , "r")
print(" Reading Multiple Line ")
print(file.readline( ) )
print(file.readline( ) )
print(file.readline( ) )
file.close()

file = open("Hi.txt" , "r")
print("Looping Through lines ")
for line in file:
    print(line)
file.close()