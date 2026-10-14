
file = open("codingal.txt", "r")

print(file.read(10))

file.close()

file = open("codingal.txt", "r")
lines = file.readlines()
file.close()

new_file = open("clean_codingal.txt", "w")

for line in lines:
    if line.startswith("IMPORTANT") or line.startswith("TODO"):
        new_file.write(line)

new_file.close()

print("Clean notes file created successfully!")
