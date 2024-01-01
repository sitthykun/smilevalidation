"""
Author: masakokh
Version: 1.0.0
Note:
"""
# built-in
import datetime
import re
from typing import Any
# internal
from rule.BaseRule import BaseRule
from schema.DateSchema import DateSchema


class DateRule(BaseRule):
	"""

	"""

	def __init__(self, element: dict, require: bool= None, year4: bool= None, year2: bool= None, month: bool= None, day: bool= None):
		"""

		:param element:
		:param require:
		:param year4:
		:param year2:
		:param month:
		:param day:
		"""
		super().__init__(
			element
			, require
		)

		#
		self.__year4    = year4
		self.__year2    = year2
		self.__month    = month
		self.__day      = day

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

		# date
		if self.validateType() is False:
			pass

		elif self.validateYear4() is False:
			# add more error
			self.addErrorNumber(
				DateSchema.keyYear4
			)

			# add in detail
			self.addErrorDetail(
				DateSchema.keyErrorDetail[
					DateSchema.keyYear4
				]
			)

		elif self.validateYear2() is False:
			# add more error
			self.addErrorNumber(
				DateSchema.keyYear2
			)

			# add in detail
			self.addErrorDetail(
				DateSchema.keyErrorDetail[
					DateSchema.keyYear2
				]
			)

		# month
		if self.validateMonth() is False:
			# add more error
			self.addErrorNumber(
				DateSchema.keyMonth
			)

			# add in detail
			self.addErrorDetail(
				DateSchema.keyErrorDetail[
					DateSchema.keyMonth
				]
			)

		# day
		if self.validateDay() is False:
			# add more error
			self.addErrorNumber(
				DateSchema.keyDay
			)

			# add in detail
			self.addErrorDetail(
				DateSchema.keyErrorDetail[
					DateSchema.keyDay
				]
			)
			# # found
			# foundError = True

	def validateYear4(self) -> bool:
		"""

		isinstance(value, datetime.datetime):
		:return:
		"""
		try:
			# 0 is year
			if self.element[DateSchema.keyRule][DateSchema.keyYear4] and self.getValue()[0]:
				#
				return bool(0 < int(self.getValue()[0]) < 9999)
			#
			return False

		except KeyError as e:
			return False

		except Exception as e:
			return False

	def validateYear2(self) -> bool:
		"""

		isinstance(value, datetime.datetime):
		:return:
		"""
		try:
			# 0 is year
			if self.element[DateSchema.keyRule][DateSchema.keyYear4] and self.getValue()[0]:
				#
				return bool(0 < int(self.getValue()[0]) < 99)
			#
			return False

		except KeyError as e:
			return False

		except Exception as e:
			return False

	def validateMonth(self) -> bool:
		"""

		isinstance(value, datetime.datetime):
		:return:
		"""
		try:
			# 1 is month
			if self.element[DateSchema.keyRule][DateSchema.keyMonth] and self.getValue()[1]:
				#
				return bool(0 < int(self.getValue()[1]) <= 12)
			#
			return False

		except KeyError as e:
			return False

		except Exception as e:
			return False

	def validateDay(self) -> bool:
		"""

		isinstance(value, datetime.datetime):
		:return:
		"""
		try:
			# 2 is day
			if self.element[DateSchema.keyRule][DateSchema.keyDay] and self.getValue()[2]:
				#
				return bool(0 < int(self.getValue()[2]) <= 31)
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
			return isinstance(self.getValue(), datetime.date)
		#
		return False
