# Python fundamentals

<span class="lead">Python</span> is a general purpose, interpreted language created by `Guido van Rossum`, and was released in the year 1991. Python encourages code readability and write fewer lines to express the concepts.

Python supports both procedural and object orinented programming. Many language features support functional programming and aspect-oriented programming.

The language was named after the popular TV show, `Monty Python's Flying Circus` (1969-74).


<img src="https://vinod.co/images/python/guido_van_rossum.jpg" style="height: 200px;" title="Guido van Rossum" alt="Guido van Rossum" class="img img-thumbnail"> <img src="https://vinod.co/images/python/montypython.jpg" style="height: 200px;" title="Monty Python's Flying Circus" alt="Monty Python's Flying Circus" class="img img-thumbnail">

Features of Python include:

* Free and open source
* Interpreted, high level
* Portability
* Extensible
* Embeddable
* Vast library of packages
* Supports procedure oriented, object oriented, functional, and aspect oriented


Python being a very simple and easy to learn language, can be used for teaching programming to kids and non-programmers. However, the language offers so many powerful features, it can be used for variety of applications such as Web applications, Scientific and Numeric applications, and creating software prototypes.

When you install Python, you get a command `python`. When you run the command with out supplying any script file, it will open a shell known as REPL (Read Eval Print and Loop). The REPL has a command prompt that allows us to execute Python commands directly.

```
$ python
Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> message = "Hello, Python!"
>>> print(message)
Hello, Python!
>>> exit()
$
```

Each command you enter will be read, evaluated, and the result is printed. Again it will repeat the same by printing the prompt and waiting for user inputs. To close the REPL, just call the `exit()` function. REPL is a very quick way to test some of the commands. So, many developers keep it handy.

Another and most common way to work with Python is to write a script file and pass it to the `python` command. Let's write our first script and save the file as `hello.py`.


```python
# This is a python script
message = "Hello, Python!"
print(message)
```

