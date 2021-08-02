# Namespace
In a nutshell, is a collection of identifiers (names created by you).

Namespaces are completely independent from each other, hence we can use the 
same identifier in different namespaces or modules, _i.e._, a python file ─ our 
source code.

When we start the Python interpreter, _i.e._, when we execute our program ─ and 
while it is being executed ─ it creates a built-in namespace (_e.g._, `print()`,
`input()` belongs to this _built-in namespace_).

# Scope
The scope allow us to access variables out of our actual namespace.

On our scope we do not need to use a prefix.

When we call an identifier: it is searched¹ in the local namespace, then in the 
global namespace and finally in the built-in namespace.

¹ Actualy it is searched in the namespace where you called it and if it is not 
there, it will be searched in the another scope where the namespace (which you 
called the identifier) is inside and so on.

If there is a scope inside another different of global or built-in, it is called
nested².

² Nesting: a structure inside another one.

```Python
def outter():
    local_to_outter = 1        # It is not local to inner(),
    # but we can ─ only ─ read local_to_outter and global_id from inner().

    def inner():                
        local_to_inner = 2     # also is a nested local namespace
                               # and we can read as well as assign.

global_id = 0                  # That's the global scope.
```

If you assign, in the _inner_ namespace, a value to `global_id` or to 
`local_to_outter` actually you are instantiating (creating) a new variable, 
rememember you are in a namespace that this variables does not exist.

To do the mentioned (above), use the keyword `global`.

It's used inside only when we want to do assignments to a non-local variable.

```Python
def outter():
    global global_id 
    global_id = 1

    def inner():
        global global_id 
        global_id = 2

        print(global_id)

    inner()
    print(global_id)


global_id = 0
outter()
print(global_id)
```

# Flow control

## Conditional structuries

Often our problem has several solutions where each one is correct for a 
specific scenario.

In _Python_ we use the keywords: `if`, `elif` (short for else if) and `else`.

### **`if` statement**

#### Syntax

```Python
if expression:
    <instruction>
    [another_instruction]
```

The Python interpreter evaluate the expression and will execute the statement 
(instructions) only if the expression is `True`.

Python interprets _non-zero values_ as `True`. `None` and `0` are interpreted 
as `False`.

If the expression is `False`, the statement will not executed.

The body (scope) of the `if` statement is indicated by the indentation 
(four spaces below the `if` statement). 
The body starts with an indentation and the first unindented instruction or no
instructions mark the end of the `if` statement.

```Python
number = -3.7

print("This is always printed.")            # Independent of conditions...

if number < 0:                              # number < 0 is the condition.
    print(f"{number} is a negative number, so it belongs \
            to the field of integers.")     # Is the instruction.

number = -1

if number > 0:                              # This returns False
    print(f"{number} is a natural number.") # Therefore this is skipped.

print("I need to stress, anyway, this will be printed.")
```

> Always try to keep the lines of your code with the size of 80 characters.

### **`else` statement**

If the condition of the `if` statement (realize that the `else` statement 
depends of the existence of the `if` statement) is `False`, the scope of 
`else` will be executed.

```Python
number = float(input('Please, type a number: '))

if number > 0:
    print(f"{number} is positive.")

else:
    print(f"{number} is negative.")
```

### **The ternary operator**

It's equals to an `if... else` statement.

```Python
<on_true> if <expression> else <on_false> 

# Equals to

if <expression>:
    <on_true>

else:
    <on_false>
```

### **`elif` statement**

Allow us to check a lot of expressions (scenarios).

If the condition `if` is `False`, the interpreter will check the condition 
of the below `elif` scope and so on.

If all the conditions are `False` (on the `if` statement and the `elif` 
statements), the scope of `else` will be executed.

The `if` statement may got several `elif` statements and just _only one_ 
`else` statement.

```Python
number = float(input('Please, type a number: '))

if number > 0:
    print(f"{number} is positive.")

elif number < 0:
    print(f"{number} is negative.")

else:
    print("0 is zero!")
```

## Nested conditional (`if`, `elif` and `else`) statements

We may have a conditional statement in another one. To obtain this we just need 
to indent a conditional statement in another one.

