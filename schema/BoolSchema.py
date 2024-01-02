"""
Author: masakokh
Version: 1.1.1
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
	keyDataType		= 'bool'

	# # translate error
	# keyErrorDetail	= {
	# 	keyDataType	: ErrorList.B_600	# Not a boolean type
	# }
