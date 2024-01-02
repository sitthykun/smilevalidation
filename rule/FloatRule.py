"""
Author: masakokh
Version: 1.0.1
Note:
"""
# built-in
from typing import Any
# internal
from InvalidTypeList import InvalidTypeList
from rule.NumericRule import NumericRule
from schema.FloatSchema import FloatSchema


class FloatRule(NumericRule):
	"""

	"""

	def __init__(self, element: dict, require: bool= None, maxValue: int= None, minValue: int= None, negative: bool= None, precision: int= None):
		"""

		:param element: name and value
		:param require:
		:param maxValue:
		:param minValue:
		:param negative:
		"""
		super().__init__(
			element
			, require
			, maxValue
			, minValue
			, negative
		)

		# precision
		self.__precisionValue	= precision

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

		# type
		if self.validateType() is False:
			# add more error
			self.addErrorNumber(
				InvalidTypeList.F_301
			)

			# add in detail
			self.addErrorDetail(
				FloatSchema.keyType
			)

			# found
			foundError	= True

		# precision or tail
		if foundError or not self.__precisionValue:
			pass

		elif self.validatePrecision() is False:
			# add more error
			self.addErrorNumber(
				InvalidTypeList.F_300
			)

			# add in detail
			self.addErrorDetail(
				FloatSchema.keyPrecision
			)

			# # found
			# foundError = True

	def validatePrecision(self) -> bool:
		"""
		pending algorithm
		:return:
		"""
		try:
			# case numeric to string
			# split of string to 2 values
			# check the tail if length equals the given precision
			return len(str(self.getValue()).split('.')[1]) == self.__precisionValue

		except Exception as e:
			return False

	def validateType(self) -> bool:
		"""

		:return:
		"""
		if self.getValue():
			return isinstance(self.getValue(), float) or isinstance(self.getValue(), int)
		#
		return False
