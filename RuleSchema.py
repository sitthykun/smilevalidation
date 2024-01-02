"""
Author: masakokh
Version: 1.0.0
"""
# built-in
import re
from typing import Any
#
# from rule.BoolRule import BoolRule
# from rule.ComparisonRule import ComparisonRule
# from rule.DateRule import DateRule
# from rule.DateTimeRule import DateTimeRule
# from rule.FloatRule import FloatRule
# from rule.IntegerRule import IntegerRule
# from rule.ListRule import ListRule
# from rule.MatchRule import MatchRule
# from rule.NotMatchRule import NotMatchRule
# from rule.StringRule import StringRule
from rule.TimeRule import TimeRule

#
# from schema.BoolSchema import BoolSchema
# from schema.ComparisonSchema import ComparisonSchema
# from schema.DateTimeSchema import DateTimeSchema
from schema.DateSchema import DateSchema
from schema.FloatSchema import FloatSchema
from schema.IntegerSchema import IntegerSchema
from schema.StringSchema import StringSchema
from schema.TimeSchema import TimeSchema


class RuleSchema:
	"""

	"""
	def __int__(self):
		"""

		:return:
		"""
		pass

	# the default args are month and day
	# def getDate(self, require: bool= None, year4: bool= None, year2: bool= None, month: bool= None, day: bool= None) -> dict:
	def getDate(self, require: bool= None, year4: bool= None, year2: bool= None, month: bool= True, day: bool= True) -> dict:
		"""

		:param require:
		:param year4:
		:param year2:
		:param month:
		:param day:
		:return:
		"""
		# MINYEAR <= year <= MAXYEAR,
		# 1 <= month <= 12,
		# 1 <= day <= number of days in the given month and year,
		# 0 <= hour < 24,
		# 0 <= minute < 60,
		# 0 <= second < 60,
		# 0 <= microsecond < 1000000,
		# fold in [0, 1].
		#
		temp = dict()

		# add key type
		temp.update({
			DateSchema.keyType: DateSchema.keyDataType
		})

		#
		if require and require is True:
			temp.update({
				DateSchema.keyRequire: require
			})

		#
		if year4 and year4 is True:
			temp.update({
				DateSchema.keyYear4: year4
			})

		#
		if year2 and year2 is True and year4 is False:
			temp.update({
				DateSchema.keyYear2: year2
			})

		#
		if month and month is True:
			temp.update({
				DateSchema.keyMonth: month
			})

		#
		if day and day is True:
			temp.update({
				DateSchema.keyDay: day
			})

		#
		return temp

	def getDateTime(self, require: bool= None, regexFormat: str= None) -> dict:
		"""

		:param require:
		:param regexFormat:
		:return:
		"""
		return {}

	def getFloat(self, require: bool= False, maxValue: float= None, minValue: float= None, negative: bool= None, precision: int= None) -> dict:
		"""

		:param require:
		:param maxValue:
		:param minValue:
		:param negative:
		:param precision:
		:return:
		"""
		#
		temp = dict()

		# add key type
		temp.update({
			FloatSchema.keyType: FloatSchema.keyDataType
		})

		#
		if require:
			temp.update({
				FloatSchema.keyRequire: require
			})

		#
		if maxValue and maxValue is not None and str(maxValue).isnumeric():
			temp.update({
				FloatSchema.keyMaxValue: maxValue
			})

		#
		if minValue and minValue is not None and str(minValue).isnumeric():
			temp.update({
				FloatSchema.keyMinValue: minValue
			})

		#
		if negative and negative is True:
			temp.update({
				FloatSchema.keyNegative: negative
			})

		# max length of precision is 15
		if precision and precision is not None and str(precision).isnumeric() and (0 < precision <= 15) :
			temp.update({
				FloatSchema.keyPrecision: precision
			})

		#
		return temp

	def getInteger(self, require: bool= False, maxValue: int= None, minValue: int= None, negative: bool= None) -> dict:
		"""

		:param require:
		:param maxValue:
		:param minValue:
		:param negative:
		:return:
		"""
		#
		temp = dict()

		# add key type
		temp.update({
			IntegerSchema.keyType: IntegerSchema.keyDataType
		})

		#
		if require and require is True:
			temp.update({
				IntegerSchema.keyRequire: require
			})

		#
		if maxValue and maxValue is not None and str(maxValue).isnumeric():
			temp.update({
				IntegerSchema.keyMaxValue: maxValue
			})

		#
		if minValue and minValue is not None and str(minValue).isnumeric():
			temp.update({
				IntegerSchema.keyMinValue: minValue
			})

		#
		if negative and negative is True:
			temp.update({
				IntegerSchema.keyNegative: negative
			})

		#
		return temp

	def getString(self, require: bool= False, maxLength: int= None, minLength: int= None, isUnicode: bool= None, regexValue: str= None) -> dict:
		"""

		:param require:
		:param maxLength:
		:param minLength:
		:param isUnicode:
		:param regexValue:
		:return:
		"""
		#
		temp = dict()

		# add key type
		temp.update({
			StringSchema.keyType: StringSchema.keyDataType
		})

		#
		if require and require is True:
			temp.update({
				StringSchema.keyRequire: require
			})

		# must be positive
		if maxLength and maxLength is not None and str(maxLength).isnumeric() and maxLength > 0:
			temp.update({
				StringSchema.keyMaxLength: maxLength
			})

		# must be positive
		if minLength and minLength is not None and str(minLength).isnumeric() and minLength > 0:
			temp.update({
				StringSchema.keyMinLength: minLength
			})

		#
		if isUnicode and isUnicode is True:
			temp.update({
				StringSchema.keyUnicode: isUnicode
			})

		# regex value must be bigger than 2
		if regexValue and regexValue is not None and len(regexValue) > 2:
			temp.update({
				StringSchema.keyRegEx: regexValue
			})

		#
		return temp

	# the default args are minute and second
	# def getTime(self, require: bool= False, hour24: bool= None, hour12: bool= None, minute: bool= None, second: bool= None, millisecond: bool= None) -> dict:
	def getTime(self, require: bool= False, hour24: bool= None, hour12: bool= None, minute: bool= True, second: bool= True, millisecond: bool= None) -> dict:
		"""

		:param require:
		:param hour24:
		:param hour12:
		:param minute:
		:param second:
		:param millisecond:
		%S 00-59 second
		%M 00-59 min
		%H 00-23 hour
		%I 00-12 hour
		:return:
		"""
		#
		temp = dict()

		# add key type
		temp.update({
			TimeSchema.keyType: TimeSchema.keyDataType
		})

		#
		if require and require is True:
			temp.update({
				TimeRule.keyRequire: require
			})

		#
		if hour24 and hour24 is True:
			temp.update({
				TimeSchema.keyHour24: hour24
			})

		# include hour24 only one that allowed
		if hour12 and hour12 is True:
			temp.update({
				TimeSchema.keyHour12: hour12
			})

		#
		if minute and minute is True:
			temp.update({
				TimeSchema.keyMinute: minute
			})

		#
		if second and second is True:
			temp.update({
				TimeSchema.keySecond: second
			})

		#
		if millisecond and millisecond is True:
			temp.update({
				TimeSchema.keyMillisecond: millisecond
			})
		#
		return temp
