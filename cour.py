#=========================================================================
print('===================== START =======================')
print("I love python") 
print("I love programming") 
print('----------comment--------------')

#---------comment-------------------------
# Informations About file 
# license
# who created the file
# when the file created 
# why the file created 
# write beside the programming line 
# write before the programming line
# prevent code frome run 

print("I love python") #this is inline comment 
print("programming") # I used this method becouse of bla bla bla 
print('------------------------')

"""
This is 
Not 
Multiple 
Line 
Comments

"""

print('=====================Somme DATA Type In PYTHON=======================')
#=========================================================================






#=========================================================================
# 1------- Some Data Types in Python -------
# All data in Python is an object.
# type()  → Used to check the data type of a variable
# int()   → Converts a value to an integer (e.g. "5" → 5)
# float() → Converts a value to a floating-point number (e.g. "3.14" → 3.14)
# str()   → Converts a value to a string (e.g. 123 → "123")
# bool()  → Converts a value to a boolean (e.g. 0 → False, "hello" → True)


print('-----------type() => int-----------')
print (type(10)) # int => integer
print (type(100)) # int => integer
print (type(-50)) # int => integer
print('---------type() => float---------------')

print (type(50.0)) # float => floating point number
print (type(50.5)) # float => floating point number
print (type(-65.5)) # float => floating point number
print('-----------type() => str-------------')

print (type("hello")) # str => string
print (type("hello world")) # str => string
print('-----------type() => bool-------------')

print (type(True)) # bool => boolean
print (type(False)) # bool => boolean
print (type(10>5)) # bool => boolean
print (type(10<5)) # bool => boolean
print (type(10==5)) # bool => boolean
print (type(10==10)) # bool => boolean
print (type(10!=5)) # bool => boolean
print('----------type() => list--------------')

print(type([1,2,3])) # list => list 
print('----------type() => tuple--------------')

print(type((1,2,3))) # tuple => tuple 
print('-----------type() => set-------------')

print(type({1,2,3})) # set => set 
print('---------type() => dict---------------')

print(type({1:"hello",2:"world"})) # dict => dictionary
print('----------comparison--------------')

print(2==2);print(4==5)
print(2!=2);print(4!=5)
print('-----------float() & int() & str() -------------')

print(float(10)) # convert integer to float 10 to 10.0
print(int(10.5)) # convert float to integer 10.5 to 10
print(str(10)) # convert integer to string 10 to "10"
print('------------------------')


print('====================VARIABLES========================')
#=========================================================================





#=========================================================================
# -- Variables --
# ---------- PART1 -------
#
# Syntax => [Variabe Name] [Assignment Operator] [Value]
#
# Name Convention and Rules 
# [1] Can Start With (a-z, A-Z) or Underscore (_) 
# [2] You cannot Start With Number or special characters Like !,@ ...etc
# [3] Can Include (0-9)or underscore (_) 
# [4] cannot Include Special Characters like !, @, #, $ ...etc
# [5] Name is Not Like name [ Case Sensitive ] 

print('----------variable--------------')
MyVariable = "Hello naima" # String 
print(MyVariable) 

my_Variable = "Hello rachida" # String
print(my_Variable)

_myVariable = "Hello mohamed" # String
print(_myVariable)

name = "Hello mohamed" # single word => Normal
myName = "Hello mohamed" # two words => camel_case
my_name = "Hello mohamed" # two words => snake_case
print('----------variable 2--------------')


#------ PART2 -------
#
# Source Code : Original Code You Write it in Computer
# Translation : Converting Source Code Into Machine Language 
# Compilation : Translate Code Bfore Run Time  
# Run-Time : Period App Take To Executing commands 
# Interpreted : Code Translated On The Fly During Execution

a = 50
a = "hello"
print(a) # the value of a is "hello" and there is no error 
print('-----------keywords-------------')

# Reserved Words
help("keywords")

b, d, c = 1, 2, 3
print(b); print(d); print(c);
print('------------------------')


print('====================Escape Sequences Characteres ========================')
#=========================================================================








#=========================================================================
# -- Escape Sequences Characters ----
# \b => Back Space
# \newline => Escape New Line + \ 
# \\ => Escape Back Slash
# \' => Escape Single Quote
# \" => Escape Double Quote
# \n => Line Feed
# \r => Carriage Return
# \t => Horizontal Tab
# \xhh => Character Hex Vlue
# \ooo => octal value


# Back Space

print('---------Back Space------------')
print("Hello\bWorld") # Will remove o 
print('----------Escape New Line + \--------------')

# Escape New Line + \
print("Hello \
I Love \
Python")
print('---------Escape Back slash---------------')

# Escape Back slash 
print("Hello World \\") 
print('-----------Espace Single Quote-------------')

# Espace Single Quote
print('I Love Back Slash \'Test\' ') 
print('----------space Double Quote--------------')

# Espace Double Quote
print("I Love Back Slash \"Test\" ") 
print('----------Line Feed--------------')

# Line Feed
print("first line\n second line")# New Line
print('----------Carriage Return--------------')

# Carriage Return
print("123456\rAbcd") 
print('----------Horizontal Tab--------------')

# Horizontal Tab
print("Name\tAge") # Tab
print('----------Character Hex Value--------------')

# Character Hex Value
print('\x4B\x41\x53\x4D\x49') # convert hex to string 
print('---------\ooo => octal value---------------')

# \ooo => octal value
print('\110\145\154\154\157') # convert octal to string 
print('------------------------')


print('=================== Concatenation -----------------------')
#=========================================================================












#=========================================================================
# -- Concatenation ------
print('----------concatenation 01--------------')
msg = "I Love"
lang = "Python"
print(msg +" "+ lang)
print('---------concatenation 02---------------')

full = msg + " " + lang
print(full)
print('----------concatenation 03--------------')

aa = 'Frist \
second \
third'
bb = "A \
B \
C"
print(aa+' '+bb)
print(aa,bb)
print(f"{aa} {bb}")
print('------------------------')

# We cannot concatenate string and int : print(msg + 123) => error


print('==================== String ========================')
# =========================================================================











# #=========================================================================
# --- Strings --------

print('----------affiche de string 01--------------')
myStringOne = 'This is Single Quote'
myStringTwo = "this is Double Quote"

myStringThree = 'This is single Quote "Test" '
myStringFour = "This is Double Quote 'Test' "

myStringFive = """First 
second 'Test' "Test" 
third """ # """ or '''" is used for multi line string

myStringSix = '''four
five 
six '''

print('--------affiche de string 02--------------')
print(myStringOne); print(myStringTwo)
print(myStringThree);print(myStringFour)
print (myStringFive);print(myStringSix)
print('------------------------')


print('==================== String Indexing & Slicing ========================')
#=========================================================================











#=========================================================================
# Strings Indexing & Slicing
# --------------------------------------
# [1] All Data in Python ia Object
# [2] Object Contain Elements 
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero)
# [5] Use Square Brackets To Access Element 
# [6] Enable Accessing Parts of Strings, Tuples or Lists

# Indexing (Access Single Item)

print('----------Indexing--------------')
myString = "I Love Python"
print(myString[0]) # Index 0 => I
print(myString[9]) # Index 9 => t
print(myString[-1]) # Index -1 => n First Character From End
print(myString[-6]) # Index -6 => P 6th character From End 
print('---------slicing 1---------------')

# Slicing (Access Multiple Sequence Item)
# [1] [Start:End] End Not Included 
# [2] [Start:End:Steps]

print(myString[8:11]) # 8:y  9:t  10:h => yth
print(myString[3:5]) # 3:o 4:v => ov
print('----------slicing 2--------------')

print(myString[:10]) # If Start Is Not Here Will start From 0
print(myString[5:]) # If End Is Not Here Will go to end
print(myString[:]) # If Start And End Is Not Here Will return all (Full Data)
print('----------sciling 3--------------')

print(myString[::1]) # Full Data  same [0::1]
print(myString[::2]) # the step is 2 => I l v  y h n => ILv yhn
print('------------------------')


print('=================== Strings Methods ------------------')
#=========================================================================











#=========================================================================
# -- Strings Methods ------------------ 

# ---------PART 01 --------------------------------------

a = "Kasmi Benaoumeur"
b = "    Kasmi Benaoumeur     "
c = "@#@#@#kasmi@#@#@#"
d = "i love 2d graphics and 3d technology and python"
e ,f,g,h = '5' ,'15','111','1111'
i = "kasmi"
j = "KASMI BENAOUMEUR"
k = "kas-mi-ben-aou-meur"
L = "I Love Python and PHP Because PHP is Easy" 
M = """First line 
Second line 
Third line"""
N = "first line \n Second line \n Third line"
O = "Hello\tWorld"
one = "I Love Python And 3G"
two = ""
three = " "
four = "KA-10-BEN"
five = "ka10mi"
P = "Hello one Two Three one one"

