# Fundamental Concepts.
## Useful concepts of any programming language.

### Identifier

An identifier is a name given to objects like functions, variables, 
constants, values, etc. It helps to differentiate one object to another one.

An identifier may have letters (`A-Z, a-z`) numbers (`0-9`) or underscores (`_`) 
and it must be not initialized with a number.

Python is case sensitive, it means: lowercase in any position
differs to uppercase in any position.

_E.g._: `identifier_1` is different of `IDENTIFIER_1` and `IDENTIFIER` of 
`identifier` or `iDeNTIfiEr`.

### Keywords
Are reserved words (means that you neither give a new 
meaning to these words nor use it as an identifier).
They are used to define the syntax and structure of the programming language.

Currently Python has 35 keywords. Naturally it may, in future, has more or less.

All the keywords ─ except `True`, `False` and `None` ─ are in lowercase and they 
must be written as they are (because — as I mentioned — Python is case 
sensitive). The list of all the keywords is given below.

|       |       |       |        |       |
|-------|-------|-------|--------|-------|
| False | await | else  | import | pass  |
| None  | break | except  | in | raise   |
| True  | class | finally | is | return  |
| and   | continue | for | lambda | try  |
| as    | def | from | nonlocal | while  |
| assert | del  | global | not  | with   |
| async  | elif | if     | or   | yield  |

> If you use a code editor or IDLE, the keywords assume a different color.

### Statement
Instructions (what you type/code) that the interpreter of the programming 
language can execute _are called statements._

