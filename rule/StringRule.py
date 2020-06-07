"""
Author: masakokh
Version: 1.0.0
Note:
"""
import re
from typing import Any
from rule.BaseRule import BaseRule
from schema.StringSchema import StringSchema


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
			self._addError(
				StringSchema.keyType
			)

			# found
			foundError	= True

		# max
		if foundError is False:
			if self.__maxLengthValue is None:
				pass
			if self.validateMaxLength() is False:
				self._addError(
					StringSchema.keyMaxLength
				)

				# found
				foundError = True

		# min
		if foundError is False:
			if self.__minLengthValue is None:
				pass
			elif self.validateMinLength() is False:
				self._addError(
					StringSchema.keyMinLength
				)

				# found
				foundError = True

		# compare min and max for a valid value
		if foundError is False:
			if self.__minLengthValue is None or self.__maxLengthValue is None:
				pass
			elif self.validateWrongRange() is False:
				self._addError(
					StringSchema.keyWrongRange
				)

				# found
				foundError = True

		# regular expression
		if foundError is False:
			if self.__regExValue is None:
				pass
			elif self.validateRegEx() is False:
				self._addError(
					StringSchema.keyRegEx
				)

				# found
				foundError = True

		# unicode
		if foundError is False:
			if self.__unicodeValue is None:
				pass
			elif self.validateUnicode() is False:
				self._addError(
					StringSchema.keyUnicode
				)

	def validateMaxLength(self) -> bool:
		"""
		self.element.get(self.__maxLengthKey) can default
		:return:
		"""
		if self.element.get(StringSchema.keyMaxLength) and self.getValue():
			if len(self.getValue()) <= self.__maxLengthValue:
				return True
			else:
				return False
		else:
			return False

	def validateMinLength(self) -> bool:
		"""
		self.element.get(self.__minLengthKey) can default
		:return:
		"""
		if self.element.get(StringSchema.keyMinLength):
			if len(self.getValue()) >= self.__minLengthValue:
				return True
			else:
				return False
		else:
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
