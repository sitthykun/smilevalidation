"""
Author: masakokh
Version: 1.0.1
Note:
"""
# built-in
from typing import Any
# internal
from InvalidTypeList import InvalidTypeList
from rule.BaseRule import BaseRule
from schema.BoolSchema import BoolSchema


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
		self.run()

	def run(self) -> None:
		"""

		:return:
		"""
		#
		super().run()
		# if found an error, it will stop checking other error
		# foundError	= False

		# type
		if self.validateType() is False:
			# add more error
			self.addErrorNumber(
				InvalidTypeList.B_600
			)

			# add in detail
			self.addErrorDetail(
				BoolSchema.keyValue
			)

			# # found
			# foundError = True

	def validateType(self) -> bool:
		"""

		:return:
		"""
		if self.getValue():
			return isinstance(self.getValue(), bool)
		#
		return False
