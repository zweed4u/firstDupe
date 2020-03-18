package main

import (
	"fmt"
	"math/rand"
	"time"
)

func firstDupe(arr []int) int {
	occurredNumbers := make(map[int]bool) // hamfisted set implementation {val:hasOccurred}
	for _, number := range arr {
		if occurredNumbers[number] {
			return number
		}
		occurredNumbers[number] = true
	}
	return -1
}

func main() {
	// generate the array to be used
	numberOfElements := 10
	array := make([]int, numberOfElements)

	// populate the array with rand values
	rand.Seed(time.Now().UTC().UnixNano())
	for i := range array {
		array[i] = rand.Intn(numberOfElements) + 1 // [0, n) - conveniently constricts array element values to 1-N as in problem statement
	}

	fmt.Println(array)
	fmt.Println(firstDupe(array))
}
