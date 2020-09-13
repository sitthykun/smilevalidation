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

	def getDateOne(self) -> dict:
		"""

		:return:
		"""
		return self.__type.getDate(
			require= True
			, format= '%Y%m%d'
		)

	# sample
	def getEmailOne(self) -> dict:
		"""

		:return:
		"""
		return self.__type.getString(
			require= True
			, maxLength= 55
			, minLength= 8
			, unicode= False
			, regex= None
		)

	def getEmailTwo(self) -> dict:
		"""

		:return:
		"""
		return self.__type.getString(
			require= True
			, maxLength= 55
			, minLength= 8
			, unicode= False
			, regex='^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$'
		)

	def getCostOne(self) -> dict:
		"""

		:return:
		"""
		return self.__type.getFloat(
			require= True
			, max= 5
			, min= 1
			, negative= False
		)