print('----------len()-----------------')
# len() is length() in pascal
print(len(a)) # len(a) => 16
print(len(b)) # len(b) => 25
print('----------strip()--------------')

# strip() => Remove All The Spaces and characters From The Start And End 
print(b.strip()) # =>Kasmi Benaoumeur
print(c.strip("@#")) # =>kasmi
print('---------rstrip()---------------')


# rstrip() => Remove All The Spaces and characters From The End 
print(b.rstrip()) # =>    Kasmi Benaoumeur
print(c.rstrip("@#")) # =>@#@#@#kasmi
print('-----------lstrip()-------------')


# lstrip() => Remove All The Spaces and characters From The Start 
print(b.lstrip()) # =>Kasmi Benaoumeur    
print(c.lstrip("@#")) # =>kasmi@#@#@#
print('----------title()--------------')


# title() => Make The First Character Of Each Word and after numbers Capital
print(d.title())
print('----------capitalize()--------------')


# capitalize() => Make The First Character Of The String Capital
print(d.capitalize()) # make sofe I in capital
print('----------zfill()--------------')


# zfill() => Fill The Str With '0' until the len() of the str is equal to the num
print(e); print(e.zfill(2))
print(f); print(f.zfill(3))
print(g); print(g.zfill(3))
print(h); print(h.zfill(5))
print('----------upper()--------------')


# upper() => Make All The Characters Capital
print(i.upper())
print('----------lower()--------------')


# lower() => Make All The Characters Small
print(j.lower())
print('---------split()---------------')




#-------- PART 02 -------------------------------------------------------------
# split() and rsplit() convert string to list


# split() => Split The String By The Character That You Give It .
print(a.split()) # split by space
print(k.split('-'))
print(k.split("-",2)) # split by "-" 
print('----------rsplit()--------------')

# rsplit() => Split The String By The Character From the End That You Give It
print(k.rsplit("-",2))
print('----------splitlines()--------------')

# splitlines() => Split The String By The New Line Character
print(M.splitlines()) # split by new line
print(N.splitlines()) # split by new line
print('----------center()--------------')



# center() => Make The String To Center In The Screen 
print(i.center(9)) # spaces 
print(i.center(9,"8")) # 88kasmi88
print('----------count()--------------')


# count() => Count The Number Of The Characters In The String 

print(L.count('a')) # count(char,start,end),)
print(L.count('Php')) # count(Php) = 0 => because we have PHP not PHp
print(L.count('e',0,6)) # [1-6] => I Love => count(e) = 1
print('----------swapcase()--------------')


# swapcase() => Make The small char to capital and capital to small
print(i.swapcase())
print(L.swapcase())
print('----------startswith()--------------')


# startswith() => Check If The String Start With The Character That You Give It 
print(i.startswith('k')) # true because kasmi start with k
print(L.startswith('a')) # false because L start with I not a
print(L.startswith('v',2,8)) # false because the string [2-8]: Love P start with L not v
print('-----------endswith()-------------')


# endswith() => Check If The String End With The Character That You Give It 
print(i.endswith('i')) # true because kasmi end with i {kasmi}
print(L.endswith('k')) # false because L end with y not k
print(L.endswith('y',2,8)) # false because the string [2-8]: Love P end with P not y 
print('---------index()---------------')




# --------- PART 03 ------------------------------------------------------------------


# index(substring,start,end) => Find The Index Of The Character That You Give It if not find it return error
print(L.index('a')) # return the index of the first a is 14
print(L.index('PHP',14,41)) # return the index of the first PHP is 18 
print(i.index('m')) # return 3 
# if not found it return error => program will stop if the error is found
# like : print(i.index('b')) => error
print('-------- -find()---------------')



# find(substring,start,end) => Find The Index Of The Character That You Give It if not find it return -1
print(L.find('a')) # return the index of the first a is 14
print(L.find('PHP',14,41)) # return the index of the first PHP is 18
print(i.find('b')) # return -1 because kasmi not have b is returne -1
print('----------rfind()--------------')


# rfind(substring,start,end) => Find The Last Index Of The Character That You Give It if not find it return -1
print(L.rfind('a')) # return the index of the last a is 38
print(L.rfind('PHP',14,41)) # return the index of the last PHP is 30 
print(i.rfind('b')) # return -1 because kasmi not have b is returne -1
print('---------rjust() and ljust()---------------')


# rjust(width,fillchar) => Add The Character To The  left Of The String 
print(i.rjust(20,'*')) # => *********kasmi

# ljust(width,fillchar) => Add The Character To The right Of The String 
print(i.ljust(20,'*')) # => kasmi*********
print('---------expandtabs()---------------')


# expandtabs(tabsize) => Add The Tab To The String 
print(O)
print(O.expandtabs(1)) # => space between words is 1
print(O.expandtabs(4)) # => space between words is 4
print('---------istitle()---------------')


# istitle() => Check If The String Is Title(the first char of the word the char after numbers are capital .)
print(i.istitle()) # => False
print(one.istitle()) # => True
print('---------isspace()---------------')


# isspace() => Check If The String Is Space(the char is space)
print(two.isspace()) # => False
print(three.isspace()) # => True
print(O.isspace()) # => False 
print('---------islower()---------------')


# islower() => check if the char of String is small 
print(i.islower()) # true => because i = kasmi small letter
print(j.islower()) # false => because j = KASMI BENAOUMEUR capital
print('---------isupper()---------------')


# isupper() => check if the char of String is capital 
print(i.isupper()) # false => because i = kasmi small letter
print(j.isupper()) # true => because j = KASMI BENAOUMEUR capital letter
print('---------isidentifier()-----------')


# isidentifier() => Check if the String is a valid python identifier
print(i.isidentifier()) # true => because i = kasmi not Include Special Characters
print(five.isidentifier()) # true => because five =ka10mi Include numbers
print(four.isidentifier()) # false => because j = KA--BEN Include Special Characters like (-)
print('----------isalpha()--------------')


# isalpha() => Check if the String Is Only  Characters
print(i.isalpha()) # true => because i = kasmi only alphabetic characters (a-z or A-Z)
print(five.isalpha()) # false => because five =ka10mi Include numbers
print(four.isalpha()) # false => because four = KA-10-BEN Include Special Characters like (-) and number (10)
print('----------isalnum()--------------')


# isalnum() => Check if the string is alphanumeric (a-z or A-Z or 0-9) 
print(i.isalnum()) # true => because i = kasmi only characters (a-z or A-Z)
print(five.isalnum()) # true => because five =ka10mi Include numbers and characters 
print(four.isalnum()) # false => because four = KA-10-BEN Include Special Characters like (-) 



# -----------PART 04 ----------------------------------------------------------------------



print('---------replace()---------------')
# replace(Old value, New Value , Count) => Replace The Old Characters To New Characters for Count Times
print(a.replace("Benaoumeur", "Mohamed")) # => Kasmi Mohamed 
print(P.replace("one", "1")) # => Hello 1 Two Three 1 1 
print(P.replace("one","1",2)) # => Hello 1 Two Three 1 one

print('---------join()-----------------')
# join(Iterable) => Convert Iterable to String whith sepator
mylist = ["Hello", "World", "Two", "Three"] 
print(" ".join(mylist)) # => Hello World Two Three
print(",".join(mylist)) # => Hello,World,Two,Three
print("-".join(mylist)) # => Hello World Two Three
print('====================== String Formatting =========================')
#=========================================================================










#=========================================================================
# --------STRING FORMATTING---------------------


# ---------------PART 01 ------------------------

# %s => String
# %d => Integer
# %f => Float
name,n,l= "Benaoumeur","Kasmi","Python"
age,y = 18,0
rank = 9.5

print('--------%s and %d and %f------- ')
print("My name is : %s " % name)
print("My name is %s and I am %d years old" %(name,age))
print("My name is : %s and My age is : %d and My rank is : %f" %(name,age,rank))
print("My name is %s and Iam %s developer with %d years experience " % (n ,l ,y))



print('-----------Control Floating Point Numbers--------------')
# %.<number>f => Number of digits after the decimal point
mynumber = 10
print("My number is : %d " % mynumber)
print("My number is : %f " % mynumber)
print("My number is : %.2f " % mynumber)



print('-----------Truncate Strings--------------')
# %.<Number>s => Number of characters in the string

mylongstring = "Hello World, I love Python, I love programming"
print("Messagr is : %s" %mylongstring)
print("Messagr is : %.1s" %mylongstring)
print("Messagr is : %.5s" %mylongstring)
print("Messagr is : %.11s" %mylongstring)






# -------------PART 02 ------------------------
# -----------String Formatting New Ways------------------

# {:s} => String
# {:d} => Integer
# {:f} => Float
# {:.<Number>f} => Number of digits after the decimal point
# {:.<Number>s} => Number of characters in the string

