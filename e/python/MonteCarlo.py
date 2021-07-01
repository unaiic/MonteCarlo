import math
import random
import matplotlib.pyplot as plt


total, c = 0, 0
estimate = 0.
ypoints = []

while round(estimate, 9) != "2.718281828":

    total += 1
    if total == 101:
        plt.savefig("foo.png")
        break
    sum_ = 0
    while sum_ <= 1.:
        sum_ += random.uniform(0, 1)
        c += 1

    estimate = c / total

    if not total % 100000:
        print(f"Iteration: {total}\tEstimate: {round(estimate, 9)}")

    if total < 101:
        ypoints.append(estimate - math.e)

        plt.plot(ypoints)
        plt.grid(True)

print(f"Iteration: {total}\tEstimate: {round(estimate, 9)}")
