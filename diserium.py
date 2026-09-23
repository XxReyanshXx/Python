def disarium(num):
    digits = str(num)
    total = 0

    for i in range(len(digits)):
        total += int(digits[i]) ** (i + 1)

    if total == num:
        return True
    else:
        return False


d = int(input("Enter a number: "))

if disarium(d):
    print("It is a Disarium number")
else:
    print("It is not a Disarium number")