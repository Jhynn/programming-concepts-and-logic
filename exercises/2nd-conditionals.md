# Conditional structuries exercises

1. Compute the ideal wheight¹ of a person, knowing:

    - Men: `72*height - 58`

    - Women: `62.1*height - 44.7`

    ¹ The program must have the sex and the height of this person.

2. Receive a number and report if it is even or odd.

3. Receive 2 scores of a student and report if him/her was approved, consider 
6 as a minimum average for this.

4. Read an arithmetic operator symbol (`+, -, *, /`) and two real numbers, 
then perform the correct arithmetic operation.

5. Receive three numbers then sort them.

6. Receive the name and the marital state of someone. If this person
is maried request for how long time. Print a message.

7. Receive two numbers then print if the first number is a multiple of the 
second one or vice versa or if they are not multiple.

8. Receive a number and verify if this number is valid to be
a number of a month then print the name of this month.

9. Receive three numbers (consider that the numbers is not equal to each other)
and sum the two largest numbers.

10. Receive the width and length then reports if this geometric figure is a 
square or a rectangle.

11. A company gives a gift to employies who catch up a goal (sell of products).
Each employe has a specific goal. Perform an algorithm to define this unique ─ 
to each one employe ─ goal and the value ($) catched by this same employe. Print
a message if him/her aime the goal. Whether or not him/her catched up.

12. Receive the student's score then reports the grade of her/him.

| Score | Grade |
:------:|:-----:|
0 - 39  | F     |
40 - 49 | E     |
50 - 59 | D     |
60 - 69 | C     |
70 - 79 | B     |
  ≥ 80  | A     |

13. Receive three values for the sides of a triangle, considering the sides as: 
A, B and C. You will verify if the sides really creates a triangle. If this 
condition is true, you will indicates which type of triangle was created: 
isosceles, scalene or equilateral.

14. Receive four values: `i, a, b, c` where `i` is a natural number and the
remaining are real numbers. Print ─ `a, b, c` ─ accordingly with the following 
rules.

- `i = 1`: print the values, `a, b, c`, in ascending order.
- `i = 2`: print the values, `a, b, c`, in descending order.
- `i = any value (default)`: print the values, `a, b, c`, in someway that 
the largest one be in between the remainig.

15. Read an employee's base salary, calculates and shows the salary to be 
received. Knowing that employee has.
- 5% bonus on the base salary and pays 
- 7% tax on the total...

16. Each apple cost 40 cents if buyed less than twelve, if buyed more than this 
it costs 25 cents. Receive the number of apples buyed then show how many needs 
be paid.

17. Get the age of a swimmer then report which category it is classified.

    | Child A | Child B | Juvenile A | Juvenile B | Adult |
    |:-------:|:-------:|:----------:|:----------:|:-----:|
    | 5 - 7   | 8 - 10  | 11 - 13    | 14 - 17    | > 17  |

18. Read the identification number of a alumnus or alumna and report him/her
average utilization, to do that receive the three exam scores and the average
of the exercises. Use the formula below.

`AU = (score_1 + score_2*2 + score_3*3 + exercises_average) / 7`

The concept attribution is defined below.

| Average Utilization | Concept |
|:-------------------:|:-------:|
| ≥ 9                 | A       |
| ≥ 7.5 < 9           | B       |
| ≥ 6 < 7.5           | C       |
| ≥ 4 < 6             | D       |
| < 4                 | E       |

You need to print a message saying ─ if the concept was A, B or C ─ Approved. 
And Fail, if the concept was D or E.

19. Build a program that reads the start and end time of a game (considering
hours and minutes as integers) and calculates the game duration, knowing that 
the maximum duration time of the game is 24 hours and the game can start in one
day and finish in the next one.

20. There are three types of polluting industries. The pollution index 
acceptable ranges from 0 to 0.29. If the index increases to 0.3, the 
industries of the 1st group are intimate to suspend their activities, if the 
index increases to 0.4, the 1st and the 2nd group must stop their activies.
If the index aim 0.5 all the groups must stop their activies.
Read the pollution index then print an appropriate message.

21. Read three values: day, month and year. Then report if it is a valid date.
> Remember that a year is a leap year when it is a multiple of 4, but it is 
> not a multiple of 100, except for the multiple years of 400.

22. A company pays to its employees $1.00 of comission to each selled product, 
however, if it would selled more than 250 products the comission increases to 
$1.5 and if would selled more than 500 products the comission increases to 
$2.00. Receive the name of an employe and the quantity of products selled by 
it, then print its name and the total of comissioin that it will receive.

23. A city is classified accordingly with the pollution index which is defined
this way: pollution index less than 35 is pleasant, from 35 to 60 is unpleasant
and above to 60 is dangerous. Someone wants to move for another city, a city 
that is pleasant and sparsely populated.
Read the pollution level of the city and its population, then classify it 
in the next way:

- Good: only if the pollution level is less than 35 and the population was less than 20,000 habitants.

- Reasonable: pollution level pleasant or unpleasant and the population less 
than 20,000.

- Bad: pollution level beeing unpleasant or dangerous and population
greater than 40,000.

- Terrible: pollution level beeing dangerous and the population greater than 
100,000.

24. Based on the table below.

| Code |    Role    | Percentual |
|:----:|:----------:|:----------:|
| 136  | Manager    | 30%        |
| 137  | Scientist  | 43%        |
| 138  | Engineer   | 12%        |
| 139  | Technician | 33%        |
| 140  | Cleaners   | 50%        |

The salaries of these employees will increase if the role (code) of the employee
do not in there, so increase it salary in 40%.
Receive the name, salary and the role of the employe. Print the old salary, the 
new salary and its difference.

25. A bank will grant a special credit to its clients, variable with the 
average balance in the last year. Read the average balance of the client then
calculates the credit value accordingly with the table.

| Average balance |          Credit        |
|:---------------:|:----------------------:|
| up to $200.99   |             ─          |
| $201 to $400.99 | 20% of the avg balance |
| $401 to $600    | 30% of the avg balance |
| above of $600   | 40% of the avg balance |

Print a message showing the average balance and the credit value.