print('----------Format () or f"--------------')
print(f"My name is : {name} and My age is : {age}") # the new way of formatting
print(f"My name is : {name:.6s} and My age is : {age} and My rank is : {rank:.3f}")
print("My name is : {} and My age is : {}" .format(name,age)) # the old way of formatting
print("My name is : {:s} and Iam {:d} developer with {:f} years experience " .format(name ,age ,rank)) # the old way of formatting
print("My name is : {:.3s} and Iam {:d} developer with {:.2f} years experience " .format(name ,age ,rank)) # the old way of formatting



# Format Money 
mymoney = 50042488754211799954
print('-----------Format Money-----------------')
print(f"My Money in Bank is :{mymoney :_d}")
print(f"My Money in Bank is :{mymoney :_d}")
print(f"My Money in Bank is :{mymoney :,d}")



# ReArrange Items
a,b,c = "one", "two", "three"

print('-----------ReArrange Items-----------------')
print("The numbers are : {} {} {} " .format(a,b,c))
print("The numbers are : {2} {1} {0} " .format(a,b,c))

x,y,z = 10 ,20 ,30
print("The numbers are : {} {} {} " .format(x,y,z))
print("The numbers are : {1} {2} {0} " .format(x,y,z))



print('=================== Numbers =========================')
# ========================================================================










# ==========================================================================
# ----- Numbers -----
# -------------------


# Integer 
print('-----Integer ------')
print(type(1))
print(type(10))
print(type(100))
print(type(-1))
print(type(-10))
print(type(-100))



# float
print('-----Float ------')
print(type(1.500))
print(type(10.6))
print(type(0.99))
print(type(-1.0))
print(type(-100.807))



# complex
print('-----Complex ------')
mycomplex = 10 + 20j
print(mycomplex)
print(f"Real part : {mycomplex.real}")
print(f"Imaginary part : {mycomplex.imag}")
print(mycomplex.imag)
print(type(1+2j))
print(type(1.2+3j))
print(type(-10+2j))

# [1] You Can Convert From Int To Float or Complex
# [2] You Can Convert From Float To Int or Complex
# [3] You Cannot Convert Complex To Any Type

print('-'*5,'Convert Int To Float & Complex','-'*5)

print(100)
print(float(100))
print(complex(100))
print(complex(100,2))

print('-'*5,'Convert Float To Int & Complex','-'*5)
print(100.62)
print(int(100.62))
print(complex(100.62))
print(complex(100.62,4))

# print(int(10+2j)), Cannot Convert Complex To Any Type

print('=================== Arithmetic Operators =========================')
# ========================================================================
 









# ===========================================================================
# ----------------------------
# --- Arithmetic Operators ---
# ----------------------------
# [+] Addition		    x + y	
# [-] Subtraction		x - y	
# [*] Multiplication	x * y	
# [/] Division		    x / y	
# [%] Modulus			x % y	
# [**] Exponentiation	x ** y	
# [//] Floor Division	x // y
# ----------------------------

# Addition

print('-'*10,'Addition','-'*10)

print("10 + 20 = ",10 + 20)
print("-10 + 30 = ",-10 + 30)
print("1.5 + 20.5 = ",1.5 + 20.5)
print("10 + 20.5j + 30 + 40j = ",10 + 20.5j + 30 + 40j)


# Subtraction

print('-'*10,'Subtraction','-'*10)

print("10 - 20 = ",10 - 20)
print("-10 - 30 = ",-10 - 30)
print("1.5 - 20.5 = ",1.5 - 20.5)
print("(10 + 20.5j) - (30 + 40j) = ",(10 + 20.5j) - (30 + 40j))


# Multiplication

print('-'*10,'Multiplication','-'*10)

print("10 * 2 = ",10 * 2)
print("-2 * 3 = ",-2 * 3)
print("1.5 * 0.5 = ",1.5 * 0.5)
print("(1 + 2j) * (2 + j) = ",(1 + 2j) * (2 + 1j))


# Division

print('-'*10,'Division','-'*10)

print("20 / 10 = ",20 / 10)
print("-6 / 3 = ",-6 / 3)
print("1.5 / 20.5 = ",2.5 / 0.5)
print("(1 + 2j) / (1 + 2j) = ",(1 + 2j) / (1 + 2j))


# Modulus (rest of the division)
print('-'*10,'Modulus','-'*10)

print("20 % 10 = ",20 % 10)
print("25 % 10 = ",25 % 10)
print("-7 % 3 = ",-8 % 3)
print("1.5 % 20.5 = ",1.5 % 20.5)


# Exponentiation (power)
print('-'*10,'Exponentiation','-'*10)

print("2 ** 0 = ",2 ** 0)
print("3 ** 2 = ",3 ** 2)
print("-2 ** 4 = ",-2 ** 4)
print("8 ** 1 = ",8 ** 1)


# Floor Division (The quotient of the division) 
print('-'*10,'Floor Division','-'*10)

