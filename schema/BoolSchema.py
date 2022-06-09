"""
Author: masakokh
Version: 1.1.0
Note:
"""
# built-in
from typing import Any
# internal
from InvalidTypeList import InvalidTypeList as ErrorList
from schema.NumericSchema import NumericSchema


class BoolSchema(NumericSchema):
	"""

	"""
	# data type
	# d datetime.now(), and type(d)
	keyDateType		= 'bool'

	# translate error
	keyErrorDetail	= {
		keyDateType	: ErrorList.B_600	# Not a boolean type
	}
