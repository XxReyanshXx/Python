
file = open("codingal.txt", "w")
file.write("Hello World!")
file.close()

file = open("codingal.txt", "r")
print(file.read())
file.close()

file = open("codingal.txt", "a")
file.write("\nWelcome to Codingal!")
file.close()

file = open("codingal.txt", "r")
print(file.read())
file.close()
