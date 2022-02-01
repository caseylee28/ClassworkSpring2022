# test point_on_line

import pytest

#def test_create_line():
#	from point_on_line import create_line
#	answer = create_line([1,1],[2,2])
#	assert answer == 1

def test_slope_2points():
    from point_on_line import slope_2points
    answer = slope_2points((-3,4),(5,-6))
    assert answer == -5/4


def test_output_y():
	from point_on_line import output_y
	answer = output_y(-5,2,(3,-4))
	assert answer == -20
