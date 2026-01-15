temperatures = [
    [32, 33, 31, 32, 34, 33, 32],
    [22, 23, 21, 22, 24, 23, 22]
]

print("Baguio temperature on Wednesday:", temperatures[1][2])
print("Manila temperatures...", temperatures[0])

print("Updating Manila temperature on Thursday to 35.")
temperatures[0][3] = 35

print("Manila updated temperatures:", temperatures[0])
