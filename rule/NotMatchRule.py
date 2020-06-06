"""
Author: masakokh
Version: 1.0.0
Note:
"""
from typing import Any
from rule.ComparisonRule import ComparisonRule


class NotMatchRule(ComparisonRule):
	"""

	"""

	def __init__(self, element: dict, value1: Any, value2: Any):
		"""
		# match and not match cannot be together
		:param element:
		:param value1:
		:param value2:
		"""
		super().__init__(element)

		# compare False
		self.__isMatched	= False

		# value comparision
		self.__value1		= value1
		self.__value2		= value2

	def compare(self) -> bool:
		"""
		compare to find false
		:return:
		"""
		return (self.__value1 is not self.__value2) is self.__compareFalse
