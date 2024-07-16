
my_map = {}


for i in range(my_arr):
    if i in my_map:
        my_map[i] = my_map.get(i) + 1
    else:
        my_map[i] = 1