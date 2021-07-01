import math
import random


text = ""
x, total, l = 0, 0, 1

while l > 1e-9:
    total += 1

    x += (1 - (random.uniform(0, 1)**2))**.5

    p = 4 * x / total
    l = abs(math.pi - p)
    a = 100 - (abs(math.pi - p) * 100) / math.pi

    if not total % 100000:
        print(f"Iteration: {total}\tEstimate: {round(p, 8)}\tLoss: {l}\tAccuracy: {round(a, 8)}")

print(f"Iteration: {total}\tEstimate: {round(p, 8)}\tLoss: {l}\tAccuracy: {round(a, 8)}")
