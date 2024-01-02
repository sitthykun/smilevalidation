"""
Author: masakokh
Version: 1.2.0
"""
# built-in
from typing import Any
# internal
from Console import Console
from rule.BoolRule import BoolRule
from rule.ComparisonRule import ComparisonRule
from rule.DateRule import DateRule
from rule.DateTimeRule import DateTimeRule
from rule.FloatRule import FloatRule
from rule.IntegerRule import IntegerRule
from rule.MatchRule import MatchRule
from rule.NotMatchRule import NotMatchRule
from rule.StringRule import StringRule
from rule.TimeRule import TimeRule
from RuleSchema import RuleSchema
from schema.BaseSchema import BaseSchema
from schema.ComparisonSchema import ComparisonSchema
from schema.DateSchema import DateSchema
from schema.DateTimeSchema import DateTimeSchema
from schema.FloatSchema import FloatSchema
from schema.IntegerSchema import IntegerSchema
from schema.StringSchema import StringSchema
from schema.TimeSchema import TimeSchema


class Validation:
	"""

	"""
	def __init__(self, ):
		"""

		"""
		# element of validation
		self.__element			= {}
		self.__elementMatched	= {}
		# contain each elements' error.
		# keep only an error of all element's errors
		self.__errorElement		= {}
		self.__errorMatched		= {}
		self.__foundValid       = True

		# key
		self.__keyError			= 'error'
		# self.__keyErrorType	= 'error_type'
		# self.__keyName		= 'name'
		self.__keyErrorDetail	= 'detail'
		# public
		self.rule               = RuleSchema()

	# def __addError(self, elementName: str, elementValue: str, errorType: str, errorMessage: str) -> None:
	# 	"""
	#
	# 	:param elementName:
	# 	:param elementValue:
	# 	:param errorType:
	# 	:param errorMessage:
	# 	:return:
	# 	"""
	# 	self.__errorElement.update({
	# 		elementName: f'<{self.__keyError}>: {errorType}, <{self.__keyErrorDetail}>: {errorMessage}'
	# 	})
	def __addComparisonError(self, elementName1: str, elementValue1: Any, elementName2: str, elementValue2: Any, errorMessage: str) -> None:
		"""

		:param elementName1:
		:param elementName2:
		:param elementValue1:
		:param elementValue2:
		:param errorMessage:
		:return:
		"""
		self.__errorMatched.update({
			f'{elementName1}_{elementName2}': f'<{self.__keyErrorDetail}>: {errorMessage}'
		})

	def __addErrorNumber(self, elementName: str, elementValue: Any, errorNumber: int, errorMessage: str) -> None:
		"""

		:param elementName:
		:param elementValue:
		:param errorNumber:
		:param errorMessage:
		:return:
		"""
		self.__foundValid   = False

		#
		self.__errorElement.update({
			elementName: f'<{self.__keyError}>: {errorNumber}, <{self.__keyErrorDetail}>: {errorMessage}'
		})

	def __addNaturalElement(self, elementName: str, elementValue: Any, rule: dict) -> None:
		"""

		:param elementName:
		:param elementValue:
		:param rule:
		:return:
		"""
		self.__element.update({
			elementName : {
				BaseSchema.keyValue	: elementValue
				, BaseSchema.keyRule: rule
			}
		})

		Console.output(f'Validation.__addNaturalElement: {self.__element=}')

	def __addSplitElement(self, elementName: str, elementValue: str, rule: dict, delimiter: str) -> None:
		"""

		:param elementName:
		:param elementValue:
		:param rule:
		:return:
		"""
		try:
			self.__element.update({
				elementName : {
					BaseSchema.keyValue	: elementValue.split(delimiter)
					, BaseSchema.keyRule: rule
				}
			})

		except Exception as e:
			Console.output(f'Validation.__addSplitElement:{str(e)}')

	def __appendWithExistedError(self, key: str, newDict: dict) -> None:
		"""

		:param key:
		:param newDict:
		:return:
		"""
		# temp Switch
		temp		= {}

		# check exist to add new avoid override
		if key in self.__errorElement:
			temp.update({
				key: self.__errorElement.get(key)
			})

		# merge with new
		temp.update(newDict)

		# add to error
		self.__errorElement.update(
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
			Console.output(f'Validation.__getElementRule KeyError: {str(e)}')
			return {}

		except Exception as e:
			Console.output(f'Validation.__getElementRule Exception: {str(e)}')
			return {}

	def __getElementType(self, element: dict) -> str:
		"""

		:param element:
		:return:
		"""
		# StringSchema is type
		# by default it returns str
		try:
			return element[BaseSchema.keyRule][BaseSchema.keyType]

		except KeyError as e:
			Console.output(f'Validation.__getElementType KeyError: {element=}, {str(e)}')
			return StringSchema.keyDataType

		except Exception as e:
			Console.output(f'Validation.__getElementType Exception: {str(e)}')
			return StringSchema.keyDataType

	def addElement(self, elementName: str, elementValue: Any, rule: dict, delimiter: str= None) -> None:
		"""

		:param elementName:
		:param elementValue:
		:param rule:
		:param delimiter:
		:return:
		"""
		# the value must be string
		if delimiter and isinstance(delimiter, str):
			Console.output(f'Validation.addElement delimiter')
			self.__addSplitElement(
				elementName     = elementName
				, elementValue	= str(elementValue)
				, rule			= rule
				, delimiter     = delimiter
			)

		#
		else:
			Console.output(f'Validation.addElement no delimiter')
			self.__addNaturalElement(
				elementName		= elementName
				, elementValue	= elementValue
				, rule			= rule
			)

	# def addElementList(self, elementName: str, rule: dict) -> None:
	# 	"""
	#
	# 	:param elementName:
	# 	:param rule:
	# 	:return:
	# 	"""
	# 	pass

	def addMatchedElement(self, elementName1: str, elementValue1: Any, elementName2: str, elementValue2: Any, errorOrder: int= 2) -> None:
		"""

		:param elementName1:
		:param elementName2:
		:param elementValue1:
		:param elementValue2:
		:param errorOrder:
		:return:
		"""
		matchRule   = MatchRule(
			name1		= elementName1
			, value1	= elementValue1
			, name2		= elementName2
			, value2	= elementValue2
		)

		# verify error
		if matchRule.getErrorNumber():
			# add error once it found
			self.__addComparisonError(
				elementName1	= elementName1
				, elementValue1	= elementValue1
				, elementName2	= elementName2
				, elementValue2	= elementValue2
				, errorMessage	= matchRule.getErrorDetail()
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
		#
		noteMatchRule   = NotMatchRule(elementName1, elementValue1, elementName2, elementValue2)

		# verify error
		if noteMatchRule.getErrorNumber():
			# add error once it found
			self.__addComparisonError(
				elementName1	= elementName1
				, elementValue1	= elementValue1
				, elementName2	= elementName2
				, elementValue2	= elementValue2
				, errorMessage	= noteMatchRule.getErrorDetail()
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
		# add more
		if self.__errorMatched:
			self.__errorElement.update(self.__errorMatched)

		# return the final items
		return self.__errorElement

	def isValid(self) -> bool:
		"""

		:return:
		"""
		###########################
		# element block
		###########################
		# elementName is string
		# elementValue is dict
		for elementName, elementValue in self.__element.items():
			# get element type
			elementType		= self.__getElementType(elementValue)
			elementRule		= self.__getElementRule(elementValue)

			# date validation
			if elementType    == DateSchema.keyDataType:
				Console.output(f'Validation.isValid {elementType}')
				# require: bool= None, maxValue: int= None, minValue: int= None, negative: bool= None, precision: int= None
				temp	= DateRule(
					element     = elementValue
					, require   = True if elementRule.get(DateSchema.keyRequire) else None
					, year4     = True if elementRule.get(DateSchema.keyYear4) else None
					, year2     = True if elementRule.get(DateSchema.keyYear2) else None
					, month     = True if elementRule.get(DateSchema.keyMonth) else None
					, day       = True if elementRule.get(DateSchema.keyDay) else None
				)

				# add error
				if not temp.isValid():
					# add error once it found
					self.__addErrorNumber(
						elementName		= elementName
						, elementValue	= temp.keyValue
						, errorNumber	= temp.getErrorNumber()
						, errorMessage	= temp.getErrorDetail()
					)

			# float
			elif elementType	== FloatSchema.keyDataType:
				Console.output(f'Validation.isValid {elementType}')
				# require: bool= None, maxValue: int= None, minValue: int= None, negative: bool= None, precision: int= None
				temp	= FloatRule(
					element		= elementValue
					, require	= True if elementRule.get(FloatSchema.keyRequire) else None
					, maxValue	= elementRule.get(FloatSchema.keyMaxValue) if elementRule.get(FloatSchema.keyMaxValue) else None
					, minValue	= elementRule.get(FloatSchema.keyMinValue) if elementRule.get(FloatSchema.keyMinValue) else None
					, negative	= elementRule.get(FloatSchema.keyNegative) if elementRule.get(FloatSchema.keyNegative) else None
					, precision	= elementRule.get(FloatSchema.keyPrecision) if elementRule.get(FloatSchema.keyPrecision) else None
				)

				# add error
				if not temp.isValid():
					# add error once it found
					self.__addErrorNumber(
						elementName		= elementName
						, elementValue	= temp.keyValue
						, errorNumber	= temp.getErrorNumber()
						, errorMessage	= temp.getErrorDetail()
					)

			# integer
			elif elementType	== IntegerSchema.keyDataType:
				Console.output(f'Validation.isValid {elementType}')
				# require: bool= None, maxValue: int= None, minValue: int= None, negative: bool= None, precision: int= None
				temp	= IntegerRule(
					element		= elementValue
					, require	= True if elementRule.get(IntegerSchema.keyRequire) else None
					, maxValue	= elementRule.get(IntegerSchema.keyMaxValue) if elementRule.get(IntegerSchema.keyMaxValue) else None
					, minValue	= elementRule.get(IntegerSchema.keyMinValue) if elementRule.get(IntegerSchema.keyMinValue) else None
					, negative	= elementRule.get(IntegerSchema.keyNegative) if elementRule.get(IntegerSchema.keyNegative) else None
				)

				Console.output(f'Validation.isValid {temp.keyValue=}, {temp.getErrorNumber()=}, {elementValue=}, {elementValue[temp.keyValue]=}, {elementName=}, {elementRule.get(IntegerSchema.keyMaxValue)=}, {temp.isValid()=}')
				# add error
				if not temp.isValid():
					# add error once it found
					self.__addErrorNumber(
						elementName		= elementName
						, elementValue	= elementValue[temp.keyValue]
						, errorNumber	= temp.getErrorNumber()
						, errorMessage	= temp.getErrorDetail()
					)

			# string validation
			elif elementType == StringSchema.keyDataType:
				Console.output(f'Validation.isValid {elementType}')
				# check unicode or literal string
				# require: bool= None, maxLength: int= None, minLength: int= None, regex: str= None,  unicode: bool= None
				temp	= StringRule(
					element		= elementValue
					, require	= True if elementRule.get(StringSchema.keyRequire) else None
					, maxLength	= elementRule.get(StringSchema.keyMaxLength) if elementRule.get(StringSchema.keyMaxLength) else None
					, minLength	= elementRule.get(StringSchema.keyMinLength) if elementRule.get(StringSchema.keyMinLength) else None
					, regex		= elementRule.get(StringSchema.keyRegEx) if elementRule.get(StringSchema.keyRegEx) else None
					, unicode	= elementRule.get(StringSchema.keyUnicode) if elementRule.get(StringSchema.keyUnicode) else None
				)

				# add error
				if not temp.isValid():
					# add error once it found
					self.__addErrorNumber(
						elementName		= elementName
						, elementValue	= temp.keyValue
						, errorNumber	= temp.getErrorNumber()
						, errorMessage	= temp.getErrorDetail()
					)

			# time
			elif elementType    == TimeSchema.keyDataType:
				Console.output(f'Validation.isValid {elementType}')
				# require: bool= None, maxValue: int= None, minValue: int= None, negative: bool= None, precision: int= None
				temp	= TimeRule(
					element		    = elementValue
					, require	    = True if elementRule.get(TimeSchema.keyRequire) else None
					, hour24        = True if elementRule.get(TimeSchema.keyHour24) else None
					, hour12        = True if elementRule.get(TimeSchema.keyHour12) else None
					, minute        = True if elementRule.get(TimeSchema.keyMinute) else None
					, second        = True if elementRule.get(TimeSchema.keySecond) else None
					, millisecond   = True if elementRule.get(TimeSchema.keyMillisecond) else None
				)

				# add error
				if not temp.isValid():
					# add error once it found
					self.__addErrorNumber(
						elementName		= elementName
						, elementValue	= temp.keyValue
						, errorNumber	= temp.getErrorNumber()
						, errorMessage	= temp.getErrorDetail()
					)
		# if it has error, it will return true
		return self.__foundValid

	def setRule(self, rule: Any) -> None:
		"""

		:param rule:
		:return:
		"""
		self.rule   = rule
