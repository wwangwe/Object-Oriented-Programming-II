# Python Variables

## Introduction

**Variables** are the names you give to computer memory locations which are used to store values in a **Computer Program**.  
Unlike most programming languages, Python is **Dynamically typed** and therefore there _values_ and _data types_ can be changed during _runtime_.

## Assignment

Assigning a value is known as binding in Python.\
The _**Assignment Operator '='**_ is used to _bind_ a value to an Variable name.  

### Variabale Name

A variable name can be either of the following:  
    - A letter eg. `x = 12`  
    - A word   eg. `crate = 24`  
    - A word with an underscores eg. `is_it_love = False`  
    - A word with a letter eg. `RG45 = "Ethernet Cable"`  
        _**Note that a number can only appear in the middle or end of a variable name, not a the beginning.**_  
        _Example:_\

```python

    >>> 45RG = "Ethernet Cable"
    File "<stdin>", line 1
    45RG = "Ethernet Cable"
    ^
    SyntaxError: invalid syntax

```  

_It is also vital to know that variables are **Case Sensitive**, therefore; life, Life, LIFE and lifE are different names._

## Data Types

Pythons supports _Integers, Floating Points, Strings, Booleans and Collections (lists, tuples &n libraries),_ they are all assigned variables in the same way. The following code illustrates:

### Strings

```python
    Python 3.8.2 (default, May 17 2020, 02:53:34)  
    [GCC 9.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> name = "Timothy Wangwe"     # String
    >>> name
    'Timothy Wangwe'
```

### Boleans

```python
    >>> male = True                 # Boolean
    >>> male
    True
```

### Integers

```python
    >>> age = 20                    # Integer
    >>> age
    20
```

### Operations  

```python
    >>> birth_year = 2020 - age     # Operations
    >>> birth_year
    2000
```

### Floating Points  

```python
    >>> height = 1.78               # Float
    >>> height
    1.78
```

### Tuples  

```python
    >>> full_name = ('Timothy', 'Wangwe')
    >>> full_name
    ('Timothy', 'Wangwe')
```

### Lists

```python
    >>> interests = [               # List
    ...             'Data Science',  
    ...             'Basketball',  
    ...             'Sci-fi Movies'
    ...             ]  
    >>> interests
    ['Data Science', 'Basketball', 'Sci-fi Movies']
```

### Dictionary

```python
    >>> summary = {                 # Dictionary
    ...     "Name":       name,
    ...     "Age":        age,
    ...     "Birth year": birth_year,
    ...     "Height":     height,
    ...     "Interests":  interests,
    ... }
    >>> summary
    {'Name': 'Timothy Wangwe', 'Age': 20, 'Birth year': 2000, 'Height': 1.78, 'Interests': ['Data Science', 'Basketball', 'Sci-fi Movies']}
    >>>  
```  

## Scope

Variables have local and global scope.  

### Local Scope

For example variables declared _**within** a function_, can only exist within the block. Once the block exists, the variables also become _inaccessible_.  
Example:  

```python

    >>> def scope():    #]In  
    ...    var = 4      #]  scope

    ...print(4)             #}Out
    Fle "<stdin>", line 3   #}   of
    print(4)                #}     scope
    ^
    SynaxError: invalid syntax
    >>>
```

Note that If-Else and For/While loops do not create a local scope.  

### Global Scope

Variables that can be accessed from any function have a global scope.  
You can declare a global variable outside of functions. It’s important to note that to assign a global variable a new value, you will have to use the _“global”_ keyword.  
Example:  

```python

    var = True
    def scope():
        global var
        var = False
    scope()
    print(var) # Returns False

```

Excluding the line `global var` will only set the variable to False within the scope() function.  

## Importance

1. Variable length saves space (in code)
2. Allow use of large sets of data without manually input
3. They allow reuse of data