Any line that starts with the pound (#) symbol is considered as a `code comment`, and the interpretor will simply ignore the same. To execute the code, open a terminal (command prompt) and run the command:

```
$ python hello.py
```

As expected, it will simply print out the message "Hello, Python!".

On Unix based operating system (Linux, Ubuntu, MacOS etc), we may also add a special comment (usually known as hashbang), pointing to the python executable:

```
#! /usr/bin/python
```

In order to execute the file, we have to add `x` permission to the script file, and then we can simply run the program using the filename itself.

```
$ chmod u+x hello.py
$ ./hello.py
$ Hello, Python!
```

A variable represents a value in the memory. Unlike many other popular languages, in Python there is no need to declare a variable in advance. It is dynamically typed. The datatype of the variable changes based on the value you assign to it. The naming convention for variables (and identifiers in general) is defined in `PEP 8`. 

PEP stands for Python Enhancement Proposal. A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment. The PEP should provide a concise technical specification of the feature and a rationale for the feature.

Some good variable convention:

* lowercase
* underscore_between_words
* don't start with numbers

```
# Working with variables

>>> var_a = 1
>>> type(var_a)
<class 'int'>
>>> 
>>> var_a = 98734598634869623946868234987345986348696239468682349873459863486962394686823498734598634869623946868234634869623946868234987345986348696239468682349873459863486962394686823498734598634869623946868234634869623946868234987345986348696239468682349873459863486962394686823498734598634869623946868234634869623946868234987345986348696239468682349873459863486962394686823498734598634869623946868234
>>> type(var_a)
<class 'int'>
>>> 
>>> var_a = 1.2
>>> type(var_a)
<class 'float'>
>>> 
>>> var_a = "Vinod"
>>> type(var_a)
<class 'str'>
>>> 
>>> var_a = 'Vinod'
>>> type(var_a)
<class 'str'>
>>> 
>>> var_a = True
>>> type(var_a)
<class 'bool'>
>>> 
>>> var_a = None
>>> type(var_a)
<class 'NoneType'>

```

Couple of things to observe:

* Numbers can be integers or float.
* Python allow extremely large values for numericals with out losing any precision.
* Single and double quotes mean the same thing - they are just strings.
* Boolean literals are `True` and `False`.
* `None` represents absense of value in a variable. In a boolean context, it will evaluate to False.
* Unlike C/C++/Java/C# the statements do not end with semicolon.

A value in Python is an object in the memory and has a unique id associated with it. Although it is not very useful practically, we can always find the id using the `id(var)` function.

```
>>> var_a = "Vinod"
>>> id(var_a)
4331162848
>>> var_a = 123
>>> id(var_a)
4297627840
>>> var_a = var_a + 10
>>> id(var_a)
4297628160
>>> 

```

With numeric variables, we can do the following maths:

<table class="table-bordered table-striped table-hover table-condensed">
	<tr>
		<th>Operator</th>
		<th>Used for</th>
		<th>Example</th>
		<th>Result</th>
	</tr>
	<tr>
		<td class="lead">+</td>
		<td>Addition</td>
		<td>a = 7+2</td>
		<td>9</td>
	</tr>
	<tr>
		<td class="lead">-</td>
		<td>Subtraction</td>
		<td>a = 7-2</td>
		<td>5</td>
	</tr>
	<tr>
		<td class="lead">*</td>
		<td>Multiplication</td>
		<td>a = 7*2</td>
		<td>14</td>
	</tr>
	<tr>
		<td class="lead">/</td>
		<td>Division</td>
		<td>a = 7/2</td>
		<td>3.5</td>
	</tr>
	<tr>
		<td class="lead">//</td>
		<td>Integer division</td>
		<td>a = 7//2</td>
		<td>3</td>
	</tr>
	<tr>
		<td class="lead">**</td>
		<td>Exponent</td>
		<td>a = 7**2</td>
		<td>49</td>
	</tr>
</table>


A String (class `str`) is a value with in single or double quotes. Strings are immutable (they can't be changed in place). By enclosing a text in 3 single or double quotes, we can even have multiline strings. These multiline strings are usually used for documentation purposes.

```
my_name = "Vinod"
my_city = 'Bangalore'
doc = '''This is a multiline string
usually used for code documentation
inside a module, class, function etc.'''
```

Strings can also contain escape characters that would produce different output:

<table class="table-bordered table-striped table-hover table-condensed">
	<thead>
		<tr>
			<th>Escape sequence</th>
			<th>Output</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>\n</td>
			<td>New line</td>
		</tr>
		<tr>
			<td>\t</td>
			<td>Tab</td>
		</tr>
		<tr>
			<td>\'</td>
			<td>Single quoute</td>
		</tr>
		<tr>
			<td>\"</td>
			<td>Double quoute</td>
		</tr>
		<tr>
			<td>\\</td>
			<td>Back slash</td>
		</tr>
		<tr>
			<td>\b</td>
			<td>ASCII backspace</td>
		</tr>
		<tr>
			<td>\u0C95</td>
			<td>A unicode character</td>
		</tr>
	</tbody>
</table>

---

We can format a string in two ways:

<p class="lead">C style - using % format specifiers</p>

```
>>> my_name = "Vinod"
>>> my_city = "Bangalore"
>>> info = "%s lives in %s" % (my_name, my_city)
>>> info
'Vinod lives in Bangalore'
>>> 
```

<p class="lead">PEP 3101 style - using { }</p>

```
>>> my_name = "Vinod"
>>> my_city = "Bangalore"
>>> info = "{0} lives in {1}".format(my_name, my_city)
>>> info
'Vinod lives in Bangalore'
>>> 

```

<p class="lead">Most useful `string` functions</p>

* capitalize
	* Return a capitalized version of the string, i.e. make the first character have upper case and the rest lower case.
	* For example, "VINOD KUMAR".capitalize() returns "Vinod kumar"
* center
	* Return the string, centered in a string of length width. Padding is done using the specified fill character (default is a space)
	* For example, "VINOD".center(25, "*") returns "**********VINOD**********"
* count
	* Return the number of non-overlapping occurrences of substring sub in the string
	* For example, "ANANDA RAMA".count("AN") returns 2
* endswith
	* Return True if the string ends with the specified suffix, False otherwise. 
	* For example, "VINOD".endswith("D") returns True
* find
	* Return the lowest index in string where substring sub is found, such that sub is contained within the string
	* For example, "VINOD KUMAR".find("MA") returns 8, and "VINOD KUMAR".find("xy") returns -1
* index
	* Like the **find** function, but raise ValueError when the substring is not found
* isalnum
	* Return True if all characters in string are alphanumeric and there is at least one character in string False otherwise
* isalpha
	* Return True if all characters in string are alphabetic and there is at least one character in S, False otherwise
* isdecimal
	* Return True if there are only decimal characters in string False otherwise
* isdigit
	* Return True if all characters in string are digits and there is at least one character in string False otherwise
* islower
	* Return True if all cased characters in string are lowercase and there is at least one cased character in string False otherwise
* isnumeric
	* Return True if there are only numeric characters in string False otherwise
* isspace
	* Return True if all characters in string are whitespace and there is at least one character in string False otherwise
* istitle
	* Return True if string is a titlecased string and there is at least one character in string i.e. upper- and titlecase characters may only follow uncased characters and lowercase characters only cased ones. Return False otherwise
* isupper
	* Return True if all cased characters in string are uppercase and there is at least one cased character in string False otherwise
* join
	* Return a string which is the concatenation of the strings in the iterable
	* For example, "-".join(["Vinod", "Kumar", "John", "Jane"]) returns "Vinod-Kumar-John-Jane"
* lower
	* Return a copy of the string string converted to lowercase
* replace
	* Return a copy of string with all occurrences of substring old replaced by new.  If the optional argument count is given, only the first count occurrences are replaced
	* For example, "black white orange yellow".replace("orange", "red") returns "black white red yellow"
* split
	* Return a list of the words in string using sep as the delimiter string. 
	* For example, "black,white,orange,yellow".split(",") returns a list ["black", "white", "orange", "yellow"]
* startswith
	* Return True if string starts with the specified prefix, False otherwise
	* For example, "VINOD".endswith("V") returns True
* strip
	* Return a copy of the string string with leading and trailing whitespace removed
* swapcase
	* Return a copy of string with uppercase characters converted to lowercase and vice versa
	* For example, "Vinod Kumar Kayartaya".swapcase() returns "vINOD kUMAR kAYARTAYA"
* title
	* Return a titlecased version of string
	* For example, "VINOD KUMAR KAYARTAYA".title() returns "Vinod Kumar Kayartaya"
* upper
	* Return a copy of string converted to uppercase


Python does not allow addition / concatenation of values of different types. 

```
>>> 
>>> n1 = 100
>>> n2 = 12
>>> n1 + n2
112
>>> s1 = "Vinod"
>>> s2 = "Kumar"
>>> s1 + s2
'VinodKumar'
>>> n1 + s1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 

``` 

But one strange operation is that you can multiply a string by a number!

```
>>> 
>>> "-" * 10
'----------'
>>> "vinod" * 3
'vinodvinodvinod'
>>> 10 * "-"
'----------'
>>> 
```

For conditional execution, we can use the `if` statements. The syntax for the same is:

```python
Syntax:

	if <condition> :
		<statements>
```

Two things to observe from the above syntax:

1. After the boolean criteria, we have a colon symbol
2. The statements to be executed if the boolean criteria evaluates to true should be indented. This is one of the Python's phylosophy - the code should be readable. In most other languages (C/C++/Java/C#), we would use a pair of curly braces group the statements to be executed when the condition is true. In some other languages (VB, Oracle and MySQL stored procedures, Unix shell scripts), we would use a statement like `end-if` to denote the end of the statemetns to be executed when the condition is true.

Here is an example. It shows how to read a value from the keyboard and print if the number is even or odd.

```
# Python script to check if the input number is even or odd

# In Python 3, the input function returns a 'str' object. 
num = input("Enter a number: ") 

# converting the num from 'str' to 'int' type.
num = int(num) 

message = "The input number is an odd number."

if num % 2 == 0:
	message = "The input number is an even number."

print(message)

```

When executed, here is the output:

```
$ python3 if1.py 
Enter a number: 23
The input number is an odd number.
$
$ python3 if1.py 
Enter a number: 34
The input number is an even number.
$ 
```

You might have observed that I have assigned a default value to the variable `message`. I am  only chaning it's value, if the condition evaluates to true. Alternately we may use the `else` block to assign the alternate message to the variable.

```python
Syntax:

	if <condition> :
		<statements>
	else:
		<statements>
```


Let's have a look at another example. This time, I want to read the age of the user and print if he/she can vote or not!


```
# Check if the user can vote or not.

age = int(input("Enter your age: "))

if age>=18:
	print("Yes! you can and should vote.")
else:
	print("Hey, just wait for another %d years to vote." % (18-age))

```

And the output of the same is:

```
$ python3 ifelse1.py 
Enter your age: 43
Yes! you can and should vote.
$ 
$ python3 ifelse1.py 
Enter your age: 12
Hey, just wait for another 6 years to vote.
$
```

In some cases, when the condition evaluates to false, we would like to check one more condition. And when the second one fails, we would like to check for another, and so on. We can do this with the combination of `if-elif-else`.

```python
Syntax:

	if <condition> :
		<statements>
	elif <condition> :
		<statements>
	...
		...
	else:
		<statements>
```

This example shows how to find the number of days in a given month.

```python
# Find the number of days in the input month.

mon = int(input("Enter a month (1-12): "))

if mon == 2:
	print("Maximum number of days in the input month is 28 or 29.")
elif mon in (4, 6, 9, 11):
	print("Maximum number of days in the input month is 30.")
elif mon in (1, 3, 5, 7, 8, 10, 12):
	print("Maximum number of days in the input month is 31.")
else:
	print("You have entered an invalid month number.")

```

And here are few sample execution of the same.
```
$ python3 ifelifelse1.py 
Enter a month (1-12): 3
Maximum number of days in the input month is 31.
$ 
$ python3 ifelifelse1.py 
Enter a month (1-12): 4
Maximum number of days in the input month is 30.
$ 
$ python3 ifelifelse1.py 
Enter a month (1-12): 2
Maximum number of days in the input month is 28 or 29.
$ 
$ python3 ifelifelse1.py 
Enter a month (1-12): 17
You have entered an invalid month number.
$ 
```

Python does not have ternary operator (like in C/C++/Java/C#), which would have been handy. But, if-else combination can be used for the same too:

````python
condition = year%400==0 or (year%4==0 and year%100!=0)
days = 29 if condition else 28
````


