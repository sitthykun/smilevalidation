from Validation import Validation
from RuleSchema import RuleSchema

pattern	= RuleSchema()


val	= Validation()
val.addElement(
	elementName= 'fda'
	, elementValue= 93
	, rule= pattern.getInteger(
		require= True
		, maxValue= 23
		, minValue= 2
		, negative= True
	)
)

#
if val.isValid():
	print('is valid')
else:
	print('invalid elements')


