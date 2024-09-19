def get_name():
    return input("Enter name (empty to quit): ")

name = get_name()

# set data structure
names = set()

# note: {} is an empty dict, not a set
# {'value', 'another'} is a set
# python is fun

while name != "":

    if name in names:
        print("Previously entered name")
    else:
        print("New name")
    names.add(name)
    name = get_name()

for name in names:
    print(name)