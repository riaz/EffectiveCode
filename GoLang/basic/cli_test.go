package basic_test

import (
	"os"
	"strings"
	"testing"

	"github.com/riaz/EffectiveCode/GoLang/basic"
	"github.com/stretchr/testify/assert"
)

func TestHelloCli(t *testing.T) {
	// Note: when running  a test, the test environment introduces lot of args, and we just
	// follow the patter to eliminate the payload which will be common to all calls - to test it effectively

	t.Parallel()

	t.Run("No arguments passed", func(t *testing.T) {
		rawGot := basic.EchoCli()
		idxOffset := strings.LastIndex(rawGot, "$")
		got := strings.TrimSpace(rawGot[idxOffset+1:])
		want := ""

		assert.Equal(t, want, got)
	})

	t.Run("With one argument", func(t *testing.T) {
		want := "Hello"

		os.Args = append(os.Args, want)

		rawGot := basic.EchoCli()
		idxOffset := strings.LastIndex(rawGot, "$")
		got := strings.TrimSpace(rawGot[idxOffset+1:])

		assert.Equal(t, want, got)

		os.Args = os.Args[:len(os.Args)-1] // clean up
	})

	t.Run("With three argument", func(t *testing.T) {
		wantArgs := []string{"Hello", "World", "Riaz"}

		os.Args = append(os.Args, wantArgs...)

		rawGot := basic.EchoCli()
		idxOffset := strings.LastIndex(rawGot, "$")
		got := strings.TrimSpace(rawGot[idxOffset+1:])

		want := strings.Join(wantArgs, " ")
		assert.Equal(t, want, got)

		os.Args = os.Args[:len(os.Args)-len(wantArgs)]
	})

	t.Run("With many argument", func(t *testing.T) {
		wantArgs := []string{"Hello", "World", "Riaz", "This", "Is", "A", "Random", "String"}

		os.Args = append(os.Args, wantArgs...)

		rawGot := basic.EchoCli()
		idxOffset := strings.LastIndex(rawGot, "$")
		got := strings.TrimSpace(rawGot[idxOffset+1:])

		want := strings.Join(wantArgs, " ")
		assert.Equal(t, want, got)

		os.Args = os.Args[:len(os.Args)-len(wantArgs)]
	})
}
