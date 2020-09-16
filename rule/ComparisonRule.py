"""
Author: masakokh
Version: 1.0.0
Note:
"""
from typing import Any
from smilevalidation.schema.ComparisonSchema import ComparisonSchema


class ComparisonRule:
	"""

	"""

	def __init__(self):
		"""

		:param element:
		"""
		# element
		self.__error		= ''
		# keep error in detail
		self.__errorDetail	= ''

	def _addError(self, errorName: str) -> None:
		"""

		:param errorName:
		:return:
		"""
		self.__error		= errorName

	def _addErrorDetail(self, errorName: str) -> None:
		"""

		:param errorName:
		:return:
		"""
		self.__errorDetail	= errorName

	def _suffixErrorMessage(self, element1: str, value1: Any, element2: str, value2: Any, flag: str) -> str:
		"""

		:param elementOne:
		:param elementTwo:
		:param flag:
		:return:
		"""
		return f'( between <<{value1}>> and <<{value2}>>, is {flag})'

	def getError(self) -> str:
		"""

		:return:
		"""
		return self.__error

	def getErrorDetail(self) -> str:
		"""

		:return:
		"""
		return self.__errorDetail
