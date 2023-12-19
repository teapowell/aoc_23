import numpy as np

array = np.array([[".", ".", "."], [".", ".", "*"], [".", ".", "."]])
print(np.argwhere(array == "*"))

string = ["...", ".**", "..."]
print(np.argwhere(np.array([list(x) for x in string]) == "*"))

print(list("..."))

print(str("?" * 5))

print([2 4] - [1 1])
