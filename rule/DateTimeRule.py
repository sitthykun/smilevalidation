"""
Author: masakokh
Version: 1.0.0
Note:
"""
# built-in
from typing import Any
# internal
from smilevalidation.InvalidTypeList import InvalidTypeList
from smilevalidation.rule.BaseRule import BaseRule
from smilevalidation.rule.DateRule import DateRule
from smilevalidation.rule.TimeRule import TimeRule
from smilevalidation.schema.DateTimeSchema import DateTimeSchema


class DateTimeRule(BaseRule):
	"""

	"""

	def __init__(self, element: dict, require: bool= None, formatDate: str= None, formatTime: str= None):
		"""

		:param element:
		:param require:
		:param formatDate:
		:param formatTime:
		"""
		super().__init__(
			element
			, require
		)

		self.__formatDate		= formatDate
		self.__formatTime		= formatTime

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
		if not self.__formatDate:
			pass
