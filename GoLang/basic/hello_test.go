package basic_test

import (
	"testing"

	"github.com/riaz/EffectiveCode/GoLang/basic"
	"github.com/stretchr/testify/assert"
)

func TestSayHello_OK(t *testing.T) {
	t.Parallel()
	t.Helper()

	want := "Hello World!"
	got := basic.SayHello(want)

	if got != want {
		t.Errorf("got %q want %q", got, want)
	}
}

func TestSayHello_NotOK(t *testing.T) {
	t.Parallel()
	t.Helper()

	want := "Hello World!"
	got := basic.SayHello("World!")

	if got == want {
		t.Errorf("got %q want %q", got, want)
	}
}

func TestSayHello_Empty(t *testing.T) {
	t.Parallel()
	t.Helper()

	want := ""
	got := basic.SayHello("")

	if got != want {
		t.Errorf("got %q want %q", got, want)
	}
}

// Running subtests
func TestSayHello_SubTests(t *testing.T) {
	t.Run("hello is echoed back", func(t *testing.T) {
		got := basic.SayHello("hello")
		want := "hello"
		assert.Equal(t, got, want)
	})

	t.Run("hello is not empty", func(t *testing.T) {
		got := basic.SayHello("hello")
		want := ""
		assert.NotEqual(t, got, want)
		assert.Empty(t, want)
	})

}
