package basic_test

import (
	"testing"

	"github.com/riaz/EffectiveCode/GoLang/basic"
	"github.com/stretchr/testify/assert"
)

func Test_WordCount(t *testing.T) {
	sentence := "The sky is blue and Oceans are blue"
	want := map[string]int{"The": 1, "sky": 1, "is": 1, "blue": 2, "Oceans": 1, "are": 1, "and": 1}
	got := basic.WordCount(sentence)
	assert.Equal(t, want, got)

}
