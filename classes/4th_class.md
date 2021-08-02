# Functions.

Just like in mathematics: Are a set of instructions to solve a particular 
problem. A function defines a scope, when you call the function all the 
instructions on its scope are executed.

The advantage of the usage of functions is that it makes the software ─ as it 
grows larger ─ more manageable, organized and clean.

Naturally, it's very clever use functions because it avoid repetition of code 
and make the same code easily reusable.

## The components of a function.

```Python
def function_name([parameter_1, parameter_2, parameter_n]):
    ['''Docstring''']
    statement_1
    [statement_2]   # The guides between [] is optional, 
    [statement_n]   # the other ones is mandatory.

    [return expression/value]
```

- The keyword `def` marks the start of the _definition_ of the function.
- The name of the function (must be unique).
- Parameters are ─ optional ─ values that we will treat inside the function.
- The colon, `:`, marks the end of the function's header.
- _Docstring_, a string that describes what the function does.
- The statements that, precisely, describes what the function does ─ them must
be in the scope of the function ─ the code itself.
- The `return` keyword, usually the last state, it returns a value or 
structure.

> Keep in mind that when the return state is executed, immediatelly the 
> interpreter goes out of the function's scope. Then go back to where
> the function was called.

## Calling functions.

> Please, keep in mind this functions because some examples will use them.

```Python
def hello():
    return 'Hello, world!'

def greet(name, part_of_the_day):
    print(f'Hello, {name}. Good {part_of_the_day}!')
```

It's very simple, realise we already did this (`print()`), we just need to 
type the function's name (and, perhaps, import the function) with proper 
parameters.

> `print()`, `input()`, `int()`, `float()`... are in the standard library which 
> is automatically imported.

> When we call the function and pass values to the parameters, 
> we call them arguments.

We may call it from another `.py` file (a python script) or the Python prompt.

```Python
greet('Lauren', 'night')    # Hello, Lauren. Good night!
hello()                     # Nothing will be printed.
print(hello())              # Hello, world!
```

## Return

The `return` may be an identifier, literal, expression (which is evaluated) 
or even nothing (just to exit from the function's scope/statements), 
_i.e._, `None`.

The `None` is returned explicitally `return None` or just `return` 
and implicitally, when the function does not have the `return` statement.

# Scope of a function

It only exits when the function is called and it's being executed, after that 
all the variables are deallocated, so we dunno have the previous values of the 
variables. When we call again the same function, all the variables are 
reallocated (probably in another memory range) and assigned to 
their identifiers.

# Types of parameters

In Python exists two types of parameters which are positional and keywords.

- Positional: Are mandatory and positional (of course).

_Exempli gratia_:
```Python
greet("Ada", "evening") # Hello, Ada. Good evening!
```

- Keyword parameters: In contrast, are optional and non-positional. 
After a keyword parameter, all the other ones must be keyword parameters too.

_E.g._:
```Python
greet(part_of_the_day='sun rise', name='Natalie') # Hello, Natalie. Good sun rise!
```

Also, you may have default values for parameters, but from this parameter
all another ones must have a default value too.

_E.g._:
```Python
def greet(name, part_of_the_day='dawn ─ cockcrow'):
    print(f'Hello, {name}. Good {part_of_the_day}!')

greet("Morgana")    # Hello, Morgana. Good dawn ─ cockcrow!
```

If you pass more or less (just in the case of the positional parameters) 
arguments, naturally, you will got an error.

> Remember: Parameter is when we don't know what is the value of the variable
> but we know its type and, then, we make treatments to generates a desirable
> result. And the argument is what the final user pass to the function. _I.e._
> _Parameter_ is for developers and _arguments_ are for the final users.

When the parameter is a collection... We use the asterisk (*) before this 
parameter. So, Python interpreter converts this collection to a tuple.
Use `for` loop to go through and retrieve the elements of the tuple.

> Remember that `tuple` is the most appropriate and fastest read-only data type.

To change the value of the other parameters you need to use the keyword type.

```Python
def greet(*names, part_of_the_day='dawn ─ cockcrow'):
    for name in names:
        print(f'Hello, {name}. Good {part_of_the_day}!')

greet('Lucy', 'Melissa', 'Victoria', 'Jennifer', 'Sterling', 
        part_of_the_day='morning')

# Hello Lucy, good morning!
# Hello Melissa, good morning!
# Hello Victoria, good morning!
# Hello Jennifer, good morning!
# Hello Sterling, good morning!
```

# Recursion

Is defining something in terms of itself. In our context, is a function that 
invoke itself.

_E.g._:

```Python
def fib(n):
    """ Fibonacci series ─ iteractive version. """
    a, b = 1, 1

    for _ in range(n-1):
        a, b = b, a + b

    return a


def fib_rec(n):
    """ Fibonacci series ─ recursive version. """
    if n < 2:   # Base condition
        return n

    return fib_rec(n-1) + fib_rec(n-2)
```

## Base condition.

Interrupts a recursion, otherwise the function calls itself until there is
no memory available on the machine.

The Python interpreter limits recursion to avoid this scenario. The limit is 
1000 recursive calls... Otherwise the interpreter throws a RecursionError.

> When you call `fib_rec(number)` it will be called `number` times.
> When `number` is less than `2` it will return itself ─ base condition.

```Python
def factorial(x):
    """Returns the factorial of an integer"""

    if x == 1:
        return 1

    return x * factorial(x-1)


factorial(3)          # 1st call with 3,
3 * factorial(2)      # 2nd call with 2,
3 * 2 * factorial(1)  # 3rd call with 1.

3 * 2 * 1             # return from 3rd call,
3 * 2                 # return from 2nd call,
6                     # return from 1st call.
```

Although recursion make the code elegant, it is expensive because it needs 
a lot of memory and time (to be processed), therefore it must be avoided.

# Lambda functions

The keyword that defines a lambda function, also knowm as anonymous function, 
is `lambda` not `def`.

```Python
lambda <parameters>: <expression>
```

They are recognized as a function, hence wherever a function is required, they
may be used too. Keep in mind that lambda functions only have an expression 
which is evaluated and returned, they may be have any number of parameters.

```Python
exponetion = lambda base, exponent: base ** exponent    # Assign and definition

exponetion(2, 10)                                       # 1024
```

> It's very used in functions like `filter()` and `map()`.

_E.g.:_ `filter(func, collection)` as the name suggests... 
Take only the items ─ inside the `collection` ─ which the `func` 
evaluateion is `True` and add it into an `iterable` (which you'll learn later).

```Python
x = [4, 6, 5, 7, 9, 8, 2, 3, 1]
y = tuple(filter(lambda x: x % 2 == 1, x))  # Only odd numbers.

print(x)
print(y)
```

_E.g.:_ `map(func, collection)` Instead of take an item... It applyes 
the `func` on all the items of the `collection`.

```Python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers = list(map(lambda x: x ** 2 , numbers))

print(squared_numbers)
```

Acecessing nonlocal variables... In nested functions, use the keyword `nonlocal`
to use nonlocal variables.

_Exempli gratia_:

```Python
def out():
    l = "local to out()"
    print(f"Original value ─ {l}")

    def inner():
        nonlocal l
        l = "nonlocal"
        print(f"Local to inner ─ {l}")

    inner()
    print(f"New value in out ─ {l}")

out()
```
