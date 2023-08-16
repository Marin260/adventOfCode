package main

import (
	"fmt"
	"os"
	"strings"
)

func check(e error){
	if e != nil{
		panic(e)
	}
}

func solver(fileData string, strategy map[string]int) int {
	var sum int
	splitData := strings.Split(fileData, "\n")

	for _, val := range splitData{
		sum += strategy[val]
	}
	
	return sum
}

func main() {
	strat1 := map[string]int {
		"A X": 4, // ROCK vs ROCK
		"A Y": 8, // ROCK vs PAPE
		"A Z": 3, // ROCK vs SCIZ
		"B X": 1, // PAPE vs ROCK
		"B Y": 5, // PAPE vs PAPE
		"B Z": 9, // PAPE vs SCIZ
		"C X": 7, // SCIZ vs ROCK
		"C Y": 2, // SCIZ vs PAPE
		"C Z": 6, // SCIZ vs SCIZ
	}

	strat2 := map[string]int {
		"A X": 3, // S Lose
		"B X": 1, // R Lose
		"C X": 2, // P Lose
		"A Y": 4, // R Draw
		"B Y": 5, // P Draw
		"C Y": 6, // S Draw
		"A Z": 8, // P Winn
		"B Z": 9, // S Winn
		"C Z": 7, // R Winn
	}
	
	pwd, _ := os.Getwd()
	fileData, fileError := os.ReadFile(pwd+ "/go/2022/day2/input.txt")
	check(fileError)
	
	partOneAnswer := solver(string(fileData), strat1)
	partTwoAnswer := solver(string(fileData), strat2)
	fmt.Print(partOneAnswer, "\n")
	fmt.Print(partTwoAnswer, "\n")
}