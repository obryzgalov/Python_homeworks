my_list = []  # Empty list
while True:  # cycle 4 filling the list w/different values
    print("Enter element (Q for exit): ")
    elm = input()
    if elm == "Q":
        break
    else:
        my_list.append(elm)

print(my_list)
