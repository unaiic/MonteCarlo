package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())

	total, c := 0, 0
	sum, estimate := 0., 0.

	for fmt.Sprintf("%.9f", estimate) != "2.718281828" {
		total++

		sum = 0
		for sum <= 1. {
			sum += rand.Float64()
			c++
		}

		estimate = float64(c) / float64(total)

		if (total % 100000) == 0 {
			fmt.Printf("Iteration: %d\tEstimate: %.9f\n", total, estimate)
		}
	}
	fmt.Printf("Iteration: %d\tEstimate: %.9f\n", total, estimate)

	fmt.Scanln()
}
