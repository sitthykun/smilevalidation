"""
Author: masakokh
Version: 1.0.0
Note:
"""
from typing import Any
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
		self.__run()

	def __run(self) -> None:
		"""

		:return:
		"""
		# if found an error, it will stop checking other error
		foundError	= False

		# type
		if self.validateType() is False:
			self._addError(
				FloatSchema.keyType
			)

			# found
			foundError	= True

		# precision or tail
		if foundError or self.__precisionValue is None:
			pass
		elif self.validatePrecision() is False:
			self._addError(
				FloatSchema.keyPrecision
			)

	def validatePrecision(self) -> bool:
		"""
		pending algorithm
		:return:
		"""
		if self.getValue():
			return self.__precisionValue
		else:
			return self.__precisionValue

	def validateType(self) -> bool:
		"""

		:return:
		"""
		if self.getValue():
			if isinstance(self.getValue(), int) or isinstance(self.getValue(), float):
				return True
			else:
				return False
		else:
			return False
