"""
Author: masakokh
Version: 1.1.0
Note:
"""
from typing import Any
from smilevalidation.schema.BaseSchema import BaseSchema


class NumericSchema(BaseSchema):
	"""

	"""
	keyMaxValue		= 'max_value'
	keyMinValue		= 'min_value'
	keyNegative		= 'negative'

	# translate error
	keyErrorDetail	= {
		keyMaxValue: 'Greater than maximum value'
		, keyMinValue: 'Less than minimum value'
		, keyNegative: 'Negative not allow'
		, BaseSchema.keyType: 'Type is not matched'
	}
