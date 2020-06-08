# Decision Making in Python

> _Submitted to @MRichardN_  

## Introduction

__Conditional Statements__, better known as __Control Structures__, direct the _order of execution_ of the statements in a program.  
Decision making statements available in python are:

- `if` statement
- `if`...`else` statements
- nested `if` statements
- `if`...`elif`

## `If` Statements

The `if statement` is how you perform this sort of decision-making. It allows for conditional execution of a statement or group of statements based on the value of an expression.
Below is the simplest most basic _if statement_.

```python
    if <condition>:
        <statement>
```

- `<condition>` evaluates to a boolean, _True_ or _False_.  
- `<statement>` is a valid python statement; it is _indented_.

If `<condition>` evaluates to __True__, `<statement>` is executed, if __False__, is it _Skipped over_.  
__Examples__  

```python
    >>> x = 0
    >>> y = 5
    ...
    >>> if x < y:
    ...     print("yes")
    ...
    'yes'
    yes
    >>> if y < x:           # Does nothing
    ...     print("yes")
    ...
    >>> i = 10
    >>> if (i > 15):
    ...    print ("10 is less than 15")
    ... print ("I am Not in if")
    ...
    'I am Not in if'

```

__Note__ that the (`:`) that follows `<condition>` is required to define the scope of `<statement>`, other languages require that the `<statement>` is enclosed by _Parenthesis_ `{}`

### Flow Chart

![If Statements](../Images/if_statement.jpg)

## `If...Else` Statements  

