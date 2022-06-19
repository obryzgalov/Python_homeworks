# Задание 2. Поменять местами элементы списка последовательно, вdод через input

new_list = list(input("Enter elements: ").split())
print("Original list is: ", (new_list))
for i in range(1, len(new_list), 2):
    x = new_list[i - 1]
    new_list[i - 1] = new_list[i]
    new_list[i] = x
print("New list is: ", (new_list))
