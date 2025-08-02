# ============ Ex 3: (19-25) ========================


# ----------------------- Task 01: (19-20) ---------------------------------
print('=================== Task 01 ==================')

# Question 01
print('Question 01 :')

a = 10
b = 10.52
c = 10 + 2j

print(a); print(b); print(c)
print(type(a)); print(type(b)); print(type(c))

# Question 02
print('Question 02 :')

print(f'The Imaginary Of number 10 + 2j Is: {c.imag}')
print(f'The Real Of number 10 + 2j Is: {c.real}')

# Question 03
print('Question 03 :')

print(f'Floating Point Number Of 10 With 12 digit Is: {a :.10f} ')

# Question 04
print('Question 04 :')

e = 159.650
e = int(e)
print(e)
print(type(e))

# Question 05
print('Question 05 :')

print(100-115)
print(50*30)
print(21 % 4)
print(110 // 11)
print(97//20)

# ----------------------- Task 02: (21-23) ---------------------------------
print('=================== Task 02 ==================')

# Question 01
print('Question 01 :')

List = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(List)
print(List[0])
print(List[-5])

print(List[4])
print(List[-1])

# Question 02
print('Question 02 :')

print(List[0::2])
print(List[1::2])

# Question 03
print('Question 03 :')

print(List[1:4])
print(List[-2:])


# Question 04
print('Question 04 :')

List[3:] = ['Elzero','Elzero']
print(List)

# Question 05
print('Question 05 :')

friends = ["Osama", "Ahmed", "Sayed"]
print(friends)
friends.insert(0,'Nasser')
print(friends)
friends.append('Salem')
print(friends)

# Question 06
print('Question 06 :')

"""
Cofriends = friends[2:4]
friends.clear()
friends = Cofriends.copy()
Cofriends.clear()
"""

friends.remove("Nasser")
friends.remove("Osama")
friends.pop(-1)

print(friends)

# Question 07
print('Question 07 :')

employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends)

# Question 08
print('Question 08 :')

friends.sort()
print(friends)
friends.sort(reverse =True)
print(friends)

# Question 09
print('Question 09 :')

print(len(friends))


# Question 10
print('Question 10 :')

technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[-1][0])
print(technologies[-1][-1])

# ----------------------- Task 03: (24-25) ---------------------------------
print('=================== Task 03 ==================')

# Question 01
print('Question 01 :')

tuplee = "Benaoumeur",
print(tuplee[0])
print(type(tuplee))

# Question 02
print('Question 02 :')

Newfriends = ("Osama", "Ahmed", "Sayed")
Newfriends = list(Newfriends)
Newfriends[0] = "Elzero"
Newfriends = tuple(Newfriends)
print(Newfriends)
print(type(Newfriends))
print(len(Newfriends),'Elements')

# Question 03
print('Question 03 :')

nums = (1,2,3)
letters = ("A","B","C")
NewTuple = nums + letters
print(NewTuple)
print(len(NewTuple))

# Question 04
print('Question 04 :')

my_tuple = (1, 2, 3, 4)
x,y, _,z = my_tuple
print(x); print(y);print(z); 
print(f'X={x} ,Y={y} ,Z={z}')
