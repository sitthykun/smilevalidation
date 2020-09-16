"""
Author: masakokh
Version: 1.1.0
Note:
"""
from typing import Any
from smilevalidation.schema.NumericSchema import NumericSchema


class IntegerSchema(NumericSchema):
	"""

	"""
	# data type
	keyDataType			= 'int'

	# translate error
	NumericSchema.keyErrorDetail.update({
		keyDataType: 'Not an integer type'
	})
