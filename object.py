def circle(radius):
    area = 3.14 * radius * radius
    perimeter = 2 * 3.14 * radius

    print("Area =", area)
    print("Perimeter =", perimeter)

r = float(input("Enter the radius: "))

circle(r)