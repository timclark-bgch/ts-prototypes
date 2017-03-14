import numpy as np
import pandas as pd


def regulate(src, start, end, inc=20):
	output = src.reindex(range(start, end, inc), method='nearest', fill_value=np.NaN, tolerance=(0.9 * inc), limit=1)
	return output.interpolate().replace(np.NaN, 0).round(2)


t1 = pd.Series(
	{
		9: 24.5,
		82: 10.0,
		95: 11.0,
		110: 13.0,
		173: 14.0,
		195: 23.0,
		230: 12.3,
		272: 34.5,
		356: -19.0,
		430: 22.3,
		456: 17.0,
		589: 29.23,
		1110: 13.0,
		1173: 14.0,
		1195: 23.0,
		1230: 12.3,
		1272: 34.5,
		1356: -19.0,
		1430: 22.3,
		1456: 17.0,
		1589: 29.23,
	})

t2 = pd.Series(
	{
		272: 10.0,
		291: 11.0,
		310: 13.0,
		375: 14.0,
	})


def test():
	print regulate(t1, start=0, end=200)

	print regulate(t2, start=0, end=200)


def benchmark():
	return regulate(t1, start=0, end=2000)

# test()
