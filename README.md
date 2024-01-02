# SmileValidation v1.2.0
![smilevalidator](https://user-images.githubusercontent.com/227092/83977155-7da56a00-a928-11ea-9f9b-66df0791a9c6.png)

Python3 validation with a different approach.

Validating those form elements is enough to make me feel hurt. Time to bring a new technique type.

What's new v2.0.0:
- Adding RuleSchema into Validation class
- Improving rule of validation method
- Fix bugs
## Validation class
After adding elements to the collection, the core class includes a validation element that validates each element by calling IsValid().

```
from smilevalidation.Validation import Validation


# validition instance
v	= Validation()

## integer validation
# add element with  
v.addElement(
    elementName= 'computer-quantity'
    , elementValue= 2
    , rule= v.rule.getInteger(
			require= True
			, maxValue= 5
			, minValue= 1
			, negative= False
		)
)

## start validating
# true if every element is correct
if v.isValid():
    Console.output(f'Everything is fine')

else:
    Console.output(f'Error: {v.getErrorNumber()}')

```

## Comparison
For reality form validation, it does not just need validation with the value, they need also the comparison such as confirm password form. So does it? It should build for this purpose via addMatchedElement method and addNotMatchedElement. Both will validate the matched value and not matched value.
```
v.addMatchedElement(
    elementName1= 'm1'
    , elementValue1='hello'
    , elementName2='m2'
    , elementValue2='hello2'
)

v.addNotMatchedElement(
    elementName1= 'm2'
    , elementValue1='hello'
    , elementName2='m1'
    , elementValue2='hello2'
)
```
Then the IsValid() method will execute these too.

Full example:

```
# sample with two elements
from smilevalidation.Validator import Validator
from smilevalidation.Rule import Rule


# validition instance
v	= Validation()

# match element value
v.addMatchedElement(
    elementName1= 'm1'
    , elementValue1='hello'
    , elementName2='m2'
    , elementValue2='hello2'
)

v.addNotMatchedElement(
    elementName1= 'm2'
    , elementValue1='hello'
    , elementName2='m1'
    , elementValue2='hello2'
)

## start validating
# true if every element is correct
if v.isValid():
    Console.output(f'Everything is fine')

else:
    Console.output(f'Error: {v.getErrorNumber()}')
```

## Rule Reusable
Extending or overriding the existing RuleSchema port

Example:
```
from Validation import Validation, RuleSchema


class Rule2(RuleSchema):

    def getQuantityOne(self) -> dict:
        """
    
        :return:
        """
        return self.getInteger(
                require= True
                , maxValue= 5
                , minValue= 1
                , negative= False
        )
 # init
 val = Validation()
 # override the new rule
 val.setRule(rule= Rule2())
``` 
getQualityOne method will present the new rule function

```
# Two elements with Rule2 class
from smilevalidation.Validation import Validation


# validition instance
v	= Validation()
v.setRule(rule= Rule2())

## integer validation
# add element with  
v.addElement(
    elementName= 'computer-quantity'
    , elementValue= 2
    , rule= self.rule.getQuantityOne()
)

v.addElement(
    elementName= 'tv-quantity'
    , elementValue= 4
    , rule= self.rule.getQuantityOne()
)

## start validating
# true if every element is correct
if v.isValid():
    Console.output(f'Everything is fine')

else:
    Console.output(f'Error: {v.getErrorNumber()}')
```

Full example
```
# validition instance
v	= Validation()

## integer validation
# add element with  
v.addElement(
    elementName= 'computer-quantity'
    , elementValue= 2
    , rule= self.rule.getInteger(
			require= True
			, maxValue= 5
			, minValue= 1
			, negative= False
		)
)

v.addElement(
    elementName= 'tv-quantity'
    , elementValue= 4
    , rule= self.rule.getInteger(
			require= True
			, maxValue= 5
			, minValue= 1
			, negative= False
		)
)

# match element value
v.addMatchedElement(
    elementName1= 'm1'
    , elementValue1='hello'
    , elementName2='m2'
    , elementValue2='hello2'
)

v.addNotMatchedElement(
    elementName1= 'm2'
    , elementValue1='hello'
    , elementName2='m1'
    , elementValue2='hello2'
)

## start validating
# true if every element is correct
if v.isValid():
    Console.output(f'Everything is fine')

else:
    Console.output(f'Error: {v.getErrorNumber()}')

```

It is available on **PyPi** store via https://pypi.org/project/SmileValidation/ \
In order to support my work, please donate to me through <a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/sitthykun"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a Pizza"><span style="margin-left:5px;font-size:28px !important;">Buy me a Coffee</span></a>

##### My unique slogan is:
a little developer in the big world \o/