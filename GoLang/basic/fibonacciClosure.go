package basic

// fibonacci is a function that returns
// a function that returns an int.
func Fibonacci() func() int {
	a := 0
	b := 1
	return func() int {
		tmp := a
		b, a = a+b, b
		return tmp
	}
}
