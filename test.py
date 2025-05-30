list_num = [1, 2, 3, 4, 5]
with open('output.txt', 'w') as f:
    for num in list_num:
        f.write(f"{num}\n")