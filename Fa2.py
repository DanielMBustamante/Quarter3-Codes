temperatures = [
    [32, 33, 31, 32, 34, 33, 32],
    [22, 23, 21, 22, 24, 23, 22]
]
print(temperatures[0][2])

temperatures[1][4] = 25

average_manila = sum(temperatures[0]) / len(temperatures[0])
print(average_manila)
