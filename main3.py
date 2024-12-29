f1 = open("Hanzla.txt" , 'r')
f2 = open("Hi.txt" , 'w')

for line in f1.readlines():
    if not (line.startswith("Coding")):
        print(line)
        
    f2.write(line)

f1.close()
f2.close()