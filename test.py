import numpy as np

list_num = np.random.randint(0, 100, size=10).tolist()
with open('/home/tn/git/tests/test_git_action/output.txt', 'w') as f:
    for num in list_num:
        f.write(f"{num}\n")