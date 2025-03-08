import pytest
import math

def get_square_root(value):
	return math.sqrt(value) 
	



def test_square_root():
	assert 10 == get_square_root(100)
	assert 25 == get_square_root(625)
