my_list = []

for i in range(1000000):
    file = open("passwords.txt", "w")
    my_list.append(file)
    file.close()