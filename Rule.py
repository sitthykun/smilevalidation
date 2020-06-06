"""
Author: masakokh
Version: 1.0.0
"""
from typing import Any
from schema.TypeSchema import TypeSchema
from rule import *


class Rule:
	"""

	"""
	def __init__(self):
		"""

		"""
		# instance
		self.__type			= TypeSchema()

		# field
		self.__emailOne		= self.__type.getString(
			require= True
			, maxLength= 75
			, minLength= 8
			, unicode= False
			, regex= None
		)

		self.__emailTwo		= self.__type.getString(
			require= False
			, maxLength= 125
			, minLength= 8
			, unicode= False
			, regex= '/mail/'
		)

		self.__currencyOne	= self.__type.getFloat(
			require= True
			, min= 21
			, max= 42
			, precision= 2
		)

	def getCurrencyOne(self) -> dict:
		"""

		:return:
		"""
		return self.__currencyOne

	def getEmailOne(self) -> dict:
		"""

		:return:
		"""
		return self.__emailOne

	def getEmailTwo(self) -> dict:
		"""

		:return:
		"""
		return self.__emailTwo
