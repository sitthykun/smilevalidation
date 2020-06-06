"""
Author: masakokh
Version: 1.0.0
Note:
"""
from typing import Any
from rule.BaseRule import BaseRule
from schema.BaseSchema import BaseSchema


class BoolRule(BaseRule):
	"""

	"""

	def __init__(self, element: dict, require: bool= None, value: bool= None):
		"""

		:param element:
		:param require:
		:param value:
		"""
		super().__init__(
			element
			, require
		)

		# precision
		self.__value	= value

		# run validation
		self.__run()

	def __run(self) -> None:
		"""

		:return:
		"""

		# type
		if self.validateType() is False:
			self._addError(
				BaseSchema.keyValue
			)

	def validateType(self) -> bool:
		"""

		:return:
		"""
		if self.getValue():
			if isinstance(self.getValue(), bool):
				return True
			else:
				return False
		else:
			return False
