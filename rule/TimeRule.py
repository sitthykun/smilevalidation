"""
Author: masakokh
Version: 1.0.1
Note:
"""
import re
from typing import Any
import datetime
from smilevalidation.rule.BaseRule import BaseRule
from smilevalidation.schema.DateTimeSchema import DateTimeSchema


class TimeRule(BaseRule):
	"""

	"""
	def __init__(self, element: dict, require: bool= None, formatTime: str= None):
		"""

		:param element:
		:param require:
		:param formatTime:
		"""
		super().__init__(
			element
			, require
		)

		self.__formatTime		= formatTime

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
			self._addError(
				DateTimeSchema.keyTime
			)

			# add in detail
			self._addErrorDetail(
				DateTimeSchema.keyErrorDetail[
					DateTimeSchema.keyDate
				]
			)

			# # found
			# foundError	= True

	def validateTime(self) -> bool:
		"""

		:return:
		"""
		try:
			if self.element[DateTimeSchema.keyRule][DateTimeSchema.keyTime] and self.getValue():
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
			if isinstance(self.getValue(), datetime.time):
				return True

			else:
				return False

		else:
			return False
