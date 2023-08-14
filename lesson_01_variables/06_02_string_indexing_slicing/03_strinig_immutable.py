name = "Ohad Zouzout"
print(name)

print(name[0:3] + "y")
print(name + "y")
print(name)

name = "Alex"
print(name)

mixed_name = "Ohad Alex"
print(mixed_name)
print(id(mixed_name))
mixed_name = mixed_name[:-1]
print(mixed_name)
mixed_name += "l"
print(mixed_name)
print(id(mixed_name))