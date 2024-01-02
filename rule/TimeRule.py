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
from Console import Console
from InvalidTypeList import InvalidTypeList
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
		self.run()

	def run(self) -> None:
		"""

		:return:
		"""
		#
		super().run()

		# found
		found24	= False

		#24
		if self.__hour24 and self.__hour24 is True:
			found24 = True
			#
			if self.__hour12:
				# add more error
				self.addErrorNumber(
					InvalidTypeList.DT_126
				)

				# add in detail
				self.addErrorDetail(
					TimeSchema.keyHour24
				)
			#
			elif self.validateHour24() is False:
				# add more error
				self.addErrorNumber(
					InvalidTypeList.DT_121
				)

				# add in detail
				self.addErrorDetail(
					TimeSchema.keyHour24
				)
		# 12
		if self.__hour12 and self.__hour12 is True:
			#
			if found24:
				# add more error
				self.addErrorNumber(
					InvalidTypeList.DT_127
				)

				# add in detail
				self.addErrorDetail(
					TimeSchema.keyHour24
				)
			#
			elif self.validateHour12() is False:
				# add more error
				self.addErrorNumber(
					InvalidTypeList.DT_122
				)

				# add in detail
				self.addErrorDetail(
					TimeSchema.keyHour12
				)

		if self.validateMinute() is False:
			# add more error
			self.addErrorNumber(
				InvalidTypeList.DT_123
			)

			# add in detail
			self.addErrorDetail(
				TimeSchema.keyMinute
			)

		if self.validateSecond() is False:
			# add more error
			self.addErrorNumber(
				InvalidTypeList.DT_124
			)

			# add in detail
			self.addErrorDetail(
				TimeSchema.keySecond
			)

		if self.__millisecond and self.__millisecond is True:
			if self.validateMillisecond() is False:
				# add more error
				self.addErrorNumber(
					InvalidTypeList.DT_125
				)

				# add in detail
				self.addErrorDetail(
					TimeSchema.keyMillisecond
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
			# Console.output(f'TimeRule.validateHour24 KeyError: {str(e)}')
			return False

		except Exception as e:
			# Console.output(f'TimeRule.validateHour24 Exception: {str(e)}')
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
			# Console.output(f'TimeRule.validateHour12 KeyError: {str(e)}')
			return False

		except Exception as e:
			# Console.output(f'TimeRule.validateHour12 Exception: {str(e)}')
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
			# Console.output(f'TimeRule.validateMinute KeyError: {str(e)}')
			return False

		except Exception as e:
			# Console.output(f'TimeRule.validateMinute Exception: {str(e)}')
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
			#Console.output(f'TimeRule.validateSecond KeyError: {str(e)}')
			return False

		except Exception as e:
			#Console.output(f'TimeRule.validateSecond Exception: {str(e)}')
			return False

	def validateMillisecond(self) -> bool:
		"""

		:return:
		"""
		try:
			# Console.output(f'222TimeRule.validateMillisecond 222: {self.element[TimeSchema.keyRule][TimeSchema.keyMillisecond]}')
			if self.element[TimeSchema.keyRule][TimeSchema.keyMillisecond] and self.getValue()[3]:
				return bool(0 <= int(self.getValue()[3]) < 1000)
			#
			return False

		except KeyError as e:
			# Console.output(f'TimeRule.validateMillisecond KeyError: {str(e)}')
			return False

		except Exception as e:
			# Console.output(f'TimeRule.validateMillisecond Exception: {str(e)}')
			return False

	def validateType(self) -> bool:
		"""

		:return:
		"""
		if self.getValue():
			return isinstance(self.getValue(), datetime.time)
		#
		return False
