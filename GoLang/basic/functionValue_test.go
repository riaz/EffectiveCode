package basic_test

import (
	"math"
	"testing"

	"github.com/riaz/EffectiveCode/GoLang/basic"
	"github.com/stretchr/testify/assert"
)

func Test_closure(t *testing.T) {
	// in go a function can be assigned as a value
	squareFn := func(x, y float64) float64 {
		return math.Sqrt(x*x + y*y)
	}

	want := 5.0
	got := basic.Compute(squareFn)

	assert.Equal(t, want, got)
}