#### Multi-line statement
In Python, the end of a statement is marked by a newline (character). But we 
can make a statement extend over multiple lines with the line continuation 
character (`\`). For example:

```Python
a = 1 + 2 + 3 \
  + 4 + 5 + 6 \
  + 7 + 8 + 9
```
We can also put multiple statements in a single line using semicolons, as follows:

```Python
a = 7; b = 21; c = 37
```
### Indentation
A code snippet (instructions of a complex statement) starts with indentation 
and ends with the first unindented instruction.

Generally four whitespaces are used for indentation and are preferred over
tabs, accordingly with 
[PEP 8 (8th Python Enhancement Proposals)](https://www.python.org/dev/peps/pep-0008/), 
please read it — the code style that I will teach you along the classes.

_E.g._:

```Python
<type_of_complex_statement_or_declaration> <some_condition_or_identifier>:
    # <Intruction 1>    The <> means this part is mandatory.
    # [Intruction 2]    The [] means this part is optional.
    # [Intruction 3]
    # [Intruction 4]

    # [Intruction 5]
    # [Intruction 6]
    # [Intruction 7]
    # [Intruction 8]
```
### Comments

Comments are very important while writing a program. They describe what is 
going on inside a program, so that a developer looking at the source code (the
code that we ─ software developers ─ type) will not have a hard time figuring 
it out.

> _Generally_ we use comments on a complex instruction.

In Python, we use the hash (`#`) symbol to start writing a comment.

It extends up to the newline character. Comments are for programmers to 
better understand a program. Python Interpreter (is a program that translate 
our code ─ source code ─ to machine code) ignores comments.

### Docstrings

Python docstrings (documentation strings) are the string literals that 
appear right after the definition of a function, method, class, or module.

Triple quotes are used while writing docstrings.

```Python
def function(parameter):
    """Function that needs a only one parameter to work."""
    return parameter
```
### Variables

Are an interval in memory, which stores an object¹, _i.e._, a structured data²
and only exists at run time, and is also associated with identifiers during 
software development.

¹ Objects are structuries that allow you to store multiple values, which are 
associated with properties, in a single variable. In order for them to be 
easily accessed later in the code.

² For the programming language which allocated that data.

#### Assignment operator (`=`)

In Python, use the assignment operator (`=`) to assign a value to a variable
associated with an identifier.

Python is a type-inferred language ("Type inference refers to the automatic 
detection of the data type of an expression in a programming language." 
─ Wikipedia).

On your Text/Code Editor, write:

```Python
# You read ─ pythonista receives the string literal.
# You are learning the Python programming language.

pythonista = "You are learning the Python programming language."
print(pythonista)
```
On the first line of the script² you instantiate (in Object Oriented Programming 
you will know what this term means) a string.

² Script means that the language is interpreted.

### Types of programming languages.

#### **Untyped programming languages or Assembly languages**.

Are languages which not have a specific type for its variables...

#### **Interpreted**.

Are languages that uses an interpreter to execute your statements.
It execute the instruction that is requested at a specific time, it means if a 
instruction ─ even though having an error ─ which never be requested 
will never be executated.

The advantage in this type is ─ in development time ─ it is very faster 
than compiled.

> It is expected that you test your code before to distribute it.

#### **Compiled**.

Are languages that creates a machine code ³.

³ Machine code means that the compiler creates a code that only the kernel of the
operating system can understand, and all the statements will be executed. So in 
development time it will be more slow than interpreted, but in run time it will
be very faster than interpreted, because the interpreter will not be necessary
(we have the machine code, so we do not need to translate the source code, 
machine code is the code which the kernel/machine understands).

#### **Typed programming languages**.

Are languages which uses variables with specific type.

#### **Strongly typed**.

Means, the data type of the variable is very important to the language, 
hence all the variables have a specific type.

#### **Weakly typed**.

In contrast — in this case — the data type is not important to the language
(but — very surely — for you while coder it is very important).

#### **Estatically typed**.

All the variables have a data type and this variable never changes its type. 
Usually operations between different types creates an error (or exception which 
you will learn later).

#### **Dynamically typed**.

The variable may changes its data type during the execution.

## Literals.

Are values not assigned to identifiers.

## Primitive types.

Are the types defined in the language.

### Numeric.

- Integers — often, `int` — represent the integer number field.
```Python
integer_1 = 0b1010  # Binary Literals
integer_2 = 100     # Decimal Literal 
integer_3 = 0o310   # Octal Literal
integer_4 = 0x12c   # Hexadecimal Literal
```

- Float — often, `float` — represent the real number field.
```Python
real_1 = 10.5 
real_2 = 1.5e2 # Scientific notation.
```

- Complex — often, `complex` — represent the complex number field.
```Python
# j is used instead of i, because electrical engineers
# can be confused with current.
x = 3.14j
```
### Char & Strings.

A _string_ is a sequence of characters surrounded by: either 
apostrophe (`'`) or quotation (`"`) marks. 
For a multiline string use triple quotes (`"""`). 

A _character_ is a character surrounded by either 
apostrophe or quotation marks.

```Python
string = "Python, since 1997."
character = 'C'
multiline_str = """This is a multiline string 
        with more than only one line."""

# To save a literal like: Joana D'arc.

joana = "Joana d'Arc"

# Similarly, to save: Joana d"Arc.

joana = 'Joana d"Arc'

# And to "Joana" d'Arc? Use \ (backslash ─ the scape character).

joana = '"Joana" d\'Arc'

```
### Boolean

A Boolean variable must have only one value of the following: either `True` 
or `False`. </br>

In Python, `0` and `None` has the boolean value `False`, therefore any other 
value is interpreted as `True`.

### None.

We use it to specify that the variable is not accessible/defined.

```Python
some_identifier = None
```

### Collections

There are 4 (four) collections: `list`, `tuple`, `dict` and `set`.

#### Important

To understand Python well, this simple idea is crucial.

- **Mutable types:** Properly, are collections which we may change its values
without the _identifier_ change its value: a memory address.

- **Immutable types:** the identifier changes its value, therefore it will be
another instance.

#### List

List is a mutable and ordered sequence of items. It is one of the most used 
collection and is very flexible.

Declaring a list is pretty straightforward. Items separated by commas are 
enclosed within brackets `[]`.

```Python
some_list = [1, 2.37, 'Pythonista',]
```

#### Tuple

Is an ordered and immutable (_i.e._: once created cannot be modified)
sequence of items.

Tuples are used to write _read only_ data and are usually faster than lists as 
they cannot change at run time.

It is defined within parentheses `()` where its elements are separated 
by commas.

```Python
some_tuple = (5, 3.7, 1+3j, 'code', False, None,)
```

#### Indexation and slicing operations

- Indexation is used to read or retrieve a specific element of an
_ordered_ collection, the first element is in the position `0`, the second in 
the `1`, the third in the `2` and so on... An arithmetic progression defined by: 
`a_1 = 0, r = 1.`

    ```Python
    some_list = [37, "An example", 4+7j, 'J', 0.8]
    some_tuple = (0, some_identifier, "Snake means Hebi in Japanese...")

    print(some_tuple[2])    # Snake means Hebi in Japanese...
    ```

- Slicing is used to retrieve an interval of an ordered collection.
    Syntax: `[begin: end: step]` (end is not included).

    ```Python
    a = [5, 10, 15, 20, 25, 30, 35, 40]

    print(f"a[0:3] = {a[0:3]}")         # [5, 10, 15],
    print(f"a[5:] = {a[5:]}")           # [30, 35, 40].
    print(f"a[6:2:-1] = {a[6:2:-1]}")   # [35, 30, 25, 20]
    ```

#### Dictionary

Is an unordered† collection of `key: value` pairs.

† Therefore indexing has no meaning. Hence, the slicing operator `[]` 
does not work.

Dictionaries are optimized for retrieving data.

In Python, dictionaries are defined within braces `{}` with each item 
being a pair in the form `key: value`. Key must be an immutable type while
value may be any type.

```Python
some_dictionary = {1: 'value', 3.7: 2}

print(f"dict[1] = {some_dictionary[1]}")
print(f"dict[3.7] = {some_dictionary[3.7]}")

# Throws an error.
print(f"d[2] = {some_dictionary[2]}");
```

#### Set (from mathematics)

Is an unordered _collection_ of unique items (duplicates are eliminated) and 
is defined by values separated by comma inside braces `{}`.

We can perform set operations like union, intersection... On two sets.

```Python
len(s)      # Number of elements in set s (cardinality).
x in s      # Test x for membership in s.
x not in s  # Test x for non-membership in s.
s <= t      # Test whether every element in s is in t, is subset.
s >= t      # Test whether every element in t is in s, is superset.

s | t       # New set with elements from both s and t, union.
s & t       # New set with elements common to s and t, intersection.
s - t       # New set with elements in s but not in t, difference.
s ^ t       # New set with elements in either s or t but not both.
```

## Type Conversion

The process of converting the value of one data type (integer, float, complex,
etc...) to another data type is called type conversion. Python has two types 
of type conversion.

- **Implicit Type Conversion** ─ Python always converts smaller data types to 
larger data types in order to avoid the loss of data.

    In this case, Python interpreter automatically converts one data type to 
    another data type. You do not need to involve yourself for this happen.

- **Explicit Type Conversion** ─ Typecasting (because you will casts (change) 
the data type of the objects).

    ```Python
    [required_datatype](expression) # Syntax

    # Example

    number_in_text = "37"           # This is a str.
    number = int(number_in_text)    # This is an integer.
    ```

### Convertion between sequencies.

```Python
set([1, 2, 3])    # {1, 2, 3},
tuple({7, 8, 9})  # (7, 8, 9),

string = 'hello'
list(string)    # ['h', 'e', 'l', 'l', 'o'].
```
> For dictionaries, each sequency must have a pair:

```Python
dict(   # {1: 2, 3: 4}
    [
        [1, 2], 
        [3, 4]
    ]
)

dict(   # {3: 26, 4: 44}
    [
        (3, 26), 
        (4, 44)
    ]
)
```

## Output

Probably you already realized that this words `print(f"")` allows us to print 
values on the screen (standard output) also we may print it on a file
(I will teach you later).

```Python
print("Hello world!")
```
The default settings of the `print()` function is:

`print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`

`objects` are the value(s) to be printed.

The `sep` parameter is used between the values. It defaults into a 
space character.

After all values are printed, `end` is printed. It defaults into a new line.

The file is the object where the values are printed and its default value is 
`sys.stdout` (screen).

The `flush` is used to buffer the file.

Buffer means saving the output until the character newline: `\n` be found. 
When it is found everything ─ at once ─ will be printed.

Some examples:

```Python
print(1, 2, 3, 4)                       # 1 2 3 4
print(1, 2, 3, 4, sep=' - ')            # 1 - 2 - 3 - 4
print(1, 2, 3, 4, sep=', ', end='.')    # 1, 2, 3, 4.
```

### Formatting the output

Sometimes we would like to format our output to make it look elegant. 
This can be done by using the `str.format()` method (or `f""`). 

```Python
x = 5
y = 10

print('The value of x is {} and y is {}.'.format(x,y))
# The value of x is 5 and y is 10.

# Or, more classy.

print(f"The value of x is {x} and y is {y}.")
# The value of x is 5 and y is 10.
# Also, you may type an expression inside the curly braces.
```

Curly braces `{}` are used as placeholders. We can specify the order 
in which they are printed by using indexes.

```Python
print('I adore {0} and {1}.'.format('coffee with milk', 'music'))
print('I adore {1} and {0}.'.format('coffee with milk', 'music'))

# I adore coffee with milk and music.
# I adore music and coffee with milk.
```

## Input

All of the examples are static programs, the value of variables was defined 
into the source code.

To take input from the user. In Python, we use the `input()` function.

`input([prompt])`

where `prompt` is the string we wish to display on the screen. It is optional.

`input('Type something: ')`

the return of input function is a string. So, usually we perform typecast.

## Import

When our program grows bigger, it is a good idea to break it into especific modules.

A module is a Python script (a `file.py`).

Definitions inside a module can be imported to another one or for the 
interactive interpreter using the keyword `import`. 

```Python
import math

print(math.pi)
```

Now all the definitions inside `math` module are available in our script. 
We can also import some specific attributes and functions only, using the 
`from` keyword.

```Python
from math import pi
pi
```

Python looks at several places defined in `sys.path`: if you want to see them 
type the code below.

```Python
import sys

sys.path
```
You may also add your own location to the list.
