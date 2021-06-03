nos = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }
primenos = { 1, 2, 3, 5, 7 }
squarenos = {1, 4, 9}

# Check for union
# print(primenos | Squarenos)

result1 = primenos.union(squarenos)
print(result1)

#Check for intersection
print(squarenos & primenos)
result2 = squarenos.intersection(primenos)
print(result2)

# Difference
print(nos - squarenos)


# Iterables - where we can loop through
