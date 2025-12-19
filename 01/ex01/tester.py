from array2D import slice_me

family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

# added testcases
# tc 1
print("tc 1")
family = []
print(slice_me(family, 0, 2))

# tc 2
print("tc 2")
family = [1, 2, 3]
print(slice_me(family, 0, 2))

# tc 3
print("tc 3")
family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]
print(slice_me(family, -2, 4))
