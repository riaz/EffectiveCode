package basic_test

import (
	"testing"

	"github.com/riaz/EffectiveCode/GoLang/basic"
	"github.com/stretchr/testify/assert"
)

func Test_Fibonacci(t *testing.T) {
	f := basic.Fibonacci()

	// we will now read the result in the array and save
	got := []int{}

	for i := 0; i < 3; i++ {
		got = append(got, f())
	}

	want := []int{0, 1, 1}

	assert.Equal(t, want, got)
}
