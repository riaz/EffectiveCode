package basic_test

import (
	"testing"

	"github.com/riaz/EffectiveCode/GoLang/basic"
	"github.com/stretchr/testify/assert"
)

func Test_Abs(t *testing.T) {
	v := basic.Vertex{3, 4}
	assert.Equal(t, v.Abs(), 5.0)
}
