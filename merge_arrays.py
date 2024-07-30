a = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
b = [6, 6, 7, 7, 8, 8, 9, 9, 10, 10]

def merge_arrays(array_a, array_b):
    # Set tar bort duplicates per automatik
    return sorted(set(array_a + array_b))

c = merge_arrays(a, b) # Det som kommer ut är en lista som är sorterad kombination på ovan listor
print(c)