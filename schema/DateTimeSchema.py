"""
Author: masakokh
Version: 1.0.0
Note:
"""
from typing import Any
from schema.BaseSchema import BaseSchema


class DateTimeSchema(BaseSchema):
	"""

	"""
	keyDate		= 'date'
	keyDateTime = 'datetime'
	keyTime		= 'time'

	# data type
	# d datetime.now(), and type(d)
	keyDataType	= 'datetime.datetime'
