"""
Author: masakokh
Version: 1.0.1
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
	# datetime
	DT_100	= 100	# Not a datetime
	DT_101  = 101   # Not a datetime type
	# date
	DT_110  = 110  # Contained is not a date
	DT_111  = 111  # Contained is not a year two
	DT_112  = 112  # Contained is not a year four
	DT_113  = 113  # Contained is not a month
	DT_114  = 114  # Contained is not a day
	# time
	DT_120  = 120   # Contained is not a time
	DT_121	= 121	# Contained is not an hour 24
	DT_122	= 122	# Contained is not an hour 12
	DT_123	= 123	# Contained is not a minute
	DT_124  = 124   # Contained is not a second
	DT_125  = 125   # Contained is not a milli
	DT_126  = 126  # Contained 24 and 12 in the rule
	DT_127  = 127  # Contained 12 and 24 in the rule
	# float
	F_300	= 300	# No precision
	F_301	= 301	# Not a float type
	# general
	G_900   = 900
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
	# N_306	= 306	# Type is not matched
	N_307   = 307   # Max less than min
	# string
	S_200	= 200	# Contained over maximum of string length
	S_201	= 201	# Contained less than minimum of string length
	S_202	= 202	# Contained unicode character
	S_203	= 203	# Not a string type
	S_204	= 204	# Not in provided range
	S_205	= 205	# Not matched the regular expression
	S_206	= 206	# Type is not matched
	S_207   = 207   # Min and Max