print("25 // 10 = ",20 // 10)
print("-6 // 3 = ",-6 // 3)
print("8 // 3 = ",8 // 3)

print('=================== List =========================')
# ===========================================================================















# ============================================================================
# -------------------------------
# --------- List -------------
# -------------------------------
# [1] List Items Are Enclosed In Square Brackets
# [2] List Are Ordered, To Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit 
# [4] List Item Is Not Unique 
# [5] List Can Have Different Data Types 
# -------------------------------

print('-'*10,'List','-'*10)

List1 = [1,2,3,4,5]
List2 = ["one","two","one"] # List Item Not Unique
List3 = [1,"two",3.45,True] # List Item Can Have Different Data Types
print(List1)
print(List2)
print(List3)

print('-'*10,'List Index (Accesse)','-'*10)

print(List1[0]) 
print(List2[1]) 
print(List3[-1]) 

print('-'*10,'List Slicing ','-'*10)

print(List1[0::1]) 
print(List1[0:3:1]) 
print(List3[::2])

print('-'*10,'Change List Item ','-'*10)

List1[4] = 6
print(List1) 

List3[0:2] = []
print(List3)


print('=================== List Methods =========================')
# ============================================================================















# =========================================================================
# -----------------------------
# --- List Methods ------------
# -----------------------------

# ------------- PART 01 ---------------


# append()	Adds an element at the end of the list

print('-'*10,"append",'-'*10)

Myfriends = ["Imad","Mohamed","Nadir","Zino"]
Myoldfriends = ["Kada","Mokhtare","Chihab"]



Myfriends.append("Annis")
print(Myfriends)

Myfriends.append(Myoldfriends)
print(Myfriends)
print(f"index 5 of List Myfriends Is : {Myfriends[5]}")
print(f"the element 2 of the indexe 5 is {Myfriends[5][2]}")



# extend()	Add the elements of a list  to the end of the current list

print('-'*10,"extend",'-'*10)

A, B, C = [1,2,3],["A","B","c"],["One","Two"]
A.extend(B)
print(A)
A.extend(C)
print(A)


# remove()	Removes the first item with the specified value

print('-'*10,"remove",'-'*10)

print('lisrt before remove :',Myfriends)
Myfriends.remove(Myoldfriends)
print('list after remove :', Myfriends) # remove Myoldfriends from the list


# sort()	Sorts the list
print('-'*10,"sort",'-'*10)

E = [10, 5, 2, 8, 1]
print('list after sort',E)
E.sort()
print("list before sort :",E)
E.sort(reverse=False)
print("list before sort with reverse = false :",E)
E.sort(reverse=True) # sort the list in reverse order
print("list before sort with reverse = true :",E)


# reverse()	Reverses list not sort in reverse order
print('-'*10,"reverse",'-'*10)

Z = [10, 1, 9, 80, 100,'Kasmi',100]
Z.reverse()
print("list after reverse :",Z) 


# ---------------- PART 02 -----------------------------


# clear()	Removes all the elements from the list
print('-'*10,"clear",'-'*10)

K = [1,2,3,4,5]
print(K)
K.clear() # clear the list
print(K)


# copy()	Returns a copy of the list
print('-'*10,"copy",'-'*10)

G = [1,2,3,4]
J = G.copy() 

print(G) # Main List 
print(J) # copied List 

J.append(5)
print('Main List :',G)
print('Copied List After append :',J)

# count()	Returns the number of elements with the specified value
print('-'*10,"count",'-'*10)

H = [1,2,3,4,5,1,2,3,4,5]
print(H)
print("The number of 1 in the list is :",H.count(1))

# index()	Returns the index of the first element with the specified value
print('-'*10,"index",'-'*10)

print(H)
print("The index of 3 in the list is :",H.index(3)) # return the index of the first 3 in the list

# insert()	Adds an element at the specified position
print('-'*10,"insert",'-'*10)

L = [1,2,4,5]
print(L)
L.insert(2,3) # insert 3 at index 2
print("List after insert :",L)


# pop()	Removes the element at the specified position
print('-'*10,"pop",'-'*10)

M = [1,2,3,7,4]
print(M)
print(M.pop(3)) # remove the element at index 3
print(M)




print('=================== Tuples =========================')
# ============================================================================













# ============================================================================
# -----------------------------
# --- Tuples ------------

# -----------------------------
# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered, To Use Index To Access Item
# [4] Tuple Are Immutable => You Cant Add or Delete
# [5] Tuple Items Is Not Unique (يمكن أن تحتوي التيبول على عناصر مكررة)
# [6] Tuple Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples
# ------------------------------



# --------------- PART 01 -----------------------------



# Tuple Syntax & Type Test
print('-'*10,'Tuple Syntax & Type Test','-'*10)

myAwesomeTupleOne = ("Benaoumeur", "Morad")
myAwesomeTupleTwo = "Benaoumeur", "Morad"

print(myAwesomeTupleOne)
print(myAwesomeTupleTwo)

print(type(myAwesomeTupleOne))
print(type(myAwesomeTupleTwo))



# Tuple Indexing
print('-'*10,'Tuple Indexing','-'*10)

myAwesomeTupleThree = (1, 2, 3, 4, 5)
print(myAwesomeTupleThree[0])
print(myAwesomeTupleThree[-1])
print(myAwesomeTupleThree[-3])



# Tuple Assign Values
print('-'*10,'Tuple Assign Values','-'*10)

myAwesomeTupleFour = (1, 2, 3, 4, 5)

print('tuple object does not support item assignment (You Cant Add or Delete)')
# myAwesomeTupleFour[2] = "Three"
# print(myAwesomeTupleFour)  # 'tuple' object does not support item assignment



# Tuple Data
print('-'*10,'Tuple Data','-'*10)

myAwesomeTupleFive = ("Osama", "Osama", 1, 2, 3, 100.5, True)
print(myAwesomeTupleFive[1])
print(myAwesomeTupleFive[-1]) 



# --------------- PART 02 -----------------------------


# Tuple With One ELement
print('-'*10,'Tuple With One Element','-'*10)

myTuple1 = ('Benaoumeur') 
myTuple2 = 'Benaoumeur'

print(myTuple1)
print(myTuple2)
print(type(myTuple1))  # <class 'str'>
print(type(myTuple2))  # <class 'str'>
print('\n')
myTuple01 = ('Benaoumeur',) 
myTuple02 = 'Benaoumeur',
print(myTuple01)
print(myTuple02)
print(type(myTuple01))  # <class 'tuple'>
print(type(myTuple02))  # <class 'tuple'>
print('the length of myTuple01 is :', len(myTuple01))  # 1
print('the length of myTuple02 is :', len(myTuple02))  # 1



# Tuple Concatination
print('-'*10,'Tuple Concatination','-'*10)

a = (1, 2, 3)
b = (4, 5, 6)
c = a + b 
e = a + ("A","B","C") + b
print(c)  
print(d)
print(e)



# Tuple, List, String Repeat (*)
print('-'*10,'Tuple, List, String Repeat (*)','-'*10)
myString = "Benaoumeur"
myList = [1, 2]
myTuple = ("A", "B")

print(myString * 3)  # BenaoumeurBenaoumeurBenaoumeur
print(myList *3)    # [1, 2, 1, 2, 1, 2]   
print(myTuple * 3)   # ('A', 'B', 'A', 'B', 'A', 'B')





print('=================== Tuples Methods ==================')
# --------------- METHODS -------------------


# count()	Returns the number of element
print('-'*10,'count()','-'*10)

Q = (1, 2, 3, 4, 5, 5, 7, 9, 5)
print('the number of 5 in the tuple Q is :', Q.count(5))



# index()	Returns the index of the first element which you entered
print('-'*10,'index()','-'*10)

print('the index of 5 in the tuple Q is :', Q.index(5))  # return the index of the first 5 in the tuple
# print(Q.index(10)) => Error => IS Not Found




# Tuple Destruct
print('-'*10,'Tuple Destruct','-'*10)

a = (1, 2, 3)
x,y,z = a 
print(f"x = {x}, y = {y}, z = {z}")





print('======================= Set ==============================')
# ============================================================================















# ============================================================================
# -----------------------------
# -- Set --
# ---------
# [1] Set Items Are Enclosed in Curly Braces {}
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cant Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique
# -----------------------------

# Ordered And Indexed
print('-'*10,'Ordered And Indexed','-'*10)
mySetOne = {"Kasmi", "Morad", 100}
print(mySetOne); print(mySetOne) # Not Ordered => The Order May Change
# print(mySetOne[0]) => Error
print('Set Indexing Cant Be Done')



# Slicing 
print('-'*10,'Slicing','-'*10)

print('Slicing Cant Be Done')
mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:3]) => Error => Slicing Cant Be Done



# Has Only Immutable Data Types
print('-'*10,'Has Only Immutable Data Types','-'*10)

# mySetThree = {"Osama", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list [1,2,3]'
mySetThree = {"Osama", 100, 100.5, True, (1, 2, 3)} # Tuples Are Immutable => Can Be Added To Set
print(mySetThree)

print('Set Has Only Immutable Data Types , List and Dict Are Not')



# Items Is Unique
print('-'*10,'Items Is Unique','-'*10)

mySetFour = {1, 2, "Osama", "One", "Osama", 1}
print(mySetFour) # {1,2,"Osama","One"}





print('=================== Set Methods =========================')
# ============================================================================














# ==============================================================================
# -----------------
# -- Set Methods --
# -----------------



# ------------- PART 01 -----------------


# clear() => Removes all the elements from the set
print('-'*10,'clear()','-'*10)

a = {1,2,3,4}
a.clear()
print(a)


# union() => Merges two or more sets
print('-'*10,'union()','-'*10)

b = {1,2,3} 
c = {"One","Two","Three"}
x = {"Cool","Nice","Good"}

print(b|c) # The First Method
print(b.union(c,x)) # The Second Method


# add() => Adds an element to the set
print('-'*10,'add()','-'*10)

d ={1,2,3,5}
print(d)
d.add(4) # Add 4 to the set
print(d)



# copy () => Returns a copy of the set
print('-'*10,'copy()','-'*10)

print(d)
e =d.copy()
print(e)
d.add(6) 
print('d after add 6 :',d) # d is after add 6
print(e)


# remove() => Remove an element from the set and returns error if not found
print('-'*10,'remove()','-'*10)

print(c)
c.remove("Three")
print(c)
# c.remove(4) => Error => 4 is not in the set


# discard() => remove an element from the set and returns nothing if not found
print('-'*10,'discard()','-'*10)

print(c)
c.discard("Two")
c.discard("Three") # Not Found => No Error
print(c)


# pop() => removes a random element from the set and returns it
print('-'*10,'pop()','-'*10)

print(e)
print(e.pop())
print(e)

# update() => merges the specified set with the current set
print('-'*10,'update()','-'*10)

f ={0,1,2}
f.update(e)
print(f)



# ------------- PART 02 -----------------


# difference() => Returns a set that contains the difference between two or more sets
print('-'*10,'difference()','-'*10) 

print(e)
print(f)
print(f.difference(e)) # f - e =>returns elements that are in f but not in e => {0, 1}
print(e.difference(f)) # e - f =>returns elements that are in e but not in f => empty set
print(e)
print(f)

# difference_update() => Removes the items in this set that are also included in another, specified set
print('-'*10,'difference_update()','-'*10)


print(e)
print(f)
v = e.copy()
e.difference_update(f)
f.difference_update(v)
print(e)
print(f)


# intersection() => returens the items that present in two or more sets
print('-'*10,'intersection()','-'*10)

c.update([1,2,"Four"])
d.add("One")
print(c)
print(d)
print("Intersetion c and d :",c.intersection(d)) # c & d
print("Intersection d and c",d.intersection(c)) # d & c
print(c)
print(d)


# intersection_update() => Removes the items in this set that are not present in other, specified set
print('-'*10,'intersection_update()','-'*10)

v = c.copy()
print(c)
print(d)
c.intersection_update(d) # c & d
d.intersection_update(v) # d & c
print(c)
print(d)


# symmetric_difference() => Returns the item in this set that are not present in other ,and the item in other that are not present in this set
print('-'*10,'symmetric_difference()','-'*10)

p = {1,2,3,"x","kasmi"}
q = {1,2,3,"y","kasmi",5}

print(p)
print(q)
print(p.symmetric_difference(q)) # p ^ q
print(q.symmetric_difference(p)) # q ^ p
print(p)
print(q)


# symmetric_difference_update() => the same of symmetric_difference but update the set with the result
print('-'*10,'symmetric_difference_update()','-'*10)

print(p)
print(q)
v = p.copy()
p.symmetric_difference_update(q) # p ^ q
q.symmetric_difference_update(v) # q ^ p
print(p)
print(q)









# --------------PART 03 -----------------



# issuperset() => returns true if the item of the set 2 is present in the set 1 and false if not
print('-'*10,'issuperset()','-'*10)

a = {1,2,3,4,5}
b = {1,2,3}
c = {1,2,3,6}
print(a.issuperset(b)) # True => a is superset of b => the item of b is present in a
print(a.issuperset(c)) # False => a is not superset of c => the item of c is not present in a


# issubset()=> returns true if the item of the set 1 is present in the set 2 and false if not
print('-'*10,'issubset()','-'*10)


print(a.issubset(b)) # False => a is not subset of b => the item of a is not present in b
print(b.issubset(a)) # True => b is subset of a => the item of b is present in a


# isdisjoint() => returns true if the item of the set 1 is not present in the set 2 and false if not
print('-'*10,'isdisjoint()','-'*10)

e = {10,11,12}
print(a.isdisjoint(b)) # False => a is not disjoint of b => the item of a is present in b
print(a.isdisjoint(e)) # True => a is disjoint of e => the item of a is not present in e






print('===================== dictionary =======================')
# ===========================================================================














# ============================================================================
# -----------------------------
# --- Dictionary --------------
# -----------------------------
# [1] Dict Items Are Enclosed in Curly Braces {}
# [2] Dict Item Are Contains Key : Value 
# [3] Dict Key Need To Be Immutable => (Numbers, Strings, Tuples) List Not Allowed 
# [4] Dict Value Can Be have any Data Type => (Numbers, Strings, Tuples, Lists, Dicts)
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Elements With Key
# -----------------------------


# Dictonary (dict)

user = {
    "name" : "KASMI",
    "age" : 18,
    "Country" : "Algeria",
    "Skills" : ["Python", "Java 0%", "Pascal"],
    "isMarried" : False,
    "My Bac " : 17.41,
    "name" : "Benaoumeur", # Key Is Not Unique => The Last Value Will Be Used
}

note = {
    # ["skills"] : ["Python", "Pascal" ], => Error => List Not Allowed
    (1,2,3) : "Test",
    1 : "One",
}

print('-'*10,'Dictionary','-'*10)
print(user)


print('-'*10,'Accessing Dictionary Items','-'*10)
print(user["Country"])
print(user.get("Country")) 


print('-'*10, 'Accessing Dictionary Keys and Values', '-'*10)
print(user.keys()) # Get All Keys
print(user.values()) # Get All Values


# Two-Dimensional Dictionary
print('-'*10,'Two-Dimensional Dictionary','-'*10)

languages = {
    "One" : {
        "name" : "Python",
        "progress" : '30 %',
    },
    "Two" : {
        "name" : "Java",
        "progress" : "0 %",
    },
    "Three" : {
        "name" : "Pascal",
        "progress" : '90 %', 
    }  
}

print(languages)
print(languages["One"])
print(languages["One"]["name"])


# length of the dictionary
print('-'*10,'Length of the dictionary','-'*10)

print("The Length of Dict 'language' is :",len(languages))
print("The Length of Dict 'user' is :",len(user))
print("The Length of Dict user Skills is :",len(user["Skills"]))

# Create Dictionary From Variables
print('-'*10,'Create Dictionary From Variables','-'*10)

framworkone = {
    "name" : "Mohamed",
    "age" : "12 years",
    "Academic year" : '2AM',  
}
framworktwo = {
    "name" : "El Haje",
    "age" : "5 years",
    "Academic year" :"He doesn't study",
}

framworkthree = {
    "name" : "Islam",
    "age" : "1.5 years",
}

Mybrothers = {
    "One" : framworkone,
    "Two" : framworktwo,
    "Three" : framworkthree,
}

print(Mybrothers)
print(Mybrothers["One"])
print(Mybrothers["One"]["name"])





print('===================== dictionary Methods =======================')
# =======================================================================












# =======================================================================
# -----------------------------
# --- Dictionary Methods ------
# -----------------------------


# ------------- PART 01 -----------------


# clear() => Removes all the elements from the dictionary
print('-'*10,'clear()','-'*10)

main = {
    "name" : "kasmi",
    "age" : 12,
}
print(main.clear()) # None => the dictionary is cleared


# update() => add or update the dictionary with the new key and value
print('-'*10,'update()','-'*10)

member = {
    "name" : "Morad",
}
member["Age"] = 45
member.update({"Country" : "Algeria"})
print(member)

member2 = {
    "JOb" : "Police",
}
member.update(member2) # add member2 to member
print(member)


# copy() => Returns a copy of the dictionary
print('-'*10,'copy()','-'*10)

Myfather = member.copy()
print(member)
Myfather["His Wife"] = "Naima"
print(Myfather)

# keys() + values => Returns a list of all the keys or values in the dictionary
print('-'*10,'keys() + values()','-'*10)

print(Myfather)
print(Myfather.keys())
print(Myfather.values())






# --------------PART 02 -----------------


# setdefault() => Returns the value of the specified key. If the key does not exist, insert the key with the specified value
print('-'*10,'setdefault()','-'*10)

test1 = {
    "name" : "Kasmi",
}
test1.setdefault("name", "Benaoumeur") # If the key "name" does not exist, insert it with the value "Benaoumeur"
print(test1)
test1.setdefault("age", 18) # If the key "age" does not exist, insert it with the value 18
print(test1)


# pop() => Removes the element with the specified key and returns its value
print('-'*10,'pop()','-'*10)

print(test1)
print(test1.pop("age")) # Remove the key "age" and return its value 18
print(test1)


# popitem() => Removes the last inserted key-value and returns it as a tuple
print('-'*10,'popitem()','-'*10)

test1["age"] = 18
test1["country"] = "Algeria"
print(test1)
print(test1.popitem()) # Remove the last inserted key-value and return it as a tuple
print(test1) 


# items() => Returns a list containing a tuple for each key-value pair in the dictionary
print('-'*10,'items()','-'*10)

allitems = test1.items()
test1["age"] = 18
test1["country"] = "Algeria"
print(allitems) 


# fromkeys() => Returns a dictionary with the specified keys and values
print('-'*10,'fromkeys()','-'*10)

a = ["name", "age", "country"]
b = "X"
print(dict.fromkeys(a,b))









print('===================== Boolean =======================')
# ===========================================================================











# ============================================================================
# -----------------------------
# --- Boolean ----------------  
# -----------------------------
# [1] In Programming You Need To Know Your If Your Code Output is True Or False 
# [2] Boolean Values Are The Two Constant Objects False + True
# ------------------------------


name =" "
print(name.isspace())
print()
print(100>200)
print(100>100)
print(100> 90)


# True Values
print("-"*10,"True Values",10*"-")

print(bool("kasmi"))
print(bool(100))
print(bool(100.95))
print(bool(True))
print(bool([1,2,3]))
print(bool({1,2,3}))
print(bool((1,2,3)))
meme ={
    "name" : "Benaoumeur",
    "age" : 18,
}
print(bool(meme))


# False Values
print("-"*10,"False Values",10*"-")

print(bool(False))
print(bool(0))
print(bool(""))
print(bool(''))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(None))








