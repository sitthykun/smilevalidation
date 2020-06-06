"""
Author: masakokh
Version: 1.0.0
Note:
"""
from typing import Any
from rule.BaseRule import BaseRule
from schema.NumericSchema import NumericSchema


class NumericRule(BaseRule):
	"""

	"""

	def __init__(self, element: dict, require: bool= None, maxValue: int= None, minValue: int= None, negative: bool= None):
		"""

		:param element:
		:param require:
		:param maxValue:
		:param minValue:
		:param negative:
		"""
		super().__init__(
			element
			, require
		)

		self.__maxValueValue	= maxValue
		self.__minValueValue	= minValue
		self.__negative			= negative

		# run validation
		self.__run()

	def __run(self) -> None:
		"""

		:return:
		"""
		# if found an error, it will stop checking other error
		foundError	= False

		# max
		if self.__maxValueValue is None:
			pass
		elif self.validateMaxValue() is False:
			self._addError(
				NumericSchema.keyMaxValue
			)

			# found
			foundError	= True

		# min
		if foundError is False:
			if self.__minValueValue is None:
				pass
			elif self.validateMinValue() is False:
				self._addError(
					NumericSchema.keyMinValue
				)

				# found
				foundError	= True

		# negative
		if foundError is False:
			if self.__negative is None:
				return True
			elif self.validateNegative() is False:
				self._addError(
					NumericSchema.keyNegative
				)

	def validateMaxValue(self) -> bool:
		"""
		self.element.get(self.__maxValueKey) can default
		:return:
		"""
		try:
			if self.element[NumericSchema.keyRule][NumericSchema.keyMaxValue] and self.getValue():
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

	def validateMinValue(self) -> bool:
		"""
		self.element.get(self.__minValueKey) can default
		:return:
		"""
		try:
			if self.element[NumericSchema.keyRule][NumericSchema.keyMinValue] and self.getValue():
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

	def validateNegative(self) -> bool:
		"""

		:return:
		"""
		try:
			if self.getValue() and self.element[NumericSchema.keyValue] >= 0:
				return True
			else:
				return False
		except KeyError as e:
			return False
		except Exception as e:
			return False
