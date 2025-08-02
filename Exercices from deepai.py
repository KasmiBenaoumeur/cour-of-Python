# Exercices From Deepai :


# Exercice 01 :

print("-------- exercice 01 : --------")

student = {
    "name" : str(input("enter your name :")) ,
    "age" : int(input("enter your age :")),
    "skills" : list(input("enter your skills :").split()),
    "isMarried" : input("You are Married : (yes or no) ")
}

print(student.get("name"))
print(student)
new_skills = input("enter your skills :").split()
student["skills"] += new_skills
student["skills"] = list(set(student["skills"]))
print(student)

if student["age"] >= 18 :
    print("Congratulation, I'm dealing with a big person. I need to adjust my position.")
else :
    print("What are you doing here kid go study")

print(type(student["skills"]))
var = student.values()

if student["name"] == "Ali" :
    print("hello Ali, I was waiting for you")
else : 
    print("you are not Ali")

    

# Exercice 02 :
print("-------- exercice 02 : --------")

Books ={
    "book_one" : {
        "author" : str(input("enter the name of author : ")),
        "year" : int(input("enter the year of publication : ")),
        "pages" : int(input("enter the number of pages : "))
    },
}

print(sorted(Books.keys()))

choice = str(input(" Do you want to enter a new book : "))
if choice == "yes" :
    book_two = {
        "author" : str(input("enter the name of author : ")),
        "year" : int(input("enter the year of publication : ")),
        "pages" : int(input("enter the number of pages : "))
    }
    Books.update(book_two)
else : print("thanks you, I won't get tired")

print("You've tired yourself out for no reason because I'll delete what put in ")
Books.popitem()
print(Books)

print(Books.values())






# Exercice 03 :
print("-------- exercice 03 : --------")


# Question 01 :
print("Question 01 : ")

x = 10
y = 17.41
z = "Benaoumeur"
print(type(x))
print(type(y))
print(type(z))
my_list = [1,2,3]
my_set = {"Ali","Sara"}
print(type(my_list))
print(type(my_set))
print(my_list)
print(my_set)
my_dict ={ "name" : "Benaoumeur","age" : 18}
print(type(my_dict))
print(my_dict)


# Question 02 :
print("Question 02 : ")

a = 16 # age of my brother
b = 13 # age of my sister
print(a+b)
"""
for coment in one line we use # 
and for multiple line we use """"""
the diferent is # use to write small comment like write the role of loop 
and """""" is to write text coment 
"""


# Question 03 :
print("Question 03 : ")

my_str = " kasmi benaoumeur "
print(len(my_str))
new_str =my_str.strip()
print(len(new_str))
print(new_str.title())
new_str2=my_str.replace("benaoumeur","EL Haje")
print(new_str2)
print(my_str.split())
print(new_str[0])



# Question 04 :
print("Question 04 : ")

num1 = 15
num2 = 4

som = num1 + num2
sub = num1 - num2 
mul = num1 * num2 
div = num1 / num2
print(num1,"+",num2,"=",som)
print(num1,"-",num2,"=",sub)
print(num1,"*",num2,"=",mul)
print(num1,"/",num2,"=",div)
force = num2 ** 4
print(num2,"** 4 =",force)
mod = num1 // num2
print(num1,"//",num2,"=",mod)


# Question 05 :
print("Question 05 : ")

fruits = ["apple","banana","cherry"]
fruits.append("orange")
print(fruits)
fruits.extend(["kiwi","melon"])
print(fruits)
fruits.remove("banana")
print(fruits)
fruits[-1] = "strawberry"
print(fruits)



# Question 06 :
print("Question 06 : ")

my_tuple = (1,2,3,4,5)
print(my_tuple[4])
print(my_tuple.count(3))
# my_tuple[0] = 5 => Error
print(my_tuple)

t =(6,)
tuples2 = my_tuple + t
print(tuples2)



# Question 07 :
print("Question 07 : ")

A = {1,2,3}
B = {3,4,5}
print(A.union(B))
print(A|B)
A.update(B)
print(A)
print(A.intersection(B))
A.add(6)
print(A)
A.discard(7)
print(A.pop())
print(A)



# Question 08 :
print("Question 08 : ")

student ={
    "name" : "Benaoumeur",
    "age" : 18,
    "skills" : ["python","java","pascal"],
}

print(student["name"])
print(student.get("name"))
student.setdefault("grade", 90)
student.update({"country" : "Algeria" , "my father" : "morad", "my mother" : "naima"})
print(student)
student.pop("skills")
print(student)

A = {"1","2","3"}
b = "x"
print(dict.fromkeys(A,b))

