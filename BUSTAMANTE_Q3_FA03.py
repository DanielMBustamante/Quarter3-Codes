temperatures = [
    [32, 33, 31, 35, 34, 33, 32],
    [22, 23, 21, 22, 24, 23, 22]
]

cities = ["Manila", "Baguio"]

for i in range(len(temperatures)):
    total = sum(temperatures[i])
    average = total / len(temperatures[i])
    minimum = min(temperatures[i])
    maximum = max(temperatures[i])

    print(
        cities[i],
        "- Total:", total,
        "| Average:", average,
        "| Min:", minimum,
        "| Max:", maximum
    )
