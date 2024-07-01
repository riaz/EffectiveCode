package basic

import (
	"fmt"
	"time"
)

/*
	golang has the in-built interface called error with the function Error
	so we can create a custom type and implement Error to return as `error`
*/

type MyError struct {
	When time.Time
	What string
}

func (e *MyError) Error() string {
	return fmt.Sprintf("at %v, %s", e.When, e.What)
}

// here we use a Error Type implementing Error
func Run() error {
	return &MyError{
		time.Now(),
		"it didn't work",
	}
}
