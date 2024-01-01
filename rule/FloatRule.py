"""
Author: masakokh
Version: 1.0.0
Note:
"""
# built-in
from typing import Any
# internal
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
				FloatSchema.keyType
			)

			# add in detail
			self.addErrorDetail(
				FloatSchema.keyErrorDetail[
					FloatSchema.keyType
				]
			)

			# found
			foundError	= True

		# precision or tail
		if foundError or not self.__precisionValue:
			pass

		elif self.validatePrecision() is False:
			# add more error
			self.addErrorNumber(
				FloatSchema.keyPrecision
			)

			# add in detail
			self.addErrorDetail(
				FloatSchema.keyErrorDetail[
					FloatSchema.keyPrecision
				]
			)

			# found
			foundError = True

	def validatePrecision(self) -> bool:
		"""
		pending algorithm
		:return:
		"""
		if self.getValue():
			return True

		else:
			return False

	def validateType(self) -> bool:
		"""

		:return:
		"""
		if self.getValue():
			return isinstance(self.getValue(), float) or isinstance(self.getValue(), int)
		#
		return False
