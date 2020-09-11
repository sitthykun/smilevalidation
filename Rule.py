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

		# sample
		# field
		self.__emailOne		= self.__type.getString(
			require= True
			, maxLength= 75
			, minLength= 8
			, unicode= False
			, regex= None
		)

		self.__dateOne		= self.__type.getDate(
			require= True
			, format= '%Y%m%d'
		)

	def getDateOne(self) -> dict:
		"""

		:return:
		"""
		return self.__dateOne

	# sample
	def getEmailOne(self) -> dict:
		"""

		:return:
		"""
		return self.__emailOne
