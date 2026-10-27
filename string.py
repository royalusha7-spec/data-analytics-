Python 3.14.8 (tags/v3.14.8:8e6e75d, Sep 30 2026, 18:19:33) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=""
len(d)
0
d=" "
len(d)
1
#count()
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("t")
5
a.count("a")
1
a.count(" ")
3
a="1234"
a.count("3")
1
a=1,2,3,4,5,6
a.count(3)
1
b=3,4,5,6,3,7
b.count(3)
2
a="code"
a{2}
SyntaxError: invalid syntax
a[2]
'd'
a.find("d")
2
b="hello"
b.find("1")
-1
b.find("l")
2
b[2:4]
'll'
b.find("k")
-1
#escape sequences
#\n->new line
#\t->tab space
a="name\nmobileno:1234567897\royalusha@7gmail.com/ncollege:urce\tbranch:cse
SyntaxError: unterminated string literal (detected at line 1)
>>> a="name:usha\nmobileno:1234567878\tmailid:royalusha@gmail.com/ncollege
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> #replace()
>>> a="wait until you succees"
>>> a.replace("wait","work")
'work until you succees'
>>> a="python java"
>>> a.replace("java","DSA")
'python DSA'
>>> a="hi"
>>> a.replace("h","a")
'ai'
>>> #escape sequences
>>> #\n->new line
>>> #\t->tab space
>>> a="name\nmobile\tmailid\ncollege\tbranch"
>>> print(a)
name
mobile	mailid
college	branch
>>> a="name:usha\nmobileno:1234567895\tmailid:royalusha@gmail.com\ncollege:pims\tbranch:da"
>>> print(a)
name:usha
mobileno:1234567895	mailid:royalusha@gmail.com
college:pims	branch:da
