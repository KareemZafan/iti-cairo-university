import pytest
import math

def get_square_root(value):
	return math.sqrt(value) 
	
def subtract(a , b):
	return a - b



def test_square_root():
	assert 10 == get_square_root(100)
	assert 25 == get_square_root(625)
	
def test_subtract():
	assert 10 == subtract(100, 90)
	
