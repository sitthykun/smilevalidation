"""
Author: masakokh
Version: 1.0.0
"""
from typing import Any


class InvalidTypeList:
	"""

	"""
	# bool
	B_600	= 600	# Not a boolean type
	# comparison
	C_400	= 400	# Need matched form
	C_401	= 401	# Need not matched form
	# date
	D_100	= 100	# Contained is not a date
	D_101	= 101	# Contained is not a datetime
	D_102	= 102	# Contained is not a time
	D_103	= 103	# Not a datetime type
	# float
	F_300	= 300	# No precision
	F_301	= 301	# Not a float type
	# integer
	I_302	= 302	# Not an integer type
	# list
	L_500	= 500
	# match
	M_700	= 700	# Match wrong type
	M_701	= 701	# Match
	# numeric
	N_303	= 303	# Greater than maximum value
	N_304	= 304	# Less than minimum value
	N_305	= 305	# Negative not allow
	N_306	= 306	# Type is not matched
	# string
	S_200	= 200	# Contained over maximum of string length
	S_201	= 201	# Contained less than minimum of string length
	S_202	= 202	# Contained unicode character
	S_203	= 203	# Not a string type
	S_204	= 204	# Not in provided range
	S_205	= 205	# Not matched the regular expression
	S_206	= 206	# Type is not matched
