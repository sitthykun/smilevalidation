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
	keyYear4       = 'year_4'
	keyYear2       = 'year_2'
	keyMonth       = 'month'
	keyDay         = 'day'

	# data type
	# d datetime.now(), and type(d)
	keyDateType		= 'date'

	# translate error
	keyErrorDetail	= {
		keyYear4        : ErrorList.DT_111  # Contained is not a year two
		, keyYear2      : ErrorList.DT_112  # Contained is not a year four
		, keyMonth      : ErrorList.DT_113  # Contained is not a month
		, keyDay        : ErrorList.DT_114  # Contained is not a day
		, keyDateType   : ErrorList.DT_110  # Contained is not a date
	}
