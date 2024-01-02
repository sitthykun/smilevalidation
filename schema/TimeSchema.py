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


class TimeSchema(BaseSchema):
	"""

	"""
	keyHour24       = 'hour_24'
	keyHour12       = 'hour12'
	keyMinute       = 'minute'
	keySecond       = 'second'
	keyMillisecond  = 'millisecond'

	# data type
	# d datetime.now(), and type(d)
	keyDataType		= 'time'

	# # translate error
	# keyErrorDetail	= {
	# 	keyHour24		: ErrorList.DT_121	#'Contained is not a hour 24'
	# 	, keyHour12     : ErrorList.DT_122	#'Contained is not a hour 12'
	# 	, keyMinute     : ErrorList.DT_123  #'Contained is not a minute'
	# 	, keySecond     : ErrorList.DT_124  #'Contained is not a second'
	# 	, keyMillisecond: ErrorList.DT_125  #'Contained is not a millisecond'
	# 	, keyDataType	: ErrorList.DT_120	#'Not a time type'
	# }