print('===================== Boolean Operators =======================')
# =======================================================================












# =======================================================================
# -----------------------
# -- Boolean Operators --
# -----------------------
# and
# or
# not 
# -----------------------

age = 18
country = "Algeria"
rank = 10

# and
print("-"*10," and ",10*"-")

print(age > 15 and country == "Algeria") # True
print(age > 15 and country == "Algeria" and rank > 2) # True
print(age > 19 and country == "Algeria" and rank > 2) # False


# or
print("-"*10," or ",10*"-")

print(age > 15 or country == "Algeria") # True
print(age > 19 or country == "Algeria" or rank > 20) # True
print(age > 19 or country == "Egypt" or rank > 20) # False


# not
print("-"*10," not ",10*"-")

print(age > 15) # True
print(not age > 15) # Not True = False





print('===================== Assignments Operators =======================')
# ===========================================================================













# ============================================================================
# ----------------------------------
# -- Assignments Operators ---------
# ----------------------------------
# =
# +=
# -=
# *=
# /=
# **=
# %=
# //=
# ----------------------------------


# Assignments Operators '='
print("-"*10,"Assignments Operators '-'",10*"=")

x = 10 # var one 
y = 20 # var two 
x = x + y 
# var one = self [operator +] var two 
print(x)


# Assignments Operators '+='
print("-"*10,"Assignments Operators '+='",10*"-")

x = 10
x+=y
# var one [operator +]= var two
print(x)


# Assignments Operators '-='
print("-"*10,"Assignments Operators '-='",10*"-")

