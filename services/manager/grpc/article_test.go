package grpc

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

// Test_stringsToInterface は stringsToInterface が文字列のスライスをインタフェースに変換できているかテストする
func Test_stringsToInterface(t *testing.T) {
	s := []string{"a", "b", "c"}

	in := stringsToInterface(s)
	assert.Equal(t, []interface{}{"a", "b", "c"}, in)
}

// Test_interfaceToStrings は interfaceToStrings がインタフェースを文字列のスライスに変換できているかテストする
func Test_interfaceToStrings(t *testing.T) {
	in := []interface{}{"a", "b", "c"}

	s := interfaceToStrings(in)
	assert.Equal(t, []string{"a", "b", "c"}, s)
}

// getBothAndDifference は getBothAndDifference が二つのインタフェースのスライスを比較し、
// 一つ目のスライスにのみ含まれている要素と、両方のスライスに含まれている要素の
// 二つの文字列のスライスを返却しているかテストする。
func Test_getBothAndDifference(t *testing.T) {
	i1 := []interface{}{"a", "b", "c"}
	i2 := []interface{}{"a", "d", "e"}

	s1, s2 := getBothAndDifference(i1, i2)
	assert.Equal(t, []string{"b", "c"}, s1)
	assert.Equal(t, []string{"a"}, s2)
}
