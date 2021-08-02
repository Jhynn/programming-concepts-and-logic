# Operators

Operators are specific characters that carry out arithmetic or logical 
computation. The value that the operator operates on is called the operand.

# Arithmetic operators

Are used to perform mathematical operations.

Operator | Meaning | Example |
---------|---------|---------|
+ | Add two operands | x + y
- | Subtract right operand from the left | x - y
* | Multiply two operands | x * y
/ | Divide left operand by the right one (returns a float) | x / y
// | Floor division - division that results into whole number | x // y
% | Modulus - remainder of the division of left operand by the right one | x % y (remainder of x/y)
** | Exponent - left operand raised to the power of right | x**y (x to the power y)

```Python
x = 7
y = 3

print(f'x + y = {x + y}')   # x + y = 10
print(f'x - y = {x - y}')   # x - y = 4
print(f'x * y = {x * y}')   # x * y = 21

print(f'x / y = {x / y}')   # 2.3333333333333335
print(f'x // y = {x // y}') # 2
print(f'x**y = {x**y}')     # 343
```

# Logical operators

Any logical operation results (and returns) a boolean value, _i.e._, either 
`True` or `False`.

`and`, `or`, `not` ─ are the logical operators.

| Operator |                      Meaning               |   Example  |
|:---------|:------------------------------------------:|-----------:|
|   `and`  | `True` if both the operands are `True`     | x `and` y  |
|   `or`   | `True` if either of the operands is `True` | x `or` y   |
|   `not`  | `True` if operand is `False`               |   `not` x  |

```Python
x = True
y = False

print(f'x and y is {x and y}')  # False
print(f'x or y is {x or y}')    # True
print(f'not x is {not x}')      # False
```

# Comparison operators

For compare values...

Any comparison operation results (and returns) a boolean value, _i.e._, either 
`True` or `False`.

| Operator | Meaning | Example  |
|:---------|:-------:|---------:|
|   `>`    | Greater than ─ `True` if left operand is greater than the right. | `x > y`
|   `<`    | Less than ─ `True` if left operand is less than the right. | `x < y`
|   `==`   | Equal to ─ `True` if both operands are equal. | `x == y`
|   `!=`   | Not equal to ─ `True` if operands are not equal. | `x != y`
|   `>=`   | Greater than or equal to ─ `True` if left operand is greater than or equal to the right. | `x >= y`
|   `<=`   | Less than or equal to ─ `True` if left operand is less than or equal to the right. | `x <= y`

```Python
x = 0
y = 4

print(f'x > y = {x > y)}'       # False
print(f'x < y = {x < y)}'       # True

print(f'x == y = {x == y}')     # False
print(f'x != y = {x != y}')     # True

print(f'x >= y = {x >= y}')     # False
print(f'x <= y = {x <= y}')     # True
```

# Bitwise operators

Bitwise operators act on operands as if they were strings of binary digits 
(bit by bit).

In the table below: Let x = 10 (0000 1010 ─ in binary) and 
y = 4 (0000 0100 ─ in binary).

| Operator | Meaning | Example | Binary    |
|:--------:|---------|:-------:|:---------:|
| `&` | Bitwise AND         | `x & y = 0`   | `0000 0000`
| `|` | Bitwise OR          | `x | y = 14`  | `0000 1110`
| `~` | Bitwise NOT         | `~x = -11`    | `1111 0101`
| `^` | Bitwise XOR         | `x ^ y = 14`  | `0000 1110`
|`>>` | Bitwise right shift | `x >> 2 = 2`  | `0000 0010`
|`<<` | Bitwise left shift  | `x << 2 = 40` | `0010 1000`

# Assignment operators
Assignment operators are used to assign values to variables.

`a = 17` (a receives 17) is a simple assignment operator that assigns the 
value 17 on the right to the variable associated with the identifier `a` 
on the left.

There are various compound operators in Python like `a += 9` that uses the 
current value of `a` and adds the value `9` on it and later assign this result 
to `a`. It is equivalent to `a = a + 9`.

Operator |  Example  | Equivalent to
---------|-----------|----------------
`=`      | `x = 5`   | `x = 5`
`+=`     | `x += 5`  | `x = x + 5`
`-=`     | `x -= 5`  | `x = x - 5`
`*=`     | `x *= 5`  | `x = x * 5`
`/=`     | `x /= 5`  | `x = x / 5`
`%=`     | `x %= 5`  | `x = x % 5`
`//=`    | `x //= 5` | `x = x // 5`
`**=`    | `x **= 5` | `x = x ** 5`
`&=`     | `x &= 5`  | `x = x & 5`
`|=`     | `x |= 5`  | `x = x | 5`
`^=`     | `x ^= 5`  | `x = x ^ 5`
`>>=`    | `x >>= 5` | `x = x >> 5`
`<<=`    | `x <<= 5` | `x = x << 5`

# Identity operators

`is` and `is not` are the identity operators in Python. They are used to check 
if two values or variables are the same.

> Let `x` = `True`

Operator | Meaning | Example
---------|----------|---------
`is`     | `True` if the operands are identical. | `x` is `True`
`is not` | `True` if the operands are not identical. | `x` is `False`

```Python
w = 5
x = 5

y = [1,2,3]
z = [1,2,3]

print(w is not x)   # False
print(y is z)       # False
```

# Membership operators
`in` and `not in` are the membership operators in Python. They are used to test
whether a value is found in a sequence (string, list, tuple, set and dictionary).

In a dictionary we may only test for presence of _key_, not the value.

Operator | Meaning | Example
---------|---------|----------
`in`     | `True` if value is found in the sequence     | `5 in x`
`not in` | `True` if value is not found in the sequence | `5 not in x`

```Python
x = 'Hello, friend...'
y = {1: 'alpha', 2: 'beta'}

print('H' in x)             # True
print('hello' not in x)     # True ─ as you know, Python is case sensitive.

print(1 in y)               # True
print('a' in y)             # False
```

> Now you able to solve the first list of exercises ─ Operators. </br>
> I ask you to resolve it, then compare your answers with mine.
