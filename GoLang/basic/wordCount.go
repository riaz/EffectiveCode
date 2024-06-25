package basic

import (
	"strings"
)

func WordCount(s string) map[string]int {
	words := strings.Split(s, " ")

	freq := make(map[string]int)

	for _, word := range words {
		freq[word] += 1
	}
	return freq
}
