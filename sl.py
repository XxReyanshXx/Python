
file = open("codingal.txt", "w")

file.write("My Slam Book\n")

name = input("Enter your friend's name: ")
nickname = input("Enter their nickname: ")
colour = input("Enter their favourite colour: ")
food = input("Enter their favourite food: ")
hobby = input("Enter their hobby: ")

file.write("Name: " + name + "\n")
file.write("Nickname: " + nickname + "\n")
file.write("Favourite Colour: " + colour + "\n")
file.write("Favourite Food: " + food + "\n")
file.write("Hobby: " + hobby + "\n")

file.close()
file = open("codingal.txt", "r")
print(file.read())
file.close()
