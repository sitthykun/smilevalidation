"""
Author: masakokh
Version: 1.0.0
Note:
"""
import re
from typing import Any
import datetime
from rule.BaseRule import BaseRule
from schema.DateTimeSchema import DateTimeSchema


class TimeRule(BaseRule):
	"""

	"""
	def __init__(self, element: dict, require: bool= None, formatTime: str= None):
		"""

		:param element:
		:param require:
		:param formatTime:
		"""
		pass

	def __run(self) -> None:
		"""

		:return:
		"""

		# wrong type
		if self.validateType() is False:
			self._addError(
				DateTimeSchema.keyTime
			)

			# found
			foundError	= True

	def validateType(self) -> bool:
		"""

		:return:
		"""
		if self.getValue():
			if isinstance(self.getValue(), datetime.time):
				return True
			else:
				return False
		else:
			return False
