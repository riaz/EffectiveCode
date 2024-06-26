package basic_test

import (
	"testing"

	"github.com/riaz/EffectiveCode/GoLang/basic"
	"github.com/stretchr/testify/assert"
)

func Test_Interfaces(t *testing.T) {
	var mbike basic.Bike = basic.MountainBike{Make: "MT", Name: "MT1", Topspeed: 20.0}
	var rbike basic.Bike = basic.RoadBike{Make: "RB", Name: "RB1", Topspeed: 40.0}

	assert.Equal(t, 20.0, mbike.GetTopSpeed())
	assert.Equal(t, 40.0, rbike.GetTopSpeed())
}
