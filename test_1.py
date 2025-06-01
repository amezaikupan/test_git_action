# test.py
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
filename = sys.argv[3]  # e.g., output_a_b.txt

with open(filename, 'w') as f:
    for num in range(a, b):
        f.write(f"{num}\n")

print(f"Written numbers from {a} to {b-1} into {filename}")
