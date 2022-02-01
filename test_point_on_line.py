# test point_on_line

import pytest

def test_create_line():
	from point_on_line import create_line
	answer = create_line([1,1],[2,2])
	assert answer == 1


def test_output_y():
	from point_on_line import output_y
	answer = output_y(3)
	assert answer == 3
