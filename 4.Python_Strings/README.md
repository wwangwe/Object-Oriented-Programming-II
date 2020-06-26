# Python Strings

> _Submitted to @MRichardN_  

## 1.0 Introduction

A String in Python is an array or a sequence of *unicode* characters.  

## 2.0 String Operators

Operators can also be applied to strings, thet include:
__+__, __*__ & __in__ operators.

### 2.1 The '__+__' Operator

This operator is used to concutination of strings. It returns a string consisting of the operands.

#### Examples

```python
    >>> x = "Trump is"
    >>> y = " a President"
    >>> z = " a Clown"
    >>> x + y
    'Trump is a President'
    >>> x + z
    'Trump is a Clown'
    >>>
```

### 2.2 The '__*__' Operator

This operator creates multiple copies of a string. It takes two operands, a string `s` and an integer `n` and returns a string consisting `s` ... `n` times.

#### Examples

```python
    >>> s = "eat.."
    >>> s * 4
    'eat..eat..eat..eat..'
    >>>
```

Note that _negative integers_ result to an __empty__ string.

### 2.3 The '__in__' Operator

This is a membership operator, it returns `True` if the left operand is contained in the left operand, `False` otherwise.

#### Examples

```python
    >>> 'a' in 'aeiou'
    True
    >>> 'z' in 'aeiou'
    False
    >>> 'land' in 'a good spaceous land'
    True
    >>> 'grass' in 'a good spaceous land'
    False
    >>>
```

Just like in regular __in__ operators, __not__ does the opposite.

```python
>>> 'bad' not in 'a good spaceous land'
True
>>>
```

## 3.0 Built-in Functions

Python has inherent functions, the following some of the most common ones that can be performed on strings.

| Function | Description|
|----------|------------|
|chr()|Converts an integer to a character
|ord()|Converts a character to an integer
|len()|Returns the length of a string
|str()|Returns a string representation of an object
