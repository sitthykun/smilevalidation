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


class NumericSchema(BaseSchema):
	"""

	"""
	keyMaxValue		= 'max_value'
	keyMinValue		= 'min_value'
	keyNegative		= 'negative'

	# # translate error
	# keyErrorDetail	= {
	# 	keyMaxValue         : ErrorList.I_302   # Greater than maximum value
	# 	, keyMinValue       : ErrorList.N_303	# Less than minimum value
	# 	, keyNegative       : ErrorList.N_304	# Negative not allow
	# 	# fix and use only error message
	# 	# , 'max_min'         : ErrorList.N_307   # Negative not allow
	# 	, BaseSchema.keyType: ErrorList.N_305	# Type is not matched
	# }
