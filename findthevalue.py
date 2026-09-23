def find_value(dictionary, key):
    return dictionary.get(key)

data = {
    "name": "Reyansh",
    "age": 13,
    "city": "Mumbai"
}

key = input("Enter the key: ")

value = find_value(data, key)

if value is not None:
    print("Value =", value)
else:
    print("Key not found")