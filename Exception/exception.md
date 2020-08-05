# Exception with function

If an exception is raised within a function and is not handled within that function, then the function is immediately exited and the calling function is checked for a handler, and so on up the function call hierarchy.

```python
def get_weight():
    weight = int(input('Enter weight (in pounds): '))
    if weight < 0:
        ## if something wrong, raise the error
        raise ValueError('Invalid weight.')
    return weight

def get_height():
    height = int(input('Enter height (in inches): '))
    if height <= 0:
        raise ValueError('Invalid height.')
    return height

user_input = ''
while user_input != 'q':
    try:
        weight = get_weight()
        height = get_height()

        bmi = (float(weight) / float(height * height)) * 703
        print('BMI:', bmi)
        print('(CDC: 18.6-24.9 normal)\n')
        # Source www.cdc.gov

    except ValueError as excpt:
        print(excpt)
        print('Could not calculate health info.\n')

    user_input = input("Enter any key ('q' to quit): ")
```









> Suppose get_weight() raises an exception of type ValueError. The get_weight() function does not handle exceptions (there is no try block in the function) so it immediately exits. Going up the function call hierarchy returns execution to the global scope script code, where the call to get_weight() was in a try block, so the exception handler for ValueError is executed.

A raise causes immediate exit, Nothing get returned by the function.

The exception handling process looks up through the function call hierachy for

an exception handler that handles the raised exception



## Finally

`Finally`

> The **finally** clause of a try statement allows a programmer to specify *clean-up* actions that are always executed.

 

- If *no exception* occurs, then execution continues in the finally clause, and then proceeds with the rest of the program.

- If a *handled exception* occurs, then an exception handler executes and then the finally clause.

- If an *unhandled exception* occurs, then the finally clause executes and then the exception is re-raised.

- The finally clause also executes if any break, continue, or return statement causes the try block to be exited.

  

```python
class ValueError(Exception):
    """ Inappropriate argument value (of correct type). """
    
class ZeroDivisionError(Exception)
```



