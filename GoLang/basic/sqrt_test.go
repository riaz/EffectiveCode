package basic_test

import (
	"math"
	"testing"

	"github.com/riaz/EffectiveCode/GoLang/basic"
	"github.com/stretchr/testify/assert"
)

func Test_Sqrt(t *testing.T) {
	var num float64 = 10
	want := math.Sqrt(num)
	got := basic.Sqrt(num)

	assert.Equalf(t, want, got, "Not equal")

}
