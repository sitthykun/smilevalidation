"""
Author: masakokh
Version: 1.0.0
Note:
"""
# built-in
from typing import Any
# internal
from schema.ComparisonSchema import ComparisonSchema


class ComparisonRule:
	"""

	"""

	def __init__(self):
		"""

		"""
		# element
		self.__error		= ''
		# keep error in detail
		self.__errorDetail	= ''
		self.__errorNumber	= 0

	def addErrorNumber(self, errorNumber: int) -> None:
		"""

		:param errorNumber:
		:return:
		"""
		self.__errorNumber	= errorNumber

	def addErrorDetail(self, errorName: str) -> None:
		"""

		:param errorName:
		:return:
		"""
		self.__errorDetail	= errorName

	def getErrorDetail(self) -> str:
		"""

		:return:
		"""
		return self.__errorDetail

	def getErrorNumber(self) -> int:
		"""

		:return:
		"""
		return self.__errorNumber
