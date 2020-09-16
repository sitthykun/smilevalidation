"""
Author: masakokh
Version: 1.0.0
Note:
"""
import re
from typing import Any
import datetime
from smilevalidation.rule.BaseRule import BaseRule
from smilevalidation.schema.DateTimeSchema import DateTimeSchema


class DateRule(BaseRule):
	"""

	"""

	def __init__(self, element: dict, require: bool= None, formatDate: str= None):
		"""

		:param element:
		:param require:
		:param formatDate:
		"""
		super().__init__(
			element
			, require
		)

		self.__formatDate		= formatDate

		# run validation
		self.__run()

	def __run(self) -> None:
		"""
		:return:
		"""
		# if found an error, it will stop checking other error
		# foundError	= False

		# date
		if not self.__formatDate:
			pass

		elif self.validateDate() is False:
			# add more error
			self._addError(
				DateTimeSchema.keyDate
			)

			# add in detail
			self._addErrorDetail(
				DateTimeSchema.keyErrorDetail[
					DateTimeSchema.keyDate
				]
			)

			# # found
			# foundError = True

	def validateDate(self) -> bool:
		"""

		isinstance(value, datetime.datetime):
		:return:
		"""
		try:
			if self.element[DateTimeSchema.keyRule][DateTimeSchema.keyDate] and self.getValue():
				return True

			else:
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
			if isinstance(self.getValue(), datetime.date):
				return True

			else:
				return False

		else:
			return False
