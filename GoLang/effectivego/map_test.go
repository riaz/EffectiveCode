package effectivego_test

import (
	"testing"

	"github.com/riaz/EffectiveCode/GoLang/effectivego"
	"github.com/stretchr/testify/assert"
)

func TestHelloWorld(t *testing.T) {
	msg := "Riaz Munshi"
	expected := "Hello, " + msg
	got := effectivego.HelloWorld(msg)

	assert.Equal(t, expected, got)
}
