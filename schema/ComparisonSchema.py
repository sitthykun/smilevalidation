"""
Author: masakokh
Version: 1.1.0
Note:
"""
# built-in
from typing import Any
import re
# internal
from InvalidTypeList import InvalidTypeList as ErrorList
# schema
from schema.BaseSchema import BaseSchema


class ComparisonSchema(BaseSchema):
	"""

	"""
	# match
	keyMatch		= 'match'
	keyNotMatch		= 'not_match'

	# # translate error
	# keyErrorDetail	= {
	# 	keyMatch		: ErrorList.C_400
	# 	, keyNotMatch	: ErrorList.C_401
	# }