```Python
number = float(input('Please, type a number: '))

if number != 0:
    if number > 0:
        print(f"{number} is positive.")
    
    elif number > 1_000:
        print(f"{number/1_000}K is positive.")

    else:
        print(f"{number} is negative.")

else:
    print("0 is zero!")
```

## Repetition structuries (loop)

### While loop

The `while` statement allows us to repeat a piece of code as long as the 
condition is `True`.

> The syntax of the `while` statement.

```Python
while condition:
    instruction_1   # The structions of the while statement
    instruction_n   # must be idented on it, i.e. its scope.
```

All of the instructions will be executed only if the condition is `True`.
When the last instruction is executed the condition will be evaluated again 
and if it is `False` the code will skipped to the next instruction of the same 
scope of the `while` statement otherwise the while's code (scope) will be 
executed again.

```Python
# Fibonacci series up to n.
n = int(input('Please, enter a number: '))
a, b = 0, 1

while a < n:
    print(a, end=' ')
    a, b = b, a + b
print()
```

### `for` loop

We use the `for` loop to iterate over iterable objects, some of them: 
`string, tuple, list`.

> The syntax of the `for` statement.

```Python
for element in iterable:
    instruction_1   # The structions of the for statement
    instruction_n   # must be idented on it, i.e. its scope.
```

`element` is the identifier associated with the variable that assumes each 
value of the `iterable` on each iteration, the `for` statement is ended when 
the code reaches the last item of the `iterable` and _also_ the last 
instruction.

Sometimes we need a range to solve a problem. In Python we have the built-in 
function `range(start, stop, step_size)`, a very clever function, it just 
stores the begin: `start`, end: `stop` and the reason: `step_size`.

So it do not stores all the elements, i.e., hence we avoid ─ eventually ─ the 
usage of a lot of memory. Because it just hold the current value, then it 
generates the next value (element), probably you realize that its parameters 
─ somehow ─ defines an arthmetic progression.

If we pass only one argument to the `range()` function this value will be 
assumed as the `stop` parameter, the `step_size` will be `1` and the `start` 
will be `0`, if we pass two arguments the `range()` assume them as the `start`
and `end`, respectively and the `step_size` as `1`. Evidently, if we pass 
three arguments them will be, respectively: `start, end` and `step_size`.

```Python
for element in range(17):
    print(element, end=', ')
print()

# Output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
```

Is very usual we use another built-in function called: `len()`, short for 
length, to iterate in an iterable using the correct range of its indexes.

```Python
instruments = ('cello', 'piano', 'guitar',)

# Iterating through the above tuple using indexation.
for instrument in range(len(instruments)):
	print(f'I play {instruments[instrument]}.')
```

### `break` and `continue` statements.

Are used to alter the _flow_ of _loops_.

Sometimes is needed to ─ get a better performance ─ stop the loop even the 
condition beeing `True`.

#### **`break` statement**

When this instruction is found the loop where it is inside is ended and the
interpreter goes to the next scope.

#### **`continue` statement**

This instruction perform the interpreter goes to the evaluation of the loop's 
condition.

```Python
x = int(input('Enter a number: '))

while x <= 10:
    x += 1      # Never forget to refresh the value of the counter,
                # in order to avoid a infinity loop.

    if x % 2:   # Is odd.
        continue

    print(x)

```

#### **`pass`** statement.

The `pass` statement is a statement that results in _no operation_.

We use it when we do not implemented yet some `function, class, loop, if`... 
statements.

Because the interpreter assumes as an error if one of these statements are 
void, and you must to agree with this fact, it doesn't make sense, _e.g._, an 
empty `if` statement.

### `for... else` statement.

The `for` loop's `else` part will be executed only if the `if` statement inside
of the `for` statement would be `False`.

```Python
# Finding factors for numbers between 2 to 10.
for number in range(2, 10):
    for k in range(2, number):
        if number % k == 0:
            print(f'{number} equals {k} * {int(number / k)}.')
            break   # Goes to the first loop.
    else:
        # Catching the numbers which have no factors, hence prime numbers.
        print(f'{number} is a prime number!')
```

### `while`... `else`

We also may use `while`... `else`, it is the same logic of the `for`... `else`.
