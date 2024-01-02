"""
Author: masakokh
Version: 1.0.1
Note:
"""
# built-in
from typing import Any

from Console import Console
from InvalidTypeList import InvalidTypeList
# internal
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
		# private
		self.__maxValueValue	= maxValue
		self.__minValueValue	= minValue
		self.__negative			= negative

	def run(self) -> None:
		"""

		:return:
		"""
		#
		super().run()
		# if found an error, it will stop checking other error
		foundError	= False

		# max
		if not self.__maxValueValue:
			pass

		elif self.validateMaxValue() is False:
			# add more error
			self.addErrorNumber(
				InvalidTypeList.N_303
			)

			# add in detail
			self.addErrorDetail(
				NumericSchema.keyMaxValue
			)

			# found
			foundError	= True

		# min
		if foundError is False:
			if not self.__minValueValue:
				pass

			elif self.validateMinValue() is False:
				# add more error
				self.addErrorNumber(
					InvalidTypeList.N_304
				)

				# add in detail
				self.addErrorDetail(
					NumericSchema.keyMinValue
				)

				# found
				foundError	= True

		# negative
		if foundError is False:
			if not self.__negative:
				pass

			elif self.validateNegative() is False:
				# add more error
				self.addErrorNumber(
					InvalidTypeList.N_305
				)

				# add in detail
				self.addErrorDetail(
					NumericSchema.keyNegative
				)
		# must be checked if possible
		self.validateMaxMinValue()

	def validateMaxMinValue(self) -> None:
		"""

		:return:
		"""
		# both are have value
		if self.element.get(NumericSchema.keyRule).get(NumericSchema.keyMaxValue) and self.element.get(NumericSchema.keyRule).get(NumericSchema.keyMinValue):
			# min > max
			if self.element.get(NumericSchema.keyRule).get(NumericSchema.keyMaxValue) < self.element.get(NumericSchema.keyRule).get(NumericSchema.keyMinValue):
				# add more error
				self.addErrorNumber(
					InvalidTypeList.N_307
				)

				# add in detail
				self.addErrorDetail(
					'min bigger than max'
				)

	def validateMaxValue(self) -> bool:
		"""
		self.element.get(self.__maxValueKey) can default
		:return:
		"""
		try:
			# Console.output(f'rule.NumericRule.validateMaxValue: {self.element[NumericSchema.keyRule][NumericSchema.keyMaxValue]=}, {self.getValue()=}, {self.getValue() <= self.__maxValueValue}')
			if self.element[NumericSchema.keyRule][NumericSchema.keyMaxValue] and self.getValue():
				return self.getValue() <= self.__maxValueValue
			#
			return False

		except KeyError as e:
			Console.output(f'rule.NumericRule.validateMaxValue KeyError: {str(e)}')
			return False

		except Exception as e:
			Console.output(f'rule.NumericRule.validateMaxValue Exception: {str(e)}')
			return False

	def validateMinValue(self) -> bool:
		"""
		self.element.get(self.__minValueKey) can default
		:return:
		"""
		try:
			# Console.output(f'rule.NumericRule.validateMinValue: {self.element[NumericSchema.keyRule][NumericSchema.keyMinValue]=}, {self.getValue()}')
			if self.element[NumericSchema.keyRule][NumericSchema.keyMinValue] and self.getValue():
				return self.getValue() >= self.__minValueValue
			#
			return False

		except KeyError as e:
			Console.output(f'rule.NumericRule.validateMinValue KeyError: {str(e)}')
			return False

		except Exception as e:
			Console.output(f'rule.NumericRule.validateMinValue Exception: {str(e)}')
			return False

	def validateNegative(self) -> bool:
		"""

		:return:
		"""
		try:
			# Console.output(f'rule.NumericRule.validateNegative: {self.element[NumericSchema.keyValue]=}, {self.getValue()}')
			return self.getValue() and self.element[NumericSchema.keyValue] >= 0

		except KeyError as e:
			Console.output(f'rule.NumericRule.validateNegative KeyError: {str(e)}')
			return False

		except Exception as e:
			Console.output(f'rule.NumericRule.validateNegative Exception: {str(e)}')
			return False
