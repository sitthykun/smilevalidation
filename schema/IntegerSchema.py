"""
Author: masakokh
Version: 1.1.0
Note:
"""
# built-in
from typing import Any
# internal
from InvalidTypeList import InvalidTypeList as ErrorList
from schema.NumericSchema import NumericSchema


class IntegerSchema(NumericSchema):
	"""

	"""
	# data type
	keyDataType			= 'int'

	# # translate error
	# NumericSchema.keyErrorDetail.update({
	# 	keyDataType		: ErrorList.I_302	# 'Not an integer type'
	# })
