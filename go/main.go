package main

import (
	"fmt"
	"strconv"
)

func main() {
	
	x := "1"
	y, e := strconv.Atoi(x)
	
	fmt.Println(y)
	fmt.Println(e)
}
