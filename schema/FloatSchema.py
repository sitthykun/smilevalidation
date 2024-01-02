"""
Author: masakokh
Version: 1.1.1
Note:
"""
# built-in
from typing import Any
# internal
from InvalidTypeList import InvalidTypeList as ErrorList
from schema.NumericSchema import NumericSchema


class FloatSchema(NumericSchema):
	"""

	"""
	keyPrecision		= 'precision'
	# data type
	keyDataType			= 'float'

	# translate error
	# NumericSchema.keyErrorDetail.update({
	# 	keyPrecision	: ErrorList.F_300	# 'No precision'
	# 	, keyDataType	: ErrorList.F_301	# 'Not a float type'
	# })
