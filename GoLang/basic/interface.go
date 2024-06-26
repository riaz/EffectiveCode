package basic

/*
In go interfaces are implicitly defined, i.e no explicit mention of interface or using implements keyword
Any type or sturct that implements all the functions defined in a interface, is said to implement that interface
That makes it hard to tell what interface a type implements, but with some familiarity with the system it can be
easy to spot
*/

// We will test implicit intent of interfaces and assignment using an interface.

type Bike interface {
	GetTopSpeed() float64        // get top speed
	GetDistance(float64) float64 // get the distance as float32
}

type MountainBike struct {
	Make     string
	Name     string
	Topspeed float64
}

type RoadBike struct {
	Make     string
	Name     string
	Topspeed float64
}

func (m MountainBike) GetTopSpeed() float64 {
	return m.Topspeed
}

func (m RoadBike) GetTopSpeed() float64 {
	return m.Topspeed
}

func (m MountainBike) GetDistance(time float64) float64 {
	return (time * m.Topspeed)
}

func (m RoadBike) GetDistance(time float64) float64 {
	return (time * m.Topspeed)
}

func TypeSwitch(b Bike) (string, Bike) {
	switch bike := b.(type) {
	case MountainBike:
		return "Mountain Bike", bike
	case RoadBike:
		return "Road Bike", bike
	case Bike:
		return "Generic Bike", bike
	default:
		return "Unknown Bike", bike
	}
}
