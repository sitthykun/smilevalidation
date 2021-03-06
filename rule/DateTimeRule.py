"""
Author: masakokh
Version: 1.0.0
Note:
"""
from typing import Any
from smilevalidation.rule.BaseRule import BaseRule
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
		self.__run()

	def __run(self) -> None:
		"""

		:return:
		"""
		# if found an error, it will stop checking other error
		foundError	= False

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

			# found
			foundError	= True

		# time
		if foundError is False:
			if self.__formatTime is None:
				pass

			elif self.validateTime() is False:
				# add more error
				self._addError(
					DateTimeSchema.keyTime
				)

				# add in detail
				self._addErrorDetail(
					DateTimeSchema.keyErrorDetail[
						DateTimeSchema.keyTime
					]
				)

	def validateDate(self) -> bool:
		"""

		isinstance(value, datetime.datetime):
		:return:
		"""
		try:
			if self.element[DateTimeSchema.keyRule][DateTimeSchema.keyDate] and self.getValue():
				if self.getValue() <= self.__maxValueValue:
					return True

				else:
					return False

			else:
				return False

		except KeyError as e:
			return False

		except Exception as e:
			return False

	def validateTime(self) -> bool:
		"""

		:return:
		"""
		try:
			if self.element[DateTimeSchema.keyRule][DateTimeSchema.keyTime] and self.getValue():
				if self.getValue() >= self.__minValueValue:
					return True

				else:
					return False

			else:
				return False

		except KeyError as e:
			return False

		except Exception as e:
			return False
