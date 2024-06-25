package duckdb_test

import (
	"testing"

	"github.com/riaz/EffectiveCode/GoLang/duckdb"
	"github.com/stretchr/testify/assert"
)

func Test_GetSampleData(t *testing.T) {
	got_id, got_name := duckdb.GetSampleData()
	assert.Equal(t, 42, got_id)
	assert.Equal(t, "Jason", got_name)
}
