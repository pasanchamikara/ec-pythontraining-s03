evennos = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }
primenos = { 2, 3, 5, 7 }
Squarenos = {1, 4, 9}

# Check for union
print(primenos | Squarenos)

result1 = primenos.union(Squarenos)

#Check for intersection
print(evennos & primenos)

# Difference
print(evennos - Squarenos)


# Iterables - where we can loop through