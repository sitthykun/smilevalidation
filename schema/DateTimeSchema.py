"""
Author: masakokh
Version: 1.1.1
Note:
"""
# built-in
from typing import Any
# internal
from InvalidTypeList import InvalidTypeList as ErrorList
from schema.BaseSchema import BaseSchema


class DateTimeSchema(BaseSchema):
	"""

	"""
	keyDate			= 'date'
	keyDateTime 	= 'datetime'
	keyTime			= 'time'

	# data type
	# d datetime.now(), and type(d)
	keyDataType		= 'datetime'

	# # translate error
	# keyErrorDetail	= {
	# 	keyDate			: ErrorList.DT_110	#'Contained is not a date'
	# 	, keyDateTime	: ErrorList.DT_100	#'Contained is not a datetime'
	# 	, keyTime		: ErrorList.DT_120	#'Contained is not a time'
	# 	, keyDataType	: ErrorList.DT_101	#'Not a datetime type'
	# }
