package basic

import "os"

// Prints the command line arguments passed to the program

func EchoCli() string {
	var s string
	sep := ""
	for i := 1; i < len(os.Args); i++ {
		s += sep + os.Args[i]
		sep = " "
	}
	return s
}
