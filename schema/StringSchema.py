"""
Author: masakokh
Version: 1.0.0
Note:
"""
from typing import Any
from schema.BaseSchema import BaseSchema


class StringSchema(BaseSchema):
	"""

	"""
	keyMaxLength		= 'max_length'
	keyMinLength		= 'min_length'
	# min > max or another reason
	keyWrongRange		= 'min_max_range'
	keyRegEx			= 'regex'
	keyUnicode			= 'unicode'
	# data type
	keyDataType			= 'str'

