# Exercises about operators.

Apply the theory learned...

If you are using the Codium, you may simply ─ when finished the code ─ click 
on right button (of the mouse) and choose the option: Run Python File in 
Terminal.

When you are coding try to limit each line to 80 characters/columns 
(you can see this on the bottom bar of the editor). If you need to have more
characters, use the continuation character: `\` (backslash), obviouly it must 
be the last _char_.

In an Code Editor (_e.g_: Codium) you can, constantly, use the autocompletion 
─ `CTRL + SPACEBAR` ─ a very cool resource.

I recomend you to use this, very cool, font: 
[Fira Code](https://github.com/tonsky/FiraCode/archive/master.zip)

On the archive that you downloaded. Got to the directory (folder) `/distr/ttf`
then install `FiraCode-Regular.ttf`.

On the codium press ─ `CTRL + ,` ─ to open the settings, then search for 
_Editor: Font Family_ and put on it: `'Fira Code Light'`

Install the extension Python by Microsoft ─ press `Ctrl + Shift + X` or click
in the icon Extensions, then search for Python and install it.

Now you can press in the icon _play_ on the right top or click with the right
button and choose the option: Run Python File in Terminal.

> Remember to get a keyboard value, use the `input()` function which returns 
> a `string` (text) and then convert this `string`, if necessary, 
> to an appropriate type. Wrapping the `input()` with the formal 
> name of the type, _e.g._.

```Python
identifier = input('Type a value: ')

to_real = float(identifier)
to_integer = int(identifier)

element_of_a_set = {identifier,}
element_of_a_list = [identifier,]
element_of_a_dict = {'key': identifier}
element_of_a_tuple = (identifier,)
```

## Perform an algorithm to...


1. Receive two numbers, then sum both and print the median of it.

2. Receive a number, then print it raised by the second power (number²).

3. Compute the Body Mass Index (BMI), then print it.

4. Receive two numbers (store it on variables), switch one with other and print
them on screen.

5. Receive three values which corresponds to hours, minutes and seconds, then 
show the total of seconds equivalent.

6. Read a value of speed in meters per seconds, then converts it to 
kilometers per hours.

7. Read the number of kilometers traveled and the amount of fuel spent in 
liters by a car and reports the average fuel spent in each kilometer traveled.

8. Compute the amount of money spent by a smoker on _'rets_ over _n_ years.
To do this, it is necessary to read the number of _'rets_ which the smoker 
smokes per day, the quantity of years which it smokes and the average price 
of a pack of _'rets_ 
(Tips: Each pack of _'rets_ contains 20 cigarettes. Each year has 365 days).

9. Convert Celsius degrees (C°) to Fahrenheit degrees (F°).
    C = ((F - 32) * 5) / 9

10. Receive the cost price of a product, then compute its final price, 
considering:

    - The final price is computed by adding the cost price, the value of
    taxes and the expected profit.

    - The amount of taxes is 45% of the cost price.

    - The expected profit is 50% of the cost price.

11. Compute the cost of a travel by car from a city to another one¹, knowing:

    - The car performs 15km per 1 liter of fuel.
    - The price of the fuel is $$2.60.
    - The price of each toll is $$8.00.

¹ The program need the distance and the number of tolls between the cities.

12. Knowing that the brass has 30% of zinc and 70% of copper. Get the total
of brass in kilograms (Kg), then reports the quantity of zinc and copper on it.

13. Reports the n-th term of a arithmetic progression.

    - a_1: first term.
    - r: reason
    - n: n-th
    - `a_n = a_1 + (n - 1)*r`

14. Compute the accumulated value of a scheduled savings account. It is necessary
to get the value of the monthly application constant (P), the tax (i) and the 
number of months (N).

    `accumulated_value = P*((1 + i)**N - 1) / i`

15. Receive the dimensions of a kitchen (length, height and width) and 
calculate how many boxes of tiles are necessary to tile all the walls 
except the ceiling (consider that the area occupied by windows and doors 
will not be discounted). Each tile box has 1.5 m².

16. Receive an `x` value of money and compute the minimum number of notes 
needed to get the `x` amount of money (consider that there are only the notes: 
$$100.00, $$50.00, $$20.00, $$10.00, $$5.00, $$2.00 and $$1.00). 

For example: Let $$98.00

    1 Note(s) of $$50,00
    2 Note(s) of $$20,00
    1 Note(s) of $$5,00
    1 Note(s) of $$2,00
    1 Note(s) of $$1,00

17. Receive two points P1(x1, y1) and P2(x2, y2), then compute and print the 
distance between them.

    `distance = √((x2 - x1)² + (y2 - y1)²)`

18. Receive the number of sides (N) of a convex polygon, compute the number of 
different diagonals (nd) of it.

    `nd = (n*(n - 3)) / 2`
