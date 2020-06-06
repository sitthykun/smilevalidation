"""
Author: masakokh
Version: 1.0.0
Note:
"""
from typing import Any
from schema.BaseSchema import BaseSchema
from schema.NumericSchema import NumericSchema


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

		"""

		self.__requireValue = require
		# self.__requireValue	= True

		# match or not match value
		self.__matchValue	= None

		# fix key for each element
		self.__valueValue	= None

		# element
		self.element		= element
		# error
		# self.__error		= {}
		self.__error		= ''

		# run validation
		self.__run()

	def __run(self) -> None:
		"""

		:return:
		"""
		if self.validateRequire() is False:
			self._addError(
				next(
					iter(
						self.element.keys()
					)
				)
				#, super().keyRequire
			)

	# def _addError(self, elementName: str, errorType: str) -> None:
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
	def _addError(self, errorName: str) -> None:
		"""

		:param errorName:
		:return:
		"""
		self.__error	= errorName

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
	def getError(self) -> str:
		"""

		:return:
		"""
		return self.__error

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
			self.element[self.keyRule][self.keyRequire]
		except KeyError as e:
			return False
		except Exception as e:
			return False
