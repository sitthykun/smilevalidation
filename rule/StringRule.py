"""
Author: masakokh
Version: 1.0.0
Note:
"""
# built-in
from typing import Any
import re
# internal
from Console import Console
from InvalidTypeList import InvalidTypeList
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

		self.__isUnicode		= unicode

		# regular expression
		self.__regExValue		= regex
		# private
		self.__isValid          = True

		# run validation
		self.run()

	def run(self) -> None:
		"""

		:return:
		"""
		#
		super().run()
		# if found an error, it will stop checking other error
		foundError	= False

		# wrong type
		if self.validateType() is False:
			# add more error
			self.addErrorNumber(
				InvalidTypeList.S_203
			)
			# add in detail
			self.addErrorDetail(
				StringSchema.keyDataType
			)

			# found
			foundError	= True

		# max
		if foundError is False:
			if not self.__maxLengthValue:
				pass

			if self.validateMaxLength() is False:
				# add more error
				self.addErrorNumber(
					InvalidTypeList.S_200
				)
				# add in detail
				self.addErrorDetail(
					StringSchema.keyMaxLength
				)

				# found
				foundError = True

		# min
		if foundError is False:
			if not self.__minLengthValue:
				pass

			elif self.validateMinLength() is False:
				# add more error
				self.addErrorNumber(
					InvalidTypeList.S_201
				)

				# add in detail
				self.addErrorDetail(
					StringSchema.keyMinLength
				)

				# found
				foundError = True

		# compare min and max for a valid value
		if foundError is False:
			if not self.__minLengthValue or not self.__maxLengthValue:
				pass

			elif self.validateWrongRange() is False:
				# add more error
				self.addErrorNumber(
					InvalidTypeList.S_207
				)

				# add in detail
				self.addErrorDetail(
					StringSchema.keyWrongRange
				)

				# found
				foundError = True

		# regular expression
		if foundError is False:
			if self.__regExValue is None:
				pass

			elif self.validateRegEx() is False:
				# add more error
				self.addErrorNumber(
					InvalidTypeList.S_205
				)

				# add in detail
				self.addErrorDetail(
					StringSchema.keyRegEx
				)

				# found
				foundError = True

		# unicode
		if foundError is False:
			if self.__isUnicode is None:
				pass

			elif self.validateUnicode() is False:
				# add more error
				self.addErrorNumber(
					InvalidTypeList.S_202
				)

				# add in detail
				self.addErrorDetail(
					StringSchema.keyUnicode
				)

	def validateMaxLength(self) -> bool:
		"""
		self.element.get(self.__maxLengthKey) can default
		:return:
		"""
		try:
			if self.element[StringRule.keyRule][StringSchema.keyMaxLength] and self.getValue():
				return len(self.getValue()) <= self.__maxLengthValue
			#
			return False

		except KeyError as e:
			Console.output(f'StringRule.validateMaxLength KeyError: {str(e)}')
			return False

		except Exception as e:
			Console.output(f'StringRule.validateMaxLength KeyError: {str(e)}')
			return False

	def validateMinLength(self) -> bool:
		"""
		self.element.get(self.__minLengthKey) can default
		:return:
		"""
		try:
			#
			if self.element[StringRule.keyRule][StringSchema.keyMinLength] and self.getValue():
				return len(self.getValue()) >= self.__minLengthValue
			#
			return False

		except KeyError as e:
			Console.output(f'StringRule.validateMaxLength KeyError: {str(e)}')
			return False

		except Exception as e:
			Console.output(f'StringRule.validateMaxLength KeyError: {str(e)}')
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
			return isinstance(self.getValue(), str)
		#
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
