"""
Author: masakokh
Version: 1.0.0
Note:
"""
# built-in
from typing import Any
# internal
from schema.BaseSchema import BaseSchema
# from schema.NumericSchema import NumericSchema


class BaseRule(BaseSchema):
	"""
	1. empty
	2. require
	3. value

	4. max_length	| string, unicode
	5. min_length	|

	4. max_value	| int, float
	5. min_value	|
	"""

	def __init__(self, element: dict, require: bool= None):
		"""

		:param element:
		:param require:
		"""
		# match or not match value
		self.__matchValue	= None
		#
		self.__requireValue = require
		# self.__requireValue	= True
		# fix key for each element
		self.__valueValue	= None

		# element
		self.element		= element
		# error as dict type
		# self.__error		= {}
		self.__error		= ''
		# keep error in detail
		self.__errorDetail	= ''

		# run validation
		self.__run()

	def __run(self) -> None:
		"""

		:return:
		"""
		# False
		if not self.validateRequire():
			self._addErrorNumber(
				next(
					iter(
						self.element.keys()
					)
				)
				#, super().keyRequire
			)

	# def _addErrorNumber(self, elementName: str, errorType: str) -> None:
	# 	"""
	#
	# 	:param elementName:
	# 	:param errorType:
	# 	:return:
	# 	"""
	# 	# accept only the first error for an element
	# 	if self.__error.get(elementName):
	# 		# add error to collect
	# 		self.__error.update({
	# 			elementName: errorType
	# 		})
	# def _addError(self, errorName: str) -> None:
	# 	"""
	#
	# 	:param errorName:
	# 	:return:
	# 	"""
	# 	self.__error		= errorName

	def _addErrorNumber(self, errorNumber: int) -> None:
		"""

		:param errorNumber:
		:return:
		"""
		self.__errorNumber	= errorNumber

	def _addErrorDetail(self, errorName: str) -> None:
		"""

		:param errorName:
		:return:
		"""
		self.__errorDetail	= errorName

	def _getElementName(self) -> str:
		"""

		:return:
		"""
		return self.element.get('name')

	# def getError(self) -> dict:
	# 	"""
	#
	# 	:return:
	# 	"""
	# 	return self.__error

	# def getError(self) -> str:
	# 	"""
	#
	# 	:return:
	# 	"""
	# 	return self.__error
	def getErrorNumber(self) -> int:
		"""

		:return:
		"""
		return self.__errorNumber

	def getErrorDetail(self) -> str:
		"""

		:return:
		"""
		return self.__errorDetail

	def getValue(self) -> Any:
		"""

		:return:
		"""
		try:
			return self.element[self.keyValue]

		except KeyError as e:
			return None

		except Exception as e:
			return None

	def validateRequire(self) -> bool:
		"""

		{'require':True}
		:return:
		"""
		try:
			if self.element[self.keyRule][self.keyRequire]:
				return True

			else:
				return False

		except KeyError as e:
			return False

		except Exception as e:
			return False
