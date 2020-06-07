"""
Author: masakokh
Version: 1.0.0
Note:
"""
from typing import Any
from rule.NumericRule import NumericRule
from schema.IntegerSchema import IntegerSchema


class IntegerRule(NumericRule):
	"""

	"""

	def __init__(self, element: dict, require: bool= None, maxValue: int= None, minValue: int= None, negative: bool= None):
		"""

		:param element: name and value
		:param require:
		:param maxValue:
		:param minValue:
		:param negative:
		"""
		super().__init__(
			element
			, require
			, maxValue
			, minValue
			, negative
		)

		# run validation
		self.__run()

	def __run(self) -> None:
		"""

		:return:
		"""
		# type
		if self.validateType() is False:
			self._addError(
				IntegerSchema.keyType
			)

	def validateType(self) -> bool:
		"""

		:return:
		"""
		if self.getValue():
			if isinstance(self.getValue(), int):
				return True
			else:
				return False
		else:
			return False
