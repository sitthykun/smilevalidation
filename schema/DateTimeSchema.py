"""
Author: masakokh
Version: 1.1.0
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
	keyDateType		= 'datetime.datetime'

	# translate error
	keyErrorDetail	= {
		keyDate			: ErrorList.D_100	#'Contained is not a date'
		, keyDateTime	: ErrorList.D_101	#'Contained is not a datetime'
		, keyTime		: ErrorList.D_102	#'Contained is not a time'
		, keyDateType	: ErrorList.D_103	#'Not a datetime type'
	}
