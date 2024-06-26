package basic

type I interface {
	Echo() string
}

type T struct {
	S string
	Q string
}

// just echo the value in the receiver type
func (t T) Echo() string {
	return t.S
}
