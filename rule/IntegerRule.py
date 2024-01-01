"""
Author: masakokh
Version: 1.0.0
Note:
"""
# built-in
from typing import Any
# internal
from InvalidTypeList import InvalidTypeList
from rule.NumericRule import NumericRule
from schema.IntegerSchema import IntegerSchema
from Console import Console


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

		# private
		self.__isValid  = True

		# run validation
		self.run()

	def run(self) -> None:
		"""

		:return:
		"""
		if self.validateType():
			super().run()

		else:
			# if found an error, it will stop checking other error
			self.__isValid	= False

	def isValid(self) -> bool:
		"""

		:return:
		"""
		return super().isValid() and self.__isValid

	def validateType(self) -> bool:
		"""

		:return:
		"""
		Console.output(f'rule.IntegerRule.validateType  {self.getValue()=}')
		if self.getValue():
			return isinstance(self.getValue(), int)
		#
		return False
