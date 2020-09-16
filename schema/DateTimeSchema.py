"""
Author: masakokh
Version: 1.1.0
Note:
"""
from typing import Any
from smilevalidation.schema.BaseSchema import BaseSchema


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
		keyDate: 'Contained is not a date'
		, keyDateTime: 'Contained is not a datetime'
		, keyTime: 'Contained is not a time'
		, keyDateType: 'Not a datetime type'
	}
