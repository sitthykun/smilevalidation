"""
Author: masakokh
Version: 1.1.0
Note:
"""
# built-in
from typing import Any
# internal
from InvalidTypeList import InvalidTypeList as ErrorList
# schema super
from schema.BaseSchema import BaseSchema


class BoolSchema(BaseSchema):
	"""

	"""
	# data type
	# d datetime.now(), and type(d)
	keyDateType		= 'bool'

	# translate error
	keyErrorDetail	= {
		keyDateType	: ErrorList.B_600	# Not a boolean type
	}
