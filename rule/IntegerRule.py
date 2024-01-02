"""
Author: masakokh
Version: 1.0.1
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

		# run validation
		self.run()

	def run(self) -> None:
		"""

		:return:
		"""
		#
		super().run()

		# type
		if self.validateType() is False:
			# add more error
			self.addErrorNumber(
				InvalidTypeList.I_302
			)

			# add in detail
			self.addErrorDetail(
				IntegerSchema.keyDataType
			)

	def validateType(self) -> bool:
		"""

		:return:
		"""
		# Console.output(f'rule.IntegerRule.validateType  {self.getValue()=}')
		if self.getValue():
			return isinstance(self.getValue(), int)
		#
		return False
