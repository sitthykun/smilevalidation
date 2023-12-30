from Validation import Validation
from RuleSchema import RuleSchema

pattern	= RuleSchema()


val	= Validation()
val.addElement(
	elementName= 'a'
	, elementValue= 93
	, rule= pattern.getInteger(
		require= True
		, maxValue= 23
		, minValue= 2
		, negative= True
	)
)

val.addElement(
	elementName= 'b'
	, elementValue= 2.3
	, rule= pattern.getFloat(
		require= True
		, maxValue= 2.1
		, minValue= 2
		, negative= False
		, precision= 1
	)
)

#
if val.isValid():
	print('is valid')
else:
	print('invalid elements')


