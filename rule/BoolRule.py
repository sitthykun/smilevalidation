"""
Author: masakokh
Version: 1.0.0
Note:
"""
from typing import Any
from smilevalidation.rule.BaseRule import BaseRule
from smilevalidation.schema.BaseSchema import BaseSchema


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
		# if found an error, it will stop checking other error
		# foundError	= False

		# type
		if self.validateType() is False:
			# add more error
			self._addError(
				BaseSchema.keyValue
			)

			# add in detail
			self._addErrorDetail(
				BaseSchema.keyErrorDetail[
					BaseSchema.keyValue
				]
			)

			# found
			# foundError = True

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
