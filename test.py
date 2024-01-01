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

val.addElement(
	elementName= 'datereq'
	, elementValue= '2012-12-21'
	, delimiter= '-'
	, rule = pattern.getDate(
		require= True
		, year4= True
		, month= True
		, day= True
	)
)

val.addElement(
	elementName= 'timereq'
	, elementValue= '13:24:58'
	, delimiter= ':'
	, rule= pattern.getTime(
		require= True
		, hour24= True
		, minute= True
		, second= True
	)
)

#
if val.isValid():
	print('is valid')
else:
	print('invalid elements')


