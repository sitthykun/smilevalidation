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
		self.__errorNumber	= 0
		# keep error in detail
		self.__errorDetail	= ''

	def _addErrorNumber(self, errorNumber: int) -> None:
		"""

		:param errorNumber:
		:return:
		"""
		self.__errorNumber	= errorNumber

	# def _addErrorNumber(self, errorName: str) -> None:
	# 	"""
	#
	# 	:param errorName:
	# 	:return:
	# 	"""
	# 	self.__error		= errorName

	def _addErrorDetail(self, errorName: str) -> None:
		"""

		:param errorName:
		:return:
		"""
		self.__errorDetail	= errorName

	# def getError(self) -> str:
	# 	"""
	#
	# 	:return:
	# 	"""
	# 	return self.__error

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
