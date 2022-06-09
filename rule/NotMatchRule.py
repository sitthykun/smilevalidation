"""
Author: masakokh
Version: 1.0.0
Note:
"""
# built-in
from typing import Any
# internal
from rule.ComparisonRule import ComparisonRule
from schema.ComparisonSchema import ComparisonSchema


class NotMatchRule(ComparisonRule):
	"""

	"""

	def __init__(self, name1: str, value1: Any, name2: str, value2: Any):
		"""

		:param name1:
		:param value1:
		:param name2:
		:param value2:
		"""
		super().__init__()

		# compare False
		self.__isMatched	= False

		# start compare
		self.__compare(name1, value1, name2, value2)

	def __compare(self, name1: str, value1: Any, name2: str, value2: Any) -> None:
		"""

		:param name1:
		:param value1:
		:param name2:
		:param value2:
		:return:
		"""
		if not((value1 is not value2) is self.__isMatched):
			# add error
			self._addErrorNumber(
				ComparisonSchema.keyMatch
			)

			# add in detail
			self._addErrorDetail(
				ComparisonSchema.keyErrorDetail[
					ComparisonSchema.keyMatch
				]
			)

