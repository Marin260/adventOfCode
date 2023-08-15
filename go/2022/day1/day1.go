package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func check(e error){
	if e != nil{
		panic(e)
	}
}

func minInt(maxCalList [3]int) int{
	var index int
	var min = maxCalList[0]
	for i, val := range maxCalList {
		if val < min {
			min =val
			index = i
		}
	}
	return index
}


func partOne(calInput string) int{
	calList := strings.Split(calInput, "\n")
	
	var max int
	var sum int

	for _, cal := range calList{
		val, e := strconv.Atoi(cal)
		if e != nil{
			if sum > max {
				max = sum
			}
			sum = 0
		}
		sum += val
	}
	return max
}

func partTwo(calInput string) int{
	calList := strings.Split(calInput, "\n")

	var max[3]int
	var sum int

	for _, cal := range calList{
		val, e := strconv.Atoi(cal)
		if e != nil {
			swapIndex := minInt(max)
			if max[swapIndex] < sum{
				max[swapIndex] = sum
			}
			sum = 0
		}
		sum += val
	}
	var maxCal int
	for _, val := range max{
		maxCal += val
	}
	return maxCal
}

func main(){
	pwd, _:= os.Getwd()
	dat, err := os.ReadFile(pwd+"/2022/day1/input.txt")
	check(err)
	
	var partOneAns = partOne(string(dat))
	var partTwoAns = partTwo(string(dat))
	fmt.Print(partOneAns, "\n")
	fmt.Print(partTwoAns, "\n")

}