x =10
x = x-y
print(x)
x = 10
x -=y
# var one [operator -]= var two
print(x)
print("Assignments Operators '*=' '/=' '**=' '%=' '//=' It Is Like '+=' and '-='")







print('===================== Comparison Operators  =======================')
# ===========================================================================















# =============================================================================
# ---------------------------
# --- Comparison Operator ---
# ---------------------------
# [ == ] Equal
# [ != ] Not Equal
# [ > ] Greater Than
# [ < ] Less Than
# [ >= ] Greater Than Or Equal
# [ <= ] Less Than Or Equal
# ---------------------------


# Equal [ == ]
print("-"*10,"Equal [ == ]",10*"-")

print(100 == 100)
print(100 == 200)
print(100 == 100.00)


# Not Equal [ != ] 
print("-"*10,"Not Equal [ != ]",10*"-")

print(100 != 100)
print(100 != 200)
print(100 != 100.00)


# Greater than [ > ]
print("-"*10,"Greater Than [ > ]",10*"-")

print(100 > 100)
print(200 > 100)
print(100 > 100.00)


# Less Than [ < ]
print("-"*10,"Less Than [ < ]",10*"-")

print(100 < 100)
print(200 < 100)
print(100 < 100.00)


# Greater Than Or Equal [ >= ]
print("-"*10,"Greater Than Or Equal [ >= ]",10*"-")

print(100 >= 100)
print(100 >= 200)
print(100 >= 100.00)


# Less Than Or Equal [ <= ]
print("-"*10,"Less Than Or Equal [ <= ]",10*"-")

print(100 <= 100)
print(100 <= 200)
print(100 <= 100.00)










print('===================== Type Conversion  =======================')
# ===========================================================================


















# ============================================================================
# ---------------------
# -- Type Conversion --
# ---------------------

# str() 
print("-"*10," str()",10*"-")

a = 10
print(type(a))
print(a)
print(type(str(a)))
print(a)


# tuple()
print("-"*10,"tuple ()",10*"-")

b = "Benaoumeur" # string
d = [1, 2, 3, 4, 5]  # List
e = {"A", "B", "C"}  # Set
f = {"A": 1, "B": 2}  # Dictionary

print(tuple(b))
print(type(b))

print(tuple(c))
print(type(c))

print(tuple(d))
print(type(d))

print(tuple(e))
print(type(e))

print(tuple(f))
print(type(f))

# list() =>
print("-"*10,"list ()",10*"-")

c = "Benaoumeur"  # String
d = (1, 2, 3, 4, 5)  # Tuple
e = {"A", "B", "C"}  # Set
f = {"A": 1, "B": 2}  # Dictionary

print(list(c))
print(type(c))

print(list(d))
print(type(d))

print(list(e))
print(type(e))

print(list(f))
print(type(f))



# set()
print("-"*10,"set ()",10*"-")

c = "Benaoumeur"  # String
d = (1, 2, 3, 4, 5)  # Tuple
e = ["A", "B", "C"]  # List
f = {"A": 1, "B": 2}  # Dictionary

print(set(c))
print(type(c))

print(set(d))
print(type(d))

print(set(e))
print(type(e))

print(set(f))
print(type(f))


# dict()
print("-"*10,"dict ()",10*"-")

d = (("A", 1), ("B", 2), ("C", 3))  # Tuple
e = [["One", 1], ["Two", 2], ["Three", 3]]  # List

print(dict(d))
print(dict(e))







print("================= User Input =========================")
# ===========================================================================

















# ==============================================================================
# ----------------------
# ----- User Input -----
# ----------------------

fName = input('What\'s Your First Name ?').strip().capitalize()
lName = input('What\'s Your Last Name ?').strip().capitalize()

print(f"Hello {fName} {lName} Happy To See You.")






print("================= Practical Slice Email =========================")
# ===========================================================================

















# ==============================================================================
# ---------------------------
# -- Practical Slice Email --
# ---------------------------

theName = input('What\'s Your Name ?').strip().capitalize()
theEmail = input('What\'s Your Email ?').strip()
print(f"Hello {theName}, Your Email Is {theEmail}")
theUsername = theEmail[:theEmail.index("@")]
theWebsite = theEmail[theEmail.index("@")+1:]
print(f"Your Username Is {theUsername} \n Your Website Is {theWebsite}")





print("================= Practical Your Age Full Details =========================")
# ===========================================================================
















# ==============================================================================
# ---------------------------------------
# --- Practical Your Age Full Details ---
# ---------------------------------------

theAge = int(input('What\'s Your Age ?').strip())
AgeM = theAge * 12
AgeW = theAge *(365.25/7)
AgeD = AgeW *7
AgeH =  AgeD*24
AgeMin = AgeH *60
AgeSec = AgeMin *3600

print(f"Your Age In Years Is {theAge} \n \
       Your Age In Months Is {AgeM} \n \
       Your Age In Weeks Is {AgeW} \n \
       Your Age In Days Is {AgeD} \n \
       Your Age In Heurs Is {AgeH} \n \
       Your Age In Minutes Is {AgeMin} \n \
       Your Age In Seconds Is {AgeSec} \
   ")




print("================= Control Flow / If, Elif, Else / Make Decisions / Nested If =========================")
# ===========================================================================














# ==============================================================================
# ----------------------
# ---- Control Flow ----
# --- If, Elif, Else ---
# ---- Make Decision ---
# ----- Nested If ------
# ----------------------

uName = input("What's Your Name ?").strip().capitalize()
uCountry = input("What's Your Country ?").strip().capitalize()
isStudent = input("Are You A Student ? (Yes/No) ").strip().lower()
cName = "Python Course"
cPrice = 100


if uCountry == "Algeria" :
    if isStudent == "yes" :
        print("hello {uName} Because You Are From Algeria and Student, You Get Discount 40 $")
        print(f"The Course \"{cName}\" Price Is : {cPrice - 40} $ ")
    else : 
        print("hello {uName} Because You Are From Algeria, You Get Discount 30 $")
        print(f"The Course \"{cName}\" Price Is : {cPrice - 30} $ ")
elif uCountry == "Morocco" or uCountry == "Tunisia":
    if isStudent == "yes" :
        print(f"hello {uName} Because You Are From {uCountry} and student, You Get Discount 25 $")
        print(f"The Course \"{cName}\" Price Is : {cPrice - 25} $ ")
    else :
        print(f"hello {uName} Because You Are From {uCountry}, You Get Discount 20 $")
        print(f"The Course \"{cName}\" Price Is : {cPrice - 20} $ ")
else :
    if isStudent == "yes" :
        print(f"hello {uName} , You Get Discount 15 $")
        print(f"The Course \"{cName}\" Price Is : {cPrice - 15} $ ")
    else :
        print(f"hello {uName} , You Get Discount 10 $")
        print(f"The Course \"{cName}\" Price Is : {cPrice - 10} $ ")





print("================= Ternary If =========================")
# ===========================================================================














# ==============================================================================
# --------------------------------
# -- Ternary Condition Operator --
# --------------------------------

country = input("What's Your Country ?").strip().capitalize()
if country == "Algeria" :
    print(f"The Weather In {country} Is 40")
elif country == "Morocco" :
    print(f"The Weather In {country} Is 32")
elif country == "Tunisia" :
    print(f"The Weather In {country} Is 30")
else :
    print("Country Is Not In The List")

# Short if 
print("-"*10,"Short if",10*"-")

movieRate = 18
age = int(input("What's Your Age ?").strip())

if movieRate <= age :
    print("You Can Watch This Movie") # condition is True
else :
    print("You Can't Watch This Movie") # condition is False

print("You Can Watch This Movie" if movieRate <= age else "You Cant Watch This Movie")
# Condition if True | If Condition | Else | Condition if False







print("================= Calculate Age Advanced Version and Training ===================")
# ===========================================================================















# ==============================================================================
# -----------------------------------
# -- Calculate Age Advanced Version -
# -----------------------------------

# Collect Age Data
age = int(input("Please Write Your Age :").strip())

# Collect Time Unit Data
unit = input("Please Choose Time Unit : (Months,Weeks,Days)").lstrip().lower()

# Get Time Unit
if unit == "months" :
    print("Your Age In Months Is :",age *12)
elif unit == "weeks" :
    print("Your Age In Weeks Is :",age *(365.25/7))
elif unit == "days" :
    print("Your Age In Days Is :",age * 365.25)
else :
    print("You Not Choose A Valid Time Unit")




print(" Membership Operators ".center(80,'='))
# =============================================================================














# ==============================================================================
# -------------------------------
# --- Membership Operators ------
# -------------------------------
# [in] => Returns True If The Value Is In The Sequence
# [not in] => Returns True If The Value Is Not In The Sequence
# -------------------------------

# String
name = "Kasmi"
print("k" in name) # True => k is in name
print("A" in name) # False => A is not in name
print("s" not in name) # False => s is in name


