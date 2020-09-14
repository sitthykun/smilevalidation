# SmileValidation
![smilevalidator](https://user-images.githubusercontent.com/227092/83977155-7da56a00-a928-11ea-9f9b-66df0791a9c6.png)

Python3 Validation in another way

I hurt enough for validating those form's elements. Time to bring a new technique type.
It's gonna solve like this way:

## Validator class
That's core class of the tool.
It contains the validation element after added element into collect and it will valid the element by called isValid()

```
from Validator import Validator

# validition instance
v	= Validator()

## float validation
# add element with  
v.addElement(
    elementName= 'computer-quantity'
    , elementValue= 2
    , rule= TypeSchema().getFloat(
			require= True
			, max= 5
			, min= 1
			, negative= False
		)
)

## start validating
# true if every element is correct
if v.isValid():
    print(f'Everything is fine')
else:
    print(f'Error: {v.getError()}')

```
## Rule class
It is the collection of what we wanna validate to those element objects. What Rule will help validation class is, make it all reusable.

Example:
```
# sample
class Rule:

    def getQuantityOne(self) -> dict:
        """
    
        :return:
        """
        return TypeSchema().getFloat(
                require= True
                , max= 5
                , min= 1
                , negative= False
        )
``` 
getQualityOne will replace previous one.

```
# sample with two elements
from Validator import Validator

# validition instance
v	= Validator()

## float validation
# add element with  
v.addElement(
    elementName= 'computer-quantity'
    , elementValue= 2
    , rule= Rule.getQuantityOne()
)

v.addElement(
    elementName= 'tv-quantity'
    , elementValue= 4
    , rule= Rule.getQuantityOne()
)

## start validating
# true if every element is correct
if v.isValid():
    print(f'Everything is fine')
else:
    print(f'Error: {v.getError()}')
```

It is available on **PyPi** store via https://pypi.org/project/SmileValidation/ \
To Support my work, please donate me via <a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/sitthykun"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a Pizza"><span style="margin-left:5px;font-size:28px !important;">Buy me a Coffee</span></a>

##### My unique slogan is:
a little developer in the big world \o/