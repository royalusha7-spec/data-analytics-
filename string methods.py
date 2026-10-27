Python 3.14.8 (tags/v3.14.8:8e6e75d, Sep 30 2026, 18:19:33) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #string methods
>>> #upper()
>>> a="code"
>>> 
>>> a.upper()
'CODE'
>>> b="python"
>>> b.upper()
'PYTHON'
>>> #lower()
>>> c="HELLO"
>>> c.lower()
'hello'
>>> d="HI"
>>> d.lower()
'hi'
>>> a="python"
>>> a.upper("p")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.upper("p")
TypeError: str.upper() takes no arguments (1 given)
>>> a[0].upper()
'P'
>>> #capitalize
a.capitalize
<built-in method capitalize of str object at 0x000001D6CC13BB40>
a.capaptalize()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.capaptalize()
AttributeError: 'str' object has no attribute 'capaptalize'. Did you mean: 'capitalize'?
capitalize()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    capitalize()
NameError: name 'capitalize' is not defined
a.capitalize()
'Python'
b="python course"
b.title()
'Python Course'
c"i am in class"
SyntaxError: invalid syntax
c="i am in class"
c.title()
'I Am In Class'
c.capitalize()
'I am in class'
a="hello"
a.isupper()
False
a.isupper()
False
a.isalpha()
True
b="hello world"
b.alpha()
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    b.alpha()
AttributeError: 'str' object has no attribute 'alpha'. Did you mean: 'isalpha'?
b.isalpha()
False
a.isdigit()
False
b=12345
b.isdigit()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    b.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
b.isdigit()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    b.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
a.isdigit()
False
c="12345"
c.isdigit()
True
a="python course"
a.startswith("p)
             
SyntaxError: unterminated string literal (detected at line 1)
a.startswith("p")
True
a.endswith("e")
True
b="python COURSE")
SyntaxError: unmatched ')'
B="python COURSE"
B.ISUPPER()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    B.ISUPPER()
AttributeError: 'str' object has no attribute 'ISUPPER'
b="python COURSE"
b=isupper()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    b=isupper()
NameError: name 'isupper' is not defined. Did you mean: 'super'?
b.isupper()
False
c="usha1234"
c.isalnum()
True
#strip()
#rstrip
9
9
#strip()
#rstrip(),lstrip()
a="  usha   "
a.strip()
'usha'
a.rstrip()
'  usha'
a.lstrip()
'usha   '

#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b= " i am learning python"
b.split()
['i', 'am', 'learning', 'python']
c=b.split()

c
['i', 'am', 'learning', 'python']
c[1].upper()
'AM'
#jion()
a="apple","banana","grapes"
"".jion(a)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    "".jion(a)
AttributeError: 'str' object has no attribute 'jion'
" ".jion(a)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    " ".jion(a)
AttributeError: 'str' object has no attribute 'jion'
" ".join(a)
'apple banana grapes'
"".join(a)
'applebananagrapes'
"k".join(a)
'applekbananakgrapes'
b="hello"
"k".join(b)
'hkeklklko'
fname="usha"
lname="ch"
print(fname+lname)
ushach
#concatrnation()
a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="course"
print(a+b)
pythoncourse
print(a+""b)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(a""+b)
SyntaxError: invalid syntax
print(a+""+b)
pythoncourse
print(fname+""+lname)
ushach
print(fname.title()+""+lname.title()0
      
SyntaxError: '(' was never closed
print(fname.title()+""+lname.title())
UshaCh
print((fname+" "+lname.title())

   print((fname+" "+lname).title())
      
SyntaxError: '(' was never closed
#formating
a=5
b=7
print(a+b)
12
print("the sum is",a+b)
the sum is 12
print("the sum is a+b")
the sum is a+b
city="vja"
print("city is ",city)
city is  vja
a="motu"
b="pathlu"
#format()
prin("hello {}{}".format(a,b))
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    prin("hello {}{}".format(a,b))
NameError: name 'prin' is not defined. Did you mean: 'print'?
print("hello {}{}.format(a,b))
      
SyntaxError: unterminated string literal (detected at line 1)
print("hello {}{}".format(a,b))
hello motupathlu
print("hello {} {}".format(a,b))
hello motu pathlu
print("hello{} hello{}".format(a,b))
hellomotu hellopathlu
#fstring
a="sweety"
="cuty"
SyntaxError: invalid syntax
b="cuty"
print(f"hello {a}{b}")
hello sweetycuty
print(f"hello {a} {b}")
hello sweety cuty
print(f"hell {a] hello {b]"0
      
SyntaxError: f-string: unmatched ']'
print(f"hello {a} hello {b}")
hello sweety hello cuty
