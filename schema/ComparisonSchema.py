"""
Author: masakokh
Version: 1.1.0
Note:
"""
from typing import Any
from schema.BaseSchema import BaseSchema


class ComparisonSchema(BaseSchema):
	"""

	"""
	# match
	keyMatch		= 'match'
	keyNotMatch		= 'not_match'

	# translate error
	keyErrorDetail	= {
		keyMatch: 'Is matched'
		, keyNotMatch: 'Not matched'
	}
