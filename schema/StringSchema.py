"""
Author: masakokh
Version: 1.0.0
Note:
"""
from typing import Any
from smilevalidation.schema.BaseSchema import BaseSchema


class StringSchema(BaseSchema):
	"""

	"""
	keyMaxLength	= 'max_length'
	keyMinLength	= 'min_length'
	# min > max or another reason
	keyWrongRange	= 'min_max_range'
	keyRegEx		= 'regex'
	keyUnicode		= 'unicode'
	# data type
	keyDataType		= 'str'

	# translate error
	keyErrorDetail	= {
		keyMaxLength: 'Contained over maximum of string length'
		, keyMinLength: 'Contained less than minimum of string length'
		, keyUnicode: 'Contained unicode character'
		, keyDataType: 'Not a string type'
		, keyWrongRange: 'Not in provided range'
		, keyRegEx: 'Not matched the regular expression'
		, BaseSchema.keyType: 'Type is not matched'
	}

