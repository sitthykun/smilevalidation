"""
Author: masakokh
Version: 1.0.0
Note:
"""
from typing import Any
from schema.ComparisonSchema import ComparisonSchema


class ComparisonRule:
	"""

	"""

	def __init__(self, element: dict):
		"""

		:param element:
		"""
		# element
		self.__element		= element

	def foundKey(self) -> bool:
		"""

		:return:
		"""
		if self.__element.get(ComparisonSchema.keyMatch):
			return True
		else:
			return False
