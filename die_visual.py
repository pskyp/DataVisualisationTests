from die import Die

dice = Die()
results = []
for roll in range(100):
    result = dice.roll()
    results.append(result)
print(results)
