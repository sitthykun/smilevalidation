from Validator import Validator
from Rule import Rule

r	= Rule()
v	= Validator()
## string
# v.addElement(elementName= 'dara', elementValue= 'hello@ggfdgfsgf fgfsfgsgfs gfsdgfsgfsdgfsgfsgfs gfsgfgfsgfs gf gfsgfs gf', rule= r.getEmailOne())
#v.addElement(elementName= 'dara', elementValue= 343, rule= r.getEmailOne())
# v.addElement(elementName= 'dara', elementValue= 'value@fdd', rule= r.getEmailOne())
# v.addElement(elementName= 'dara', elementValue= 'hello@world.com', rule= r.getEmailOne())
# v.addElement(elementName= 'dara', elementValue= 'value@ccc', rule= r.getEmailTwo())
# v.addElement(elementName= 'dara', elementValue= 'value@ccc.travel', rule= r.getEmailTwo())
v.addElement(elementName= 'dara', elementValue= 'value@ccc.travel.kh', rule= r.getEmailTwo())
# v.addElement(elementName= 'dara', elementValue= 'value@ccc.info', rule= r.getEmailTwo())

## float
v.addElement(elementName= 'thyda', elementValue= 2, rule= r.getCostOne())
# v.addElement(elementName= 'thyda', elementValue= 1.0, rule= r.getCostOne())
# v.addElement(elementName= 'thyda', elementValue= 0, rule= r.getCostOne())
# v.addElement(elementName= 'thyda', elementValue= 8, rule= r.getCostOne())
# v.addElement(elementName= 'thyda', elementValue= 'gdfgfdsgsf', rule= r.getCostOne())

v.addMatchedElement(elementName1= 'm1', elementValue1='hello', elementName2='m2', elementValue2='hello2')
v.addNotMatchedElement(elementName1= 'm2', elementValue1='hello', elementName2='m1', elementValue2='hello2')



if v.isValid():
	print('All fine')
else:
	print(f'error: {v.getError()}')


if __name__	== '__main__':

	print('test')

