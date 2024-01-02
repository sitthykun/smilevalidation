"""
Author: masakokh
Version: 1.0.1
Note:
"""
# built-in
from typing import Any
# internal
from rule.BaseRule import BaseRule


class ListRule(BaseRule):
	"""

	"""

	def __init__(self, element: dict, empty: bool, require: bool):
		"""

		:param element:
		:param empty:
		:param require:
		"""
		super().__init__(
			element
			, require
		)
