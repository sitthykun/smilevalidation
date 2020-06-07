"""
Author: masakokh
Version: 1.0.0
"""
from typing import Any
from rule import *
from schema import BaseSchema, ComparisonSchema, FloatSchema, IntegerSchema, StringSchema


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

	def getFloat(self, require: bool= None, max: int= None, min: int= None, precision: int= None) -> dict:
		"""

		:param require:
		:param max:
		:param min:
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

		# precision
		if precision:
			temp.update({
				FloatSchema.FloatSchema.keyPrecision: precision
			})

		# return the element value
		return temp

	def getInteger(self, require: bool= None, max: int= None, min: int= None) -> dict:
		"""

		:param require:
		:param max:
		:param min:
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
