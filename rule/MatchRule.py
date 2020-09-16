"""
Author: masakokh
Version: 1.0.1
Note:
"""
from typing import Any
from smilevalidation.rule.ComparisonRule import ComparisonRule
from smilevalidation.schema.ComparisonSchema import ComparisonSchema


class MatchRule(ComparisonRule):
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

		# compare True
		self.__isMatched	= True

		# compare now
		self.__compare(name1, value1, name2, value2)

	def __compare(self, name1: str, value1: Any, name2: str, value2: Any) -> None:
		"""

		:param name1:
		:param value1:
		:param name2:
		:param value2:
		:return:
		"""
		if not((value1 is value2) is self.__isMatched):
			# add error
			self._addError(
				ComparisonSchema.keyMatch
			)

			# add in detail
			self._addErrorDetail(
				ComparisonSchema.keyErrorDetail[
					ComparisonSchema.keyMatch
				] + self._suffixErrorMessage(name1, value1, name2, value2, 'Not matched')
			)
