from Rule import Rule as ValidationRule
from Validator import Validator

rule			= ValidationRule()
validator		= Validator()

# validator.addElement('aa', 'masako', rule.getEmailOne())
# validator.addElement('bb', 12213, rule.getEmailTwo())
# validator.addElement('hello', 23.34, rule.getCurrencyOne())
# validator.addNotMatchedElement('cc', 'masako', 'aa', 'masako')
# validator.addMatchedElement('cc', 'masako2', 'aa', 'masako')
# validator.addElement('a2', '344', rule.getCurrencyOne())
validator.addElement('a3', 5654.90, rule.getCurrencyOne())
validator.addElement('a4', -1, rule.getCurrencyOne())

# validator.addElementList()

# print(validator.getElement())
# print(validator.getError())

if validator.isValid():
	print(f'3333333 Valid')
else:
	print(f'4444444 invalid {validator.getError()}')