# List 
friends = ["Morad", "Islam", "Benaoumeur"]
print("Morad" in friends) # True => Morad is in friends
print("Benaoumeur" not in friends) # True => Benaoumeur is in friends
print("sayed" in friends) # False => Kasmi is not in friends
print("Islam" not in friends) # False => Islam is in friends

# Using In and Not In With If Condition

countriesOne = ["Algeria", "Morocco", "Tunisia"]
countriesTwo = ["France", "Spain", "Italy"]
YourCountry = input("What's Your Country ?").strip().capitalize()

if YourCountry in countriesOne:
    print(f"{YourCountry}, You Are From Africa")
elif YourCountry in countriesTwo:
    print(f"{YourCountry}, You Are From Europe")
else:
    print(f"{YourCountry}, You Are From Another Continent")







print(" Practical Membership Operators ".center(80,'='))
# =============================================================================














# ==============================================================================
# --------------------------------------
# -- Practical Membership Operators ----
# --------------------------------------

# List Contains Admins
admins = ["Kasmi Benaoumeur","Imad","Morad","Islam","Fatima","Chaima"]
# Login
name = input("What's Your Name ?").strip().title()
# If Name is In Admins
theBoss = "Kasmi Benaoumeur"
if name == theBoss:
    code = 13122006
    inputcode = int(input("Please Enter Your Code : ").strip())
    if inputcode == code:
        print("Hello Boss, Welcome Back")
        option = input("Delete Or Update The Admins List ?").strip().capitalize()
        if option == "Update":
           choice = input("You Would To Add New Admin Or Update An Name ? (ADD/UPD_N) ").strip().lower() 
           if choice == "add":
                Newadmin = input("What's The New Admin Name ?").strip().capitalize()
                admins.append(Newadmin)
           elif choice == "upd_n":
               oldname = input("What's The Old Admin Name ?").strip().capitalize()
               if oldname in admins:
                    Newname = input("What's The New Admin Name ?").strip().capitalize()
                    admins[admins.index(oldname)] = Newname
                    print(f"Your Name Has Been Updated To {Newname}")
                    print("Admins List : ", admins)
               else : 
                    print(f"{oldname} Is Not In The Admins List")
                
                
else :
    if name in admins :
        print(f"Hello {name} Welcome Back")
        option = input("Delete Or Update Your Name ?").strip().capitalize()
        if option == "Update":
            Newname = input("What's Your New Name ?").strip().capitalize()
            admins[admins.index(name)] = Newname
            print(f"Your Name Has Been Updated To {Newname}")
        elif option == "Delete":
            admins.remove(name)
            print(f"Your Name {name} Has Been Deleted From Admins, You Are Not An Admin Now")
            choice = input("You Would To Show The Admins List ? (Yes/No)").strip().lower()
            if choice == "yes":
                print("Admins List : ", admins)
            else:
                print("Thank You For Using Our Program")
        else:
            print("You Not Choose A Valid Option")
    else :
        print(f"Hello {name},You Are Not An Admin")
    









print("Loop => While ".center(80,'='))
# ====================================================================


















# =======================================================================
# -------------------
# -- Loop => While --
# -------------------
# While Condition_is_True
#     Code Will Run

a = 0
while a <= 10:
    print(a) 
    a += 1

else : print("Loop Is Done")



# -------------------------------
# -- Loop => While Training 01 --
# -------------------------------
print("While Training 01".center(50,"-"))


myF = ["Im","Go","Na","Ka","Mo","Ah","Ha","Is","Mor","Cha"]
i = 0
while i <len(myF):
    print(f"# {str(i+1).zfill(2)} - {myF[i]}")
    i +=1
else: print("All Friends Printed To Screen. ")
 















# --------------------------------
# -- Loop => While Training 02 ---
# -- Simple Bookmark Manage ------
# --------------------------------
print("While Training 02".center(50,'-'))


# Empty List To Fill Later 
myFavouritWebs = []  
# Maximum Allowed Websites 
maximumWebs = 5

while maximumWebs > 0 :
    newWibs = input("enter An new Website Without https:// ").strip().lower()
    newWibs = "https://"+ newWibs 
    if newWibs in myFavouritWebs :
        print("The Website is available in The List .")
        print(myFavouritWebs)
    else: 
        myFavouritWebs.append(newWibs)
        choice = input("Do You Want To Look Your Favourit Websit List : (yes / no) ?").strip().lower()
        if choice == "yes" :
            myFavouritWebs.sort()
            print(myFavouritWebs)
        else :
            print("Thank You For Your Time")
    maximumWebs -= 1
print(f"The List Of My Favourit Webs : {myFavouritWebs}")

# Check If List Is Not Empty
if len(myFavouritWebs) == 0 :
    print("The List Is Empty.")
else :
    print("The List Is Not Empty.")
    












# --------------------------------
# -- Loop => While Training 03 ---
# -- Simple Password Guess -------
# --------------------------------
print("While Training 03".center(50,'-'))



tries = 5
mainpassword = 13122006
inputpassword = int(input("Enter The Password : ").strip())

while tries != 1 and inputpassword != mainpassword :
    tries -=1
    print("The Password Is Incorrect . Please Try Agian")
    print(f"You Have {"Last" if tries == 1 else tries} Tries")
    inputpassword = int(input("Enter The Password : ").strip())
else :
    if inputpassword == mainpassword :
        print("Correct Password") 
    elif tries == 1 :
        print("Sorry, You Don't Have Another Tries ")









print("Loop For And Else ".center(80,'='))
# ====================================================================


















# =======================================================================
# -------------------------------
# --- Loop => For ---------------
# -------------------------------
# for item in iterable_object :
#   Do Something With Item
# -------------------------------
# item Is A Variable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
#  Iterable_object => Sequence [ list , tuples , set , dict , string or charactere , etc ...]
#------------------------------------------------------

myNumber = [1,2,3,4,5,6,7,8,9]
print(myNumber)
EvenNum = []
OddNum = []
for number in myNumber :
    if number % 2 == 0 :
        EvenNum.append(number)
        EvenNum.sort()
    else :
        OddNum.append(number)
        OddNum.sort()
else : 
    print("The Loop Is Finished")

print(f"The List OF Even Number Is :{EvenNum}")
print(f"The List OF Odd Number Is :{OddNum}")

myName = "Benaoumeur"

for char in myName :
    print(char)







# -------------------------------
# -- Loop => For ----------------
# ------- Trainings -------------
# -------------------------------
print("For Trainings".center(50,'-'))


# Rang

myRang = range(1,100) 
for number in myRang :
    print(number)


# Dictionary 

mySkills ={
    "Html" : "10%",
    "Css" : "20%",
    "Java" : "30%",
    "Python" : "40%",
    "Pascal" : "50%",
}
for skill in mySkills :
    print(f"My Progress in Lang {skill} Is: {mySkills.get(skill)}")







# -------------------------------
# -- Loop => For ----------------
# -- Nested Loop -------------
# -------------------------------
print("Nested Loop (For in For)".center(50,'-'))

peoples = ["Osama","Ahmed","Sayed","Ali"]
skills = ["Html","Css","Java"]

for name in peoples : # Outer Loop 
    print(f"{name} Skills Is : ")
    for skill in skills : # Inner Loop
        print(skill)

peoples = {
  "Osama": {
    "Html": "70%",
    "Css": "80%",
    "Js": "70%"
  },
  "Ahmed": {
    "Html": "90%",
    "Css": "80%",
    "Js": "90%"
  },
  "Sayed": {
    "Html": "70%",
    "Css": "60%",
    "Js": "90%"
  }
}


for name in peoples :
    print(f"Skills and Progress For {name} Is :  ")
    for skill in peoples[name] :
        print(f"{skill.upper( )} : {peoples[name][skill]}")
        





print("Break, Continue, Pass ".center(80,'='))
# ====================================================================


















# =======================================================================
# -------------------------------
# -- Break, Continue, Pass ------
# -------------------------------

myNumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]

# Continue 
print("continue".center(50,'-'))

for number in myNumbers :
    if number == 13 :
        continue
    print(number)    


# break
print("break".center(50,'-'))

for number in myNumbers :
    if number == 13 :
        break
    print(number)


# pass
print("pass".center(50,'-'))

for number in myNumbers :
    if number == 13 :
        pass 
    print(number)







print("Advance Dictionary Loop ".center(80,'='))
# ====================================================================


















# =======================================================================
# -------------------------------
# -- Advance Dictionary Loop ----
# -------------------------------

mySkills = {
  "HTML": "80%",
  "CSS": "90%",
  "JS": "70%",
  "PHP": "80%"
}

# print(mySkills.items())
for key, value in mySkills.items() :
    print(f"{key} => {value}")




myUltimateSkills = {
  "HTML": {
    "Main": "80%",
    "Pugjs": "80%"
  },
  "CSS": {
    "Main": "90%",
    "Sass": "70%"
  }
}

