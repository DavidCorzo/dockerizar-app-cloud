import sys

rows = int(sys.argv[1])

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n", end="")

print("Terminated.")