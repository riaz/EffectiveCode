package basic

func Sqrt(x float64) float64 {
	z := 0.5 * x

	for z*z > x {
		z -= (z*z - x) / (2 * z)
	}

	return z
}
