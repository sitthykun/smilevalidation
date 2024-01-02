"""
Author: masakokh
Version: 1.0.1
Note:
"""
# built-in
from typing import Any
# internal
from InvalidTypeList import InvalidTypeList as ErrorList
from schema.BaseSchema import BaseSchema


class StringSchema(BaseSchema):
	"""

	"""
	# blank string equal to empty
	keyEmpty		= 'empty'
	keyMaxLength	= 'max_length'
	keyMinLength	= 'min_length'
	# min > max or another reason
	keyWrongRange	= 'min_max_range'
	keyRegEx		= 'regex'
	keyUnicode		= 'unicode'
	# data type
	keyDataType		= 'str'

	# translate error
	# keyErrorDetail	= {
	# 	keyMaxLength		: ErrorList.S_200	# 'Contained over maximum of string length'
	# 	, keyMinLength		: ErrorList.S_201	# 'Contained less than minimum of string length'
	# 	, keyUnicode		: ErrorList.S_202	# 'Contained unicode character'
	# 	, keyDataType		: ErrorList.S_203	# 'Not a string type'
	# 	, keyWrongRange		: ErrorList.S_204	# 'Not in provided range'
	# 	, keyRegEx			: ErrorList.S_205	# 'Not matched the regular expression'
	# 	, BaseSchema.keyType: ErrorList.S_206	# 'Type is not matched'
	# }