for main_key,main_value in myUltimateSkills.items() :
    print(f"{main_key} Progress Is ")
    for key,value in main_value.items() :
        print(f"- {key} => {value}")







print("Function".center(80,'='))
# ====================================================================


















# =======================================================================
# -------------------------------
# -- Function And Return --------
# -------------------------------
# [1] A Function is A Reusable Block Of Code Do A Task
# [2] A Function Run When You Call It
# [3] A Function Accept Element To Deal With Called [Parameters]
# [4] A Function Can Do The Task Without Returning Data
# [5] A Function Can Return Data After Job is Finished
# [6] A Function Create To Prevent DRY
# [7] A Function Accept Elements When You Call It Called [Arguments]
# [8] There's A Built-In Functions and User Defined Functions
# [9] A Function Is For All Team and All Apps
# --------------------------------

                       
def function_name() :
    return"Hello Python From Inside Function"

DataFromFunction = function_name()
print(DataFromFunction)







# ---------------------------------------
# -- Function Parameters And Arguments --
# ---------------------------------------
print("Function Parameters And Arguments".center(50,'-'))

a, b, c = "Osama", "Ahmed", "Sayed"

# def                         => Function Keyword [Define]
# say_hello                   => Function Name
# name                        => Parameter
# print(f"hello {name}")      => Task
# say_hello(a)                => a  Is The Argument

def say_hello(name):
    print(f"hello {name}")

say_hello(a)
say_hello(b)
say_hello(c)


def addition(n1,n2) :
    if type(n1) == str or type(n2) == str :
        print("Only Integers Allowed")
    else : 
        print(f"{n1} + {n2} = {n1+n2}")

addition("40",20)
addition(13,28)


def full_name(first,last):
    print(f"Hello {first.strip().upper():.1s}.{last.strip().capitalize()}")
    
full_name("kasmi","benaoumeur")








# -------------------------------------------------
# -- Function Packing, Unpacking Arguments *Args --
# -------------------------------------------------
print(" Function Packing, Unpacking Arguments *Args ".center(50,"-"))

myList = [1,2,3,4]
print(myList)
print(*myList)

def say_hello(*peoples) :
    for name in peoples :
        print(f"Hello {name}")

say_hello("Benaoumeur","Mohamed","El_Haje")

def show_details(name,*skills) :
    print(f"Hello {name} Your Skills Is: ")
    for skill in skills :
        print(skill)

show_details("Osama", "Html", "CSS", "JS")
show_details("Ahmed", "Html", "CSS", "JS", "Python", "PHP", "MySQL")






# ---------------------------------
# -- Function Default Parameters --
# ---------------------------------
print(" Function Default Parameters ".center(50,"-"))


def say_hello(name ='Unknown',age ='Unknowm',country ='Unknown'):
    print(f"Hello {name} Your Age Is {age} And Your Country Is {country}")

say_hello('Benaoumeur',18,'Algeria')
say_hello('Benaoumeur',18)
say_hello('Benaoumeur')
say_hello()




# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# ----------------------------------------------------
print(" Function Packing, Unpacking Arguments **KWArgs ".center(50,"-"))

def show_skills(*skills):
    print(type(skills))
    for skill in skills :
        print(f"{skill}")

show_skills("Html", "CSS", "JS")



mySkills = {
  'Html': "80%",
  'Css': "70%",
  'Js': "50%",
  'Python': "80%",
  "Go": "40%"
}

def show_skills(**skills):
    print(type(skills))
    for key,value in skills.items() :
        print(f"{key} => {value}")

show_skills(**mySkills)
show_skills(java ="60%", pascal = "20%")






# -----------------------------------------------------
# -- Function Packing, Unpacking Arguments Trainings --
# -----------------------------------------------------
print(" Function Packing, Unpacking Arguments Trainings ".center(50,"-"))


myTuple = ("Html", "CSS", "JS")

mySkills = {
  'Go': "80%",
  'Python': "50%",
  'MySQL': "80%"
}

def show_skills(name,*skills,**progress): # if we not have skills or progress ,the function is work because we use * and **
    print(f"Hello {name} \nYour Skills Without Progress Is :")
    for skill in skills :
        print(f"- {skill}")
    print("Skills With Progress Is :")
    for key,value in progress.items():
        print(f"{key} => {value}")

show_skills("Kasmi",*myTuple,**mySkills)









# --------------------
# -- Function Scope --
# --------------------
print(" Function Scope ".center(50,"-"))


x = 1  # Global Scope
def one():
    x = 2
    print(f"Print Variable From Function scope {x}")

def two():
    # x = 4
    print(f"Print Variable From Function scope {x}")

def three():
    x = 4
    print(f"Print Variable From Function scope {x}")

print(f"Print Variable From Global scope {x}")
one()
two()
three()

print("------------------")
def One():
    global x
    x = 2
    print(f"Print Variable From Function scope {x}")

def Two():
    x = 10
    print(f"Print Variable From Function scope {x}")

One()
print(f"Print Variable From Global scope {x}")
Two()
print(f"Print Variable From Global scope After One Function Is Called {x}")












# ------------------------
# -- Function Recursion --
# ------------------------
# ---------------------------------------------------------------------
# -- To Understand Recursion, You Need to First Understand Recursion --
# ---------------------------------------------------------------------
print(" Function Recursion ".center(50,"-"))



# Test Word [ WWWoooorrrldd ] # print(x[1:])

def cleanword(word):

    if len(word) == 1 :

        return word
    
    print(f"Print Start Function {word}")
    
    if word[0] == word[1] :

        print(f"Print Before Condition {word}")

        return cleanword(word[1:])
    
    print(f"Print Before Return {word}")
    
    return word[0] + cleanword(word[1:])

# Stash [ World ]
print(cleanword("WWWoooorrrldd"))


# -------------------------
# - Exercice From Chatgpt -
# -------------------------
print(" Exercice From Chatgpt (Function Recursion) ".center(70,"-"))

def factoriel(n):
    if n == 0 :
        return 1
    elif n == 1 :
        return n
    else :
        return n * factoriel(n-1) 

print(factoriel(6))


def countdown(n) :
    if n == 1 :
        return "- 1"
    else :
        return f"- {n}\n{countdown(n-1)}"

print(countdown(8))


def sum_rec(n) :
    if n == 0 :
        return 0
    else :
        return n + sum_rec(n-1)

print(sum_rec(9))


def count_char(string,char) :
    count = 0
    if len(string) == 0:
        print("enter string please")
    elif len(string) == 1 :
        if string == char :
            return 1
        else : 
            return 0
    else :
        if string[0] == char :
            count += 1
            return count + count_char(string[1:],char)
        else :
            return 0 + count_char(string[1:],char)
    
print(count_char("banana", "a"))


def reverse(string) :
    if len(string) == 0 :
        print("enter string please")
    elif len(string) == 1 :
        return string
    else :
        return string[-1] + reverse(string[:-1])
    
print(reverse("hello"))


def fibonacci(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))
print(fibonacci(7))






# ------------------------
# -- Function => lambda --
# -- Anonymous Function --
# ------------------------
# [1] It Has No Name
# [2] You Can Call It Inline Without Defining It
# [3] You Can Use It In Return Data From Another Function
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda is One Single Expression not Block Of Code
# [6] Lambda Type is Function
# -------------------------------------------------------------------

print(" lambda Function ".center(50,"-"))

def say_hello(name,age) : return f"Hello {name} Your Age Is {age}"

hello = lambda name,age : f"Hello {name} Your Age Is {age}"

print(say_hello("Benaoumeur",18))
print(hello("Benaoumeur",18))

print(say_hello.__name__) # __name__  => Display The Function Name
print(hello.__name__) # __name__  => Display The Function Name

print(type(hello)) # <class 'function'> => lambda is a function











# -------------------
# -- File Handling --
# -------------------
# "a" => Append  Open File For Appending Values, Create File If Not Exists
# "r" => Read    [Default Value] Open File For Read and Give Error If File is Not Exists
# "w" => Write   Open File For Writing, Create File If Not Exists
# "x" => Create  Create File, Give Error If File Exists
# --------------------------------------------------
print(" File Handling ".center(50,"-"))



import os # os module is used to interact with the operating system

print(os.getcwd()) # Get Current Working Directory

print(os.path.dirname(os.path.abspath(__file__))) # Get Current File Directory

print(os.path.abspath(__file__)) # Get Current File Full Path

os.chdir(os.path.dirname(os.path.abspath(__file__))) # Change Current Working Directory To Current File Directory
print(os.getcwd())

# ex
file = open("source for lerne.txt")
file1 = open("C:\\course\\python\\source for lerne.txt")




























































































print('===================== THE END OF THE COURSE  =======================')
# ===========================================================================