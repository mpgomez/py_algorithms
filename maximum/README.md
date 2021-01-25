# Maximum
Calculate the maximum of to numbers, without using if/else or comparisons.
Assumptions:
I am assuming the bit at the left (the first bit) of an integer represents the sign of an integer.

def max_number(a, b):
	# I want an integer with all zeros except the first bit (the sign), something like 10000...000
	sign_mask = ~((~ 0) >> 1)
	int_length = sys.getsizeof(int()) * 8
	a_sign = (a - b) & sign_mask
	a_sign = a_sing >> (int_length - 1)
	b_sign = (b - a) & sign_mask
	b_sign = b_sing >> (int_length - 1)
	return a * a_sign + b * b_sing
