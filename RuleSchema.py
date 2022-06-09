"""
Author: masakokh
Version: 1.0.0
"""
# built-in
from typing import Any
#
from rule.BoolRule import BoolRule
from rule.ComparisonRule import ComparisonRule
from rule.DateRule import DateRule
from rule.DateTimeRule import DateTimeRule
from rule.FloatRule import FloatRule
from rule.IntegerRule import IntegerRule
from rule.ListRule import ListRule
from rule.MatchRule import MatchRule
from rule.NotMatchRule import NotMatchRule
from rule.StringRule import StringRule
from rule.TimeRule import TimeRule

#
from schema.BoolSchema import BoolSchema
from schema.ComparisonSchema import ComparisonSchema
from schema.DateTimeSchema import DateTimeSchema
from schema.FloatSchema import FloatSchema
from schema.IntegerSchema import IntegerSchema
from schema.StringSchema import StringSchema


class RuleSchema:
	"""

	"""
	def __int__(self):
		"""

		:return:
		"""
		pass

	def __require(self, value: Any) -> bool:
		"""

		:param value:
		:return:
		"""
		return True if value else False

	def getDate(self, require: bool= None, regexFormat: str= None) -> dict:
		"""

		:param require:
		:param regexFormat:
		:return:
		"""
		return {}

	def getDateTime(self, require: bool= None, regexFormat: str= None) -> dict:
		"""

		:param require:
		:param regexFormat:
		:return:
		"""
		return {}

	def getFloat(self, require: bool= None, maxValue: int= None, minValue: int= None, negative: bool= None, precision: bool= None) -> dict:
		"""

		:param require:
		:param maxValue:
		:param minValue:
		:param negative:
		:param precision:
		:return:
		"""


		return {}

	def getInteger(self, require: bool= None, maxValue: int= None, minValue: int= None, negative: bool= None) -> dict:
		"""

		:param require:
		:param maxValue:
		:param minValue:
		:param negative:
		:return:
		"""
		#
		temp = dict()

		#
		if require:
			temp.update({
				IntegerSchema.keyRequire: True
			})

		#
		if maxValue:
			temp.update({
				IntegerSchema.keyMaxValue: maxValue
			})

		#
		if minValue:
			temp.update({
				IntegerSchema.keyMinValue: minValue
			})

		#
		if negative:
			temp.update({
				IntegerSchema.keyNegative: negative
			})

		#
		return temp

	def getString(self, require: bool= None, maxLength: int= None, minLength: int= None, isUnicode: bool= None, regexValue: str= None) -> dict:
		"""

		:param require:
		:param maxLength:
		:param minLength:
		:param isUnicode:
		:param regexValue:
		:return:
		"""
		return {}

	def getTime(self, require: bool= None, regexFormat: str= None) -> dict:
		"""

		:param require:
		:param regexFormat:
		:return:
		"""
		return {}
