from Validation import Validation, RuleSchema
from RuleSchema import RuleSchema
from Console import Console


val	= Validation()

# val.addElement(
# 	elementName= 'a'
# 	, elementValue= 93
# 	, rule= val.rule.getInteger(
# 		require= True
# 		, maxValue= 23
# 		, minValue= 2
# 		, negative= True
# 	)
# )

# val.addElement(
# 	elementName= 'b'
# 	, elementValue= 20
# 	, rule= val.rule.getInteger(
# 		require= True
# 		, maxValue= 23
# 		, minValue= 2
# 	)
# )
#
# val.addElement(
# 	elementName= 'b'
# 	, elementValue= 2.0
# 	, rule= val.rule.getFloat(
# 		require= True
# 		, maxValue= 2.1
# 		, minValue= 1
# 		, negative= False
# 		, precision= 1
# 	)
# )

# val.addElement(
# 	elementName= 'datereq'
# 	, elementValue= '2012-12-90'
# 	, delimiter= '-'
# 	, rule = val.rule.getDate(
# 		require= True
# 		, year4= True
# 		, month= True
# 		, day= True
# 	)
# )
#
# val.addElement(
# 	elementName= 'timereq'
# 	, elementValue= '13:24:58'
# 	, delimiter= ':'
# 	, rule= val.rule.getTime(
# 		require= True
# 		, hour24= True
# 		# , hour12= True
# 		, minute= True
# 		, second= True
# 	)
# )

val.addElement(
	elementName= 'timereq'
	, elementValue= '14:24:58'
	, delimiter= ':'
	, rule= val.rule.getTime(
		require= True
		, hour24= True
		# , hour12= True
		, minute= True
		, second= True
	)
)

val.addMatchedElement()

#
if val.isValid():
	Console.output('is valid')
else:
	Console.output(f'invalid elements: {val.getError()}')


