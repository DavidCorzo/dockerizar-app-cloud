import sys
import pandas as pd

rows = int(sys.argv[1])

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n", end="")

print("Terminated.")

# pandas app
df = pd.DataFrame({'A': [1, 2], 'B': [10, 20]})

def square(x):
    return x * x


df1 = df.apply(square)

print(df)