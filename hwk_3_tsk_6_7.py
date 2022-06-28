def int_func(wrd):
    return wrd.capitalize()


ent_list = input('enter string w/split: ').split()
for i, wrd in enumerate(ent_list):
    ent_list[i] = int_func(wrd)
print(' '.join(ent_list))
