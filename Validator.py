"""
Author: masakokh
Version: 1.0.0
"""
from typing import Any
from rule.BoolRule import BoolRule
from rule.ComparisonRule import ComparisonRule
from rule.FloatRule import FloatRule
from rule.IntegerRule import IntegerRule
from rule.MatchRule import MatchRule
from rule.NotMatchRule import NotMatchRule
from rule.StringRule import StringRule
from schema.BaseSchema import BaseSchema
from schema.ComparisonSchema import ComparisonSchema
from schema.FloatSchema import FloatSchema
from schema.IntegerSchema import IntegerSchema
from schema.StringSchema import StringSchema


class Validator:
	"""

	"""
	def __init__(self, ):
		"""

		"""
		self.__element		= {}
		self.__error		= {}
		self.__found		= {}

		# key
		self.__keyError		= 'error'
		self.__keyErrorType	= 'error_type'
		self.__keyName		= 'name'

		# form
		self.__load()

	def __addError(self, elementName: str, elementValue: str, errorType: str, errorMessage: str) -> None:
		"""

		:param elementName:
		:param errorType:
		:param errorMessage:
		:return:
		"""
		self.__error.update({
			elementName: errorType
		})

	def __addMatchedError(self, elementName: str) -> None:
		"""

		:param elementName:
		:return:
		"""
		pass

	def __addNatureElement(self, elementName: str, elementValue: str, rule: dict) -> None:
		"""

		:param elementName:
		:param elementValue:
		:param rule:
		:return:
		"""
		self.__element.update({
			elementName : {
				BaseSchema.keyValue: elementValue
				, BaseSchema.keyRule: rule
			}
		})

	def __appendWithExistedError(self, key: str, newDict: dict) -> None:
		"""

		:param key:
		:param newDict:
		:return:
		"""
		# temp Switch
		temp		= {}

		# check exist to add new avoid override
		if key in self.__error:
			temp.update({
				key: self.__error.get(key)
			})

		# merge with new
		temp.update(newDict)

		# add to error
		self.__error.update(
			temp
		)

	def __getElementRule(self, element: dict) -> dict:
		"""

		:param element:
		:return:
		"""
		# StringSchema is type
		# by default it returns str
		try:
			return element[BaseSchema.keyRule]
		except KeyError as e:
			return {}
		except Exception as e:
			return {}

	def __getElementType(self, element: dict) -> str:
		"""

		:param element:
		:return:
		"""
		# StringSchema is type
		# by default it returns str
		try:
			return element[BaseSchema.keyRule][StringSchema.keyType]
		except KeyError as e:
			return StringSchema.keyDataType
		except Exception as e:
			return StringSchema.keyDataType

	def __load(self) -> None:
		"""

		:return:
		"""
		pass

	def __validate(self) -> bool:
		"""

		:return:
		"""
		return False

	def addElement(self, elementName: str, elementValue: str, rule: dict) -> None:
		"""

		:param elementName:
		:param elementValue:
		:param rule:
		:return:
		"""
		self.__addNatureElement(
			elementName
			, elementValue
			, rule
		)

	def addElementList(self, elementName: str, rule: dict) -> None:
		"""

		:param elementName:
		:param rule:
		:return:
		"""
		pass

	def addMatchedElement(self, elementName1: str, elementValue1: Any, elementName2: str, elementValue2: Any, errorOrder: int= 2) -> None:
		"""

		:param elementName1:
		:param elementName2:
		:param elementValue1:
		:param elementValue2:
		:param errorOrder:
		:return:
		"""
		if elementValue1 is not elementValue2:

			# add error to the element
			if errorOrder and errorOrder == 1:
				# update
				self.__appendWithExistedError(
					elementName1
					, {ComparisonSchema.keyMatch: True}
				)

				# add error once it found
				self.__addError(
					elementName= elementName1
					, elementValue= elementValue1
					, errorType= ComparisonSchema.keyMatch
					, errorMessage= ''
				)

			else:
				# update
				self.__appendWithExistedError(
					elementName2
					, {ComparisonSchema.keyMatch: True}
				)

				# add error once it found
				self.__addError(
					elementName= elementName2
					, elementValue= elementValue2
					, errorType= ComparisonSchema.keyMatch
					, errorMessage= ''
				)

	def addNotMatchedElement(self, elementName1: str, elementValue1: Any, elementName2: str, elementValue2: Any, errorOrder: int= 2) -> None:
		"""

		:param elementName1:
		:param elementName2:
		:param elementValue1:
		:param elementValue2:
		:param errorOrder:
		:return:
		"""
		if elementValue1 is elementValue2:

			# add error to the element
			if errorOrder and errorOrder == 1:
				# update
				self.__appendWithExistedError(
					elementName1
					, {ComparisonSchema.keyNotMatch: True}
				)

				# add error once it found
				self.__addError(
					elementName= elementName1
					, elementValue= elementValue1
					, errorType= ComparisonSchema.keyNotMatch
					, errorMessage= ''
				)

			else:
				# update
				self.__appendWithExistedError(
					elementName2
					, {ComparisonSchema.keyNotMatch: True}
				)

				# add error once it found
				self.__addError(
					elementName= elementName2
					, elementValue= elementValue2
					, errorType= ComparisonSchema.keyNotMatch
					, errorMessage= ''
				)

	def getElement(self) -> dict:
		"""

		:return:
		"""
		return self.__element

	def getError(self) -> dict:
		"""

		:return:
		"""
		return self.__error

	def isValid(self) -> bool:
		"""

		:return:
		"""
		# elementName is string
		# elementValue is dict
		for elementName, elementValue in self.__element.items():
			# get element type
			elementType		= self.__getElementType(elementValue)
			elementRule		= self.__getElementRule(elementValue)

			# string validation
			if elementType == StringSchema.keyDataType:
				# check unicode or literal string
				# require: bool= None, maxLength: int= None, minLength: int= None, regex: str= None,  unicode: bool= None
				temp	= StringRule(
					element= elementValue
					, require= True if elementRule.get(StringSchema.keyRequire) else None
					, maxLength= elementRule.get(StringSchema.keyMaxLength) if elementRule.get(StringSchema.keyMaxLength) else None
					, minLength= elementRule.get(StringSchema.keyMinLength) if elementRule.get(StringSchema.keyMinLength) else None
					, regex= elementRule.get(StringSchema.keyRegEx) if elementRule.get(StringSchema.keyRegEx) else None
					, unicode= elementRule.get(StringSchema.keyUnicode) if elementRule.get(StringSchema.keyUnicode) else None
				)

				# add error
				if temp.getError():
					# add error once it found
					self.__addError(
						elementName= elementName
						, elementValue= temp.keyValue
						, errorType= temp.getError()
						, errorMessage= ''
					)

			elif elementType	== FloatSchema.keyDataType:
				# require: bool= None, maxValue: int= None, minValue: int= None, negative: bool= None, precision: int= None
				temp = FloatRule(
					element= elementValue
					, require= True if elementRule.get(FloatSchema.keyRequire) else None
					, maxValue= elementRule.get(FloatSchema.keyMaxValue) if elementRule.get(FloatSchema.keyMaxValue) else None
					, minValue= elementRule.get(FloatSchema.keyMinValue) if elementRule.get(FloatSchema.keyMinValue) else None
					, negative= elementRule.get(FloatSchema.keyNegative) if elementRule.get(FloatSchema.keyNegative) else None
					, precision= elementRule.get(FloatSchema.keyPrecision) if elementRule.get(FloatSchema.keyPrecision) else None
				)

				# add error
				if temp.getError():
					# add error once it found
					self.__addError(
						elementName= elementName
						, elementValue= temp.keyValue
						, errorType= temp.getError()
						, errorMessage= ''
					)

			elif elementType	== IntegerSchema.keyDataType:
				# require: bool= None, maxValue: int= None, minValue: int= None, negative: bool= None, precision: int= None
				temp = IntegerRule(
					element= elementValue
					, require= True if elementRule.get(IntegerSchema.keyRequire) else None
					, maxValue= elementRule.get(IntegerSchema.keyMaxValue) if elementRule.get(IntegerSchema.keyMaxValue) else None
					, minValue= elementRule.get(IntegerSchema.keyMinValue) if elementRule.get(IntegerSchema.keyMinValue) else None
					, negative= elementRule.get(IntegerSchema.keyNegative) if elementRule.get(IntegerSchema.keyNegative) else None
				)

				# add error
				if temp.getError():
					# add error once it found
					self.__addError(
						elementName= elementName
						, elementValue= temp.keyValue
						, errorType= temp.getError()
						, errorMessage= ''
					)

		# if has error, it will return true
		return not bool(
			self.getError()
		)
