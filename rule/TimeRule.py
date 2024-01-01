"""
Author: masakokh
Version: 1.0.1
Note:
"""
# built-in
import datetime
import re
from typing import Any
# internal
from rule.BaseRule import BaseRule
from schema.TimeSchema import TimeSchema


class TimeRule(BaseRule):
	"""

	"""
	def __init__(self, element: dict, require: bool= None, hour24: bool= None, hour12: bool= None, minute: bool= None, second: bool= None, millisecond: bool= None):
		"""

		:param element:
		:param require:
		:param hour24:
		:param hour12:
		:param minute:
		:param second:
		:param millisecond:
		"""
		super().__init__(
			element
			, require
		)

		#
		self.__hour24       = hour24
		self.__hour12       = hour12
		self.__minute       = minute
		self.__second       = second
		self.__millisecond  = millisecond

		# run validation
		self.__run()

	def __run(self) -> None:
		"""

		:return:
		"""
		# if found an error, it will stop checking other error
		# foundError	= False

		# wrong type
		if self.validateType() is False:
			# add more error
			self._addErrorNumber(
				TimeSchema.keyDataType
			)

			# add in detail
			self._addErrorDetail(
				TimeSchema.keyErrorDetail[
					TimeSchema.keyDataType
				]
			)

			# # found
			# foundError	= True
		elif self.validateHour24() is False:
			# add more error
			self._addErrorNumber(
				TimeSchema.keyHour24
			)

			# add in detail
			self._addErrorDetail(
				TimeSchema.keyErrorDetail[
					TimeSchema.keyHour24
				]
			)

		elif self.validateHour12() is False:
			# add more error
			self._addErrorNumber(
				TimeSchema.keyHour12
			)

			# add in detail
			self._addErrorDetail(
				TimeSchema.keyErrorDetail[
					TimeSchema.keyHour12
				]
			)

		elif self.validateMinute() is False:
			# add more error
			self._addErrorNumber(
				TimeSchema.keyMinute
			)

			# add in detail
			self._addErrorDetail(
				TimeSchema.keyErrorDetail[
					TimeSchema.keyMinute
				]
			)

		elif self.validateSecond() is False:
			# add more error
			self._addErrorNumber(
				TimeSchema.keySecond
			)

			# add in detail
			self._addErrorDetail(
				TimeSchema.keyErrorDetail[
					TimeSchema.keySecond
				]
			)

		elif self.validateMillisecond() is False:
			# add more error
			self._addErrorNumber(
				TimeSchema.keyMillisecond
			)

			# add in detail
			self._addErrorDetail(
				TimeSchema.keyErrorDetail[
					TimeSchema.keyMillisecond
				]
			)

	def validateHour24(self) -> bool:
		"""

		:return:
		"""
		try:
			if self.element[TimeSchema.keyRule][TimeSchema.keyHour24] and self.getValue()[0]:
				return bool(0 <= int(self.getValue()[0]) <= 23)
			#
			return False

		except KeyError as e:
			return False

		except Exception as e:
			return False

	def validateHour12(self) -> bool:
		"""

		:return:
		"""
		try:
			if self.element[TimeSchema.keyRule][TimeSchema.keyHour12] and self.getValue()[0]:
				return bool(0 <= int(self.getValue()[0]) <= 12)
			#
			return False

		except KeyError as e:
			return False

		except Exception as e:
			return False

	def validateMinute(self) -> bool:
		"""

		:return:
		"""
		try:
			if self.element[TimeSchema.keyRule][TimeSchema.keyMinute] and self.getValue()[1]:
				return bool(0 <= int(self.getValue()[0]) <= 59)
			#
			return False

		except KeyError as e:
			return False

		except Exception as e:
			return False

	def validateSecond(self) -> bool:
		"""

		:return:
		"""
		try:
			if self.element[TimeSchema.keyRule][TimeSchema.keySecond] and self.getValue()[2]:
				return bool(0 <= int(self.getValue()[2]) <= 59)
			#
			return False

		except KeyError as e:
			return False

		except Exception as e:
			return False

	def validateMillisecond(self) -> bool:
		"""

		:return:
		"""
		try:
			if self.element[TimeSchema.keyRule][TimeSchema.keyMillisecond] and self.getValue()[3]:
				return bool(0 <= int(self.getValue()[3]) < 1000)
			#
			return False

		except KeyError as e:
			return False

		except Exception as e:
			return False

	def validateType(self) -> bool:
		"""

		:return:
		"""
		if self.getValue():
			return isinstance(self.getValue(), datetime.time)
		else:
			return False
