"""
Author: masakokh
Version: 1.0.1
Note:
"""
# built-in
from typing import Any
# internal
from Console import Console
from InvalidTypeList import InvalidTypeList
from schema.BaseSchema import BaseSchema


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
		# keep error in detail
		self.__errorDetail	= ''
		self.__errorNumber  = 0

		# match or not match value
		self.__matchValue	= None
		#
		self.__requireValue = require
		# fix key for each element
		self.__value        = None

		# public
		# element
		self.element		= element

	def run(self) -> None:
		"""

		:return:
		"""
		# False
		if self.__requireValue is True and not self.validateRequire():
			self.addErrorNumber(
				InvalidTypeList.G_900
			)

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

	def getElementName(self) -> str:
		"""

		:return:
		"""
		return self.element.get(self.keyName)

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
			Console.output(f'rule.BaseRule.getValue KeyError: {str(e)}')
			return None

		except Exception as e:
			Console.output(f'rule.BaseRule.getValue Exception: {str(e)}')
			return None

	def getSplitValue(self) -> list | None:
		"""

		:return:
		"""
		try:
			return self.element[self.keyValue]

		except KeyError as e:
			Console.output(f'rule.BaseRule.getSplitValue KeyError: {str(e)}')
			return None

		except Exception as e:
			Console.output(f'rule.BaseRule.getSplitValue Exception: {str(e)}')
			return None

	def isValid(self) -> bool:
		"""

		:return:
		"""
		return not bool(self.__errorNumber)

	def validateRequire(self) -> bool:
		"""

		{'require':True}
		:return:
		"""
		try:
			# true and value is not null
			# return self.element[self.keyRule][self.keyRequire] is True and self.element[self.keyRule][self.keyValue]
			return self.element[self.keyRule][self.keyRequire] is True and bool(self.getValue())

		except KeyError as e:
			Console.output(f'rule.BaseRule.validateRequire KeyError: {str(e)}')
			return False

		except Exception as e:
			Console.output(f'rule.BaseRule.validateRequire Exception: {str(e)}')
			return False
