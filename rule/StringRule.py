"""
Author: masakokh
Version: 1.0.0
Note:
"""
import re
from typing import Any
from smilevalidation.rule.BaseRule import BaseRule
from smilevalidation.schema.StringSchema import StringSchema


class StringRule(BaseRule):
	"""

	"""

	def __init__(self, element: dict, require: bool= None, maxLength: int= None, minLength: int= None, regex: str= None, unicode: bool= None):
		"""

		:param element:
		:param require:
		:param maxLength:
		:param minLength:
		:param regex:
		:param unicode:
		"""
		super().__init__(
			element
			, require
		)

		self.__maxLengthValue	= maxLength
		self.__minLengthValue	= minLength

		self.__unicodeValue		= unicode

		# regular expression
		self.__regExValue		= regex

		# run validation
		self.__run()

	def __run(self) -> None:
		"""

		:return:
		"""
		# if found an error, it will stop checking other error
		foundError	= False

		# wrong type
		if self.validateType() is False:
			# add more error
			self._addError(
				StringSchema.keyType
			)
			# add in detail
			self._addErrorDetail(
				StringSchema.keyErrorDetail[
					StringSchema.keyType
				] + self.__suffixErrorMessage(type(self.getValue()), 'string', 'type')
			)

			# found
			foundError	= True

		# max
		if foundError is False:
			if not self.__maxLengthValue:
				pass

			if self.validateMaxLength() is False:
				# add more error
				self._addError(
					StringSchema.keyMaxLength
				)
				# add in detail
				self._addErrorDetail(
					StringSchema.keyErrorDetail[
						StringSchema.keyMaxLength
					] + self.__suffixErrorMessage(len(self.getValue()), self.__maxLengthValue, 'max')
				)

				# found
				foundError = True

		# min
		if foundError is False:
			if not self.__minLengthValue:
				pass

			elif self.validateMinLength() is False:
				# add more error
				self._addError(
					StringSchema.keyMinLength
				)

				# add in detail
				self._addErrorDetail(
					StringSchema.keyErrorDetail[
						StringSchema.keyMinLength
					] + self.__suffixErrorMessage(len(self.getValue()), self.__minLengthValue, 'min')
				)

				# found
				foundError = True

		# compare min and max for a valid value
		if foundError is False:
			if not self.__minLengthValue or not self.__maxLengthValue:
				pass

			elif self.validateWrongRange() is False:
				# add more error
				self._addError(
					StringSchema.keyWrongRange
				)

				# add in detail
				self._addErrorDetail(
					StringSchema.keyErrorDetail[
						StringSchema.keyWrongRange
					]
				)

				# found
				foundError = True

		# regular expression
		if foundError is False:
			if self.__regExValue is None:
				pass

			elif self.validateRegEx() is False:
				# add more error
				self._addError(
					StringSchema.keyRegEx
				)

				# add in detail
				self._addErrorDetail(
					StringSchema.keyErrorDetail[
						StringSchema.keyRegEx
					]
				)

				# found
				foundError = True

		# unicode
		if foundError is False:
			if self.__unicodeValue is None:
				pass

			elif self.validateUnicode() is False:
				# add more error
				self._addError(
					StringSchema.keyUnicode
				)

				# add in detail
				self._addErrorDetail(
					StringSchema.keyErrorDetail[
						StringSchema.keyUnicode
					]
				)

	def __suffixErrorMessage(self, givenValue: str,  ruleValue: str, flag: str) -> str:
		"""

		:param givenValue:
		:param ruleValue:
		:param flag:
		:return:
		"""
		return f'( given: {givenValue}, rule {flag}: {ruleValue})'

	def validateMaxLength(self) -> bool:
		"""
		self.element.get(self.__maxLengthKey) can default
		:return:
		"""
		try:
			if self.element[StringRule.keyRule][StringSchema.keyMaxLength] and self.getValue():
				if len(self.getValue()) <= self.__maxLengthValue:
					return True

				else:
					return False

			else:
				return False

		except KeyError as e:
			print(f'StringRule.validateMaxLength KeyError: {str(e)}')
			return False

		except Exception as e:
			print(f'StringRule.validateMaxLength KeyError: {str(e)}')
			return False

	def validateMinLength(self) -> bool:
		"""
		self.element.get(self.__minLengthKey) can default
		:return:
		"""
		try:
			if self.element[StringRule.keyRule][StringSchema.keyMinLength]:
				if len(self.getValue()) >= self.__minLengthValue:
					return True

				else:
					return False

			else:
				return False

		except KeyError as e:
			print(f'StringRule.validateMaxLength KeyError: {str(e)}')
			return False

		except Exception as e:
			print(f'StringRule.validateMaxLength KeyError: {str(e)}')
			return False

	def validateRegEx(self) -> bool:
		"""

		:return:
		"""
		return bool(
			re.search(
				self.__regExValue
				, self.getValue()
			)
		)

	def validateType(self) -> bool:
		"""

		:return:
		"""
		if self.getValue():
			if isinstance(self.getValue(), str):
				return True

			else:
				return False
		else:
			return False

	def validateUnicode(self) -> bool:
		"""

		:return:
		"""
		try:
			return bool(
				self.getValue().encode('ascii')
				# self.getValue().decode('ascii')
			)

		except UnicodeEncodeError as e:
			return False

		except Exception as e:
			return False

	def validateWrongRange(self) -> bool:
		"""

		:return:
		"""
		return self.__maxLengthValue >= self.__minLengthValue
