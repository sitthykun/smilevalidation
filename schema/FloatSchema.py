"""
Author: masakokh
Version: 1.1.0
Note:
"""
from typing import Any
from smilevalidation.schema.NumericSchema import NumericSchema


class FloatSchema(NumericSchema):
	"""

	"""
	keyPrecision		= 'precision'
	# data type
	keyDataType			= 'float'

	# translate error
	NumericSchema.keyErrorDetail.update({
		keyPrecision: 'No precision'
		, keyDataType: 'Not a float type'
	})
