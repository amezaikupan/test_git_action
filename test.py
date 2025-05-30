list_num = [1, 2, 3, 4, 5]
with open('/home/tn/git/tests/test_git_action/output.txt', 'w') as f:
    for num in list_num:
        f.write(f"{num}\n")