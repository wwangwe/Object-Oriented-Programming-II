# Operators in Python

> _Submitted to @MRichardN_  

## 1.0 Introduction

An operator is a symbol that tells the compiler to perform specific mathematical or logical manipulations. The values that an operator acts on are called __Operands__.  
> _Example:_  
`y = m*x + c`  
`y, m, x,` and `c` are Operands  
while  
`=, *` and `+` are the Operators.  

### 1.1 Arithmetic Operators  

Arithmetic operators take numerical values (either literals or variables) as their operands and return a single numerical value.  
The basic arithmetic operators are Addition ( + ), Subtraction ( - ), Multiplication ( * ) and Division ( / ).  
The following table lists the arithmetic operators supported by Python:  

|Operator|Meaning       |Example  |Result                                  |
|-------|---------------|---------|----------------------------------------|
|+      | Addition      | 5 + 2   | Sum of 5 and 2 = (7)                   |
|-      | Subtraction   | 5 - 2   | Difference of 5 and 2 = (3)            |
|\*     | Multiplication| 5 * 2   | Product of 5 and 2 = (10)              |
|/      | Division      | 5 / 2   | Quotient when 5 is divided be 2 = (2.5)|
|//     | Floor Division| 5 // 2  | Quotient when 5 is divided be 2 and rounded to the next smallest whole number = (2.0)|
|%      | Modulus       | 5 % 2   | Reminder when 5 is divided by 2 = (1)  |
|\**    | Exponentiation| 5 ** 2  | 5 Raised to the power of 2 = (25)      |

__Note__ that  The result of standard division ( / ) is always a float, even if the dividend is evenly divisible by the divisor:  

```python
    >>> 10 / 5
    2.0
    >>> type(10 / 5)
    <class 'float'>
```

View more examples in the Python file in this directory.  

### 1.2 Assignment Operators  

A single equal sign (=) is used to assign a value to a variable. The on its left is the variable name while on its
right is the value or expression of the variable.
Example:

```python
    >>> a = 10
    >>> b = 20
    >>> c = a * 5 + b
    >>> c
    70
```

View more examples in the Python file in this directory.

### 1.3 Comparison Operators

Comparison Operators compare values and operations and return _True_ or _False_.  
The following table lists the arithmetic operators supported by Python:  
|Operator     | Meaning                 | Example   |  Result                                                                      |
|-------------|-------------------------|-----------|------------------------------------------------------------------------------|
|   >         | Greater than            | 4 > 2     |_True_ if 4 is Greater than 2, _False_ otherwise; In this case __True__       |
|   <         | Less than               | 4 < 2     |_True_ if 4 is Less than 2, _False_ otherwise; In this case __False__         |
|   ==        | Equal to                | 4 == 2    |_True_ if 4 is Equal to 2, _False_ otherwise; In this case __False__          |
|   !=        | Not equal to            | 4 != 2    |_True_ if 4 is Not Equal to 2, _False_ otherwise; In this case __True__       |
|   >=        | Greater than or equal to| 4 >= 2    |_True_ if 4 is Either Greater or equal to 2, _False_ otherwise; In this case __True__|
|   <=        | Less than or equal to   | 4 <= 2    |_True_ if 4 is Either Less or equal to 2, _False_ otherwise; In this case __False__  |

View more examples in the Python file in this directory.

### 1.4 Logical Opeartors  

Logical operators in Python are used for conditional statements; they evaluate to and return _True_ or _False_. Common logical operators include
__AND__, __OR__, and __NOT__.  
They following conditions apply to logical operators:  

> - AND Operator  
    It returns TRUE if both the operands (right side and left side) are true  
    It returns TRUE if both the operands (right side and left side) are false
> - OR Operator  
    It returns TRUE if either of the operands (right side or left side) is true  
    It returns FALSE if neither of the operands (right side or left side) is true
> - NOT Operator  
    It returns TRUE if operand is false  
    It returns FALSE if operand is true

```python
    >>> a = True
    >>> b = False
    >>> a and b
    False
    >>> a or b
    True
    >>> not a
    False       # not inverts the boolean
    >>> not b
    True
    >>>
```

View more examples in the Python file in this directory.

### 1.5 Membership Operators  

Membership operators test for membership in a sequence such as __lists, strings__ or __tuples__.  
There are two membership operators that are used in Python. (**_in, not in_**). It gives the result based on whether or not the variable is
present in specified sequence.  
Example;  

```python
    >>> a = 2
    >>> b = 7
    >>> even = (2, 4, 6, 8, 10)
    >>> a in even
    True
    >>> b in even
    False
    >>>
```

View more examples in the Python file in this directory.

### 1.6 Bitwise Operators  

Bitwise operators treat operands as sequences of binary digits and operate on them bit by bit.  
The following operators are supported:
| Operator  | Meaning                    | Example     | Result                                                             |
|-----------|----------------------------|-------------|--------------------------------------------------------------------|
|   &       | Bitwise AND                |  x & y      | 1 if both are 1, otherwise 0                                       |
|   &#124;  | Bitwise OR                 |  x &#124; y | 1 if either is 1, otherwise 0                                      |
|   ~       | Bitwise __negation__       |  ~ x        | 1 if 0, 0 if 1                                                     |
|   ^       | Bitwise XOR (exclusive or) |  x ^ y      | 1 if the bits in the operands are different, 0 if they are the same|
|   >>      | Shift Right                |  x >> n     | Each bit is shifted right n places                                 |
|   <<      | Shift Left                 |  y << n     | Each bit is shifted left n places                                  |

View more examples in the Python file in this directory.

## 2.0 Operator precedence

The following table summarizes the operator precedence in Python, from lowest precedence (least binding) to highest precedence (most binding).  
Operators in the same box have the same precedence. Operators in the same box group left to right (except for exponentiation, which groups from right to left).

| Operator                                     | Description                                                                  |
|----------------------------------------------|------------------------------------------------------------------------------|
| :=                                           | Assignment expression                                                        |
| lambda                                       | Lambda expression                                                            |
| if – else                                    | Conditional expression                                                       |
| or                                           | Boolean OR                                                                   |
| and                                          | Boolean AND                                                                  |
| not x                                        | Boolean NOT                                                                  |
| in, not in, is, is not, <, <=, >, >=, !=, == | Comparisons, including membership tests and identity tests                   |
| &#124;                                       | Bitwise OR                                                                   |
| ^                                            | Bitwise XOR                                                                  |
| &                                            | Bitwise AND                                                                  |
| <<, >>                                       | Shifts                                                                       |
| +, -                                         | Addition and subtraction                                                     |
| *, @, /, //, %                               | Multiplication, matrix multiplication, division, floor division, remainder 5 |
| +x, -x, ~x                                   | Positive, negative, bitwise NOT                                              |
| **                                           | Exponentiation 6                                                             |
| await x                                      | Await expression                                                             |
| x[index], x[index:index], x(arguments...), x.attribute | Subscription, slicing, call, attribute reference                   |
| (expressions...), [expressions...], {key: value...}, {expressions...} | Binding or parenthesized expression, list display, dictionary display, set display|
