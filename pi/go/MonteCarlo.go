package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())

	x, total, p, l, a := 0., 0, 0., 1., 0.

	for l > 1e-9 {
		total++

		x += math.Pow(1-math.Pow(rand.Float64(), 2), .5)

		p = 4 * float64(x) / float64(total)
		l = math.Abs(math.Pi - p)
		a = 100 - (math.Abs(math.Pi-p)*100)/math.Pi

		if total%100000 == 0 {
			fmt.Printf("Iteration: %d\tEstimate: %.8f\tLoss: %e\tAccuracy: %.8f\n", total, p, l, a)
		}
	}
	fmt.Printf("Iteration: %d\tEstimate: %.8f\tLoss: %e\tAccuracy: %.8f\n", total, p, l, a)

	fmt.Scanln()
}
