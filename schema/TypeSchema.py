"""
Author: masakokh
Version: 1.0.0
"""
from typing import Any
from smilevalidation.rule import *
from smilevalidation.schema import BaseSchema, ComparisonSchema, DateTimeSchema, FloatSchema, IntegerSchema, StringSchema


class TypeSchema:
	"""

	"""
	def __init__(self):
		"""

		"""
		# self.__float	= FloatRule.FloatRule()
		# self.__integer	= IntegerRule.IntegerRule()
		# self.__list		= ListRule.ListRule()
		# self.__string	= StringRule.StringRule()
		# self.__unicode	= UnicodeRule.UnicodeRule()
		pass

	def __findDateFormat(self, format: str) -> bool:
		"""

		:param format:
		:return:
		"""
		found	= False
		# fmts = ('%Y', '%b %d, %Y', '%b %d, %Y', '%B %d, %Y', '%B %d %Y', '%m/%d/%Y', '%m/%d/%y', '%b %Y', '%B%Y', '%b %d,%Y')

		return found

	def __findTimeFormat(self, format: str) -> bool:
		"""

		:param format:
		:return:
		"""
		found = False

		return found

	def getDate(self, require: bool= None, format: str= None) -> dict:
		"""

		:param require:
		:param format:
		:return:
		"""
		temp		= {}

		# type
		temp.update({
			BaseSchema.BaseSchema.keyType: DateTimeSchema.DateTimeSchema.keyDate
		})

		# require
		if require and require is True:
			temp.update({
				BaseSchema.BaseSchema.keyRequire: True
			})

		# format date string
		if format and self.__findDateFormat(format):
			temp.update({
				DateTimeSchema.DateTimeSchema.keyDate: True
			})

		# return the element value
		return temp

	def getDateTime(self, require: bool= None, format: str= None) -> dict:
		"""

		:param require:
		:param format:
		:return:
		"""
		temp		= {}

		# type
		temp.update({
			BaseSchema.BaseSchema.keyType: FloatSchema.FloatSchema.keyDataType
		})

		# require
		if require and require is True:
			temp.update({
				BaseSchema.BaseSchema.keyRequire: True
			})

		# format date string
		if format and self.__findDateFormat(format) and self.__findTimeFormat(format):
			temp.update({
				DateTimeSchema.DateTimeSchema.keyDateTime: True
			})

		# return the element value
		return temp

	def getFloat(self, require: bool= None, max: int= None, min: int= None, negative: bool= None, precision: int= None) -> dict:
		"""

		:param require:
		:param max:
		:param min:
		:param negative:
		:param precision:
		:return:
		"""
		temp		= {}

		# type
		temp.update({
			BaseSchema.BaseSchema.keyType: FloatSchema.FloatSchema.keyDataType
		})

		# require
		if require and require is True:
			temp.update({
				BaseSchema.BaseSchema.keyRequire: True
			})

		# max
		if max:
			temp.update({
				FloatSchema.FloatSchema.keyMaxValue: max
			})

		# min
		if min:
			temp.update({
				FloatSchema.FloatSchema.keyMinValue: min
			})

		# negative
		if negative:
			temp.update({
				FloatSchema.FloatSchema.keyNegative: negative
			})

		# precision
		if precision:
			temp.update({
				FloatSchema.FloatSchema.keyPrecision: precision
			})

		# return the element value
		return temp

	def getInteger(self, require: bool= None, max: int= None, min: int= None, negative: bool= None) -> dict:
		"""

		:param require:
		:param max:
		:param min:
		:param negative:
		:return:
		"""
		# temp of dict
		temp		= {}

		# type
		temp.update({
			BaseSchema.BaseSchema.keyType: IntegerSchema.IntegerSchema.keyDataType
		})

		# require
		if require and require is True:
			temp.update({
				BaseSchema.BaseSchema.keyRequire: True
			})

		# max
		if max:
			temp.update({
				IntegerSchema.IntegerSchema.keyMaxValue: max
			})

		# min
		if min:
			temp.update({
				IntegerSchema.IntegerSchema.keyMinValue: min
			})

		# negative
		if negative:
			temp.update({
				IntegerSchema.IntegerSchema.keyNegative: negative
			})

		# return the element value
		return temp

	def getListInteger(self) -> dict:
		return {}

	def getListFloat(self) -> dict:
		return {}

	def getListString(self) -> dict:
		return {}

	def getString(self, require: bool= None, maxLength: int= None, minLength: int= None, regex: str= None,  unicode: bool= None) -> dict:
		"""

		:param require:
		:param maxLength:
		:param minLength:
		:param regex:
		:param unicode:
		:return:
		"""
		temp		= {}

		# type
		temp.update({
			BaseSchema.BaseSchema.keyType: StringSchema.StringSchema.keyDataType
		})

		# require
		if require and require is True:
			temp.update({
				BaseSchema.BaseSchema.keyRequire: True
			})

		# maxLength
		if maxLength:
			temp.update({
				StringSchema.StringSchema.keyMaxLength: maxLength
			})

		# minLength
		if minLength:
			temp.update({
				StringSchema.StringSchema.keyMinLength: minLength
			})

		# regex
		if regex:
			temp.update({
				StringSchema.StringSchema.keyRegEx: regex
			})

		# unicode
		if unicode and unicode is True:
			temp.update({
				StringSchema.StringSchema.keyUnicode: True
			})

		# return the element value
		return temp

	def getTime(self, require: bool= None, format: str= None) -> dict:
		"""

		:param require:
		:param format:
		:return:
		"""
		temp		= {}

		# type
		temp.update({
			BaseSchema.BaseSchema.keyType: FloatSchema.FloatSchema.keyDataType
		})

		# require
		if require and require is True:
			temp.update({
				BaseSchema.BaseSchema.keyRequire: True
			})

		# format date string
		if format and self.__findTimeFormat(format):
			temp.update({
				DateTimeSchema.DateTimeSchema.keyTime: True
			})

		# return the element value
		return temp
