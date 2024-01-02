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


class DateSchema(BaseSchema):
	"""

	"""
	keyYear2        = 'year_2'
	keyYear4        = 'year_4'
	keyMonth        = 'month'
	keyDay          = 'day'

	# data type
	# d datetime.now(), and type(d)
	keyDataType     = 'date'

	# # translate error
	# keyErrorDetail	= {
	# 	keyYear4        : ErrorList.DT_111  # Contained is not a year two
	# 	, keyYear2      : ErrorList.DT_112  # Contained is not a year four
	# 	, keyMonth      : ErrorList.DT_113  # Contained is not a month
	# 	, keyDay        : ErrorList.DT_114  # Contained is not a day
	# 	, keyDataType   : ErrorList.DT_110  # Contained is not a date
	# }
