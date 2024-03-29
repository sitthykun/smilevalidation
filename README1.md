# SmileValidation v1.1.0
![smilevalidator](https://user-images.githubusercontent.com/227092/83977155-7da56a00-a928-11ea-9f9b-66df0791a9c6.png)

Python3 Validation in another way

I hurt enough for validating those form's elements. Time to bring a new technique type.
It's going to solve like this way:

What's new v1.1.0:
- h
- c
## Validator class
That's core class of the tool.
It contains the validation element after added element into collect and it will valid the element by called isValid()

```
from smilevalidation.Validator import Validator


# validition instance
v	= Validator()

## integer validation
# add element with  
v.addElement(
    elementName= 'computer-quantity'
    , elementValue= 2
    , rule= TypeSchema().getInteger(
			require= True
			, max= 5
			, min= 1
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
For reality form validation, it does not just need validation with the value, they need also the comparison such as confirm password form.
So does it?
It should build for this purpose via addMatchedElement method and addNotMatchedElement. Both will validation matched value and not matched value.
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
Then the isValid() method will execute these too.

Full example:

```
# sample with two elements
from smilevalidation.Validator import Validator
from smilevalidation.Rule import Rule

# validition instance
v	= Validator()

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
If you wanna use a rule to another addition, we can create a rule class as the collection of what we wanna validate to those element objects.

Example:
```
# sample
class Rule:

    def getQuantityOne(self) -> dict:
        """
    
        :return:
        """
        return TypeSchema().getInteger(
                require= True
                , max= 5
                , min= 1
                , negative= False
        )
``` 
getQualityOne will replace previous one.

```
# sample with two elements
from smilevalidation.Validator import Validator
from smilevalidation.Rule import Rule

# validition instance
v	= Validator()

## integer validation
# add element with  
v.addElement(
    elementName= 'computer-quantity'
    , elementValue= 2
    , rule= Rule().getQuantityOne()
)

v.addElement(
    elementName= 'tv-quantity'
    , elementValue= 4
    , rule= Rule().getQuantityOne()
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
v	= Validator()

## integer validation
# add element with  
v.addElement(
    elementName= 'computer-quantity'
    , elementValue= 2
    , rule= TypeSchema().getInteger(
			require= True
			, max= 5
			, min= 1
			, negative= False
		)
)

v.addElement(
    elementName= 'tv-quantity'
    , elementValue= 4
    , rule= TypeSchema().getInteger(
			require= True
			, max= 5
			, min= 1
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
To Support my work, please donate me via <a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/sitthykun"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a Pizza"><span style="margin-left:5px;font-size:28px !important;">Buy me a Coffee</span></a>

##### My unique slogan is:
a little developer in the big world \o/