package basic_test

import (
	"errors"
	"testing"

	"github.com/riaz/EffectiveCode/GoLang/basic"
	"github.com/stretchr/testify/assert"
)

func Test_Errors(t *testing.T) {
	if err := basic.Run(); err != nil {
		assert.Equal(t, true, errors.Is(err, &basic.MyError{}))
	}
}
