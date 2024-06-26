package basic_test

import (
	"testing"

	"github.com/riaz/EffectiveCode/GoLang/basic"
	"github.com/stretchr/testify/assert"
)

func Test_Interface2(t *testing.T) {
	msg := "hello"
	var i basic.I = basic.T{S: msg, Q: msg}
	assert.Equal(t, msg, i.Echo())
}
