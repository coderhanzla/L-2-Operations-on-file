file = open("Hi.txt" , "r")
print(file.read())
file.close()

file = open("Hi.txt" , "r")
print("\n Read ")
print(file.read(8))
file.close()

file = open("Hi.txt" , "a")
file.write("Hi I am Hanzla")
file.close()