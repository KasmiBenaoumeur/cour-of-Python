
# Exercice 01 :
print("Exercice 01".center(50,"="))

# First Name: Kasmi 
# Last Name: Benaoumeur
# Email: benoumeurkasmi@gmail.com
# Date: 27/05/2025
# Project Name: User Info Manager


# Welcome Message
print("="*50)
print("Welcome to the User Info Manager")
print("="*50)

# enter User Information 
name = input("Enter Your Name :")
age = int(input("enter Your Age :").strip())
country = input("Enter Your Country :")

print('-'*25)

# delete spaces 
print(f"Your Name without spaces :{name.strip()}")
print(f"Your Age without spaces :{age}")
print(f"Your Country without spaces :{country.strip()}")

print('-'*25)

# save name with small letter and capital letter

nameCapi = name.upper()
nameSmal = name.lower()
print(nameCapi); print(nameSmal)

print('-'*25)

# the number of string
print(f"The Number Of Letter In Your Name Without Spaces Is: {len(name.strip())} ")

# the first and last Letter in the name 
print(f"The First Letter In Your Name Is: \"{name[0]}\", And The Last Letter Is: \"{name[-1]}\"")

print('-'*25)

# print the first three and the last three letters 
print(f"The First Three Letters In Your Name Is '{name[0:3]}'.\nThe Last Three Letters Is '{name[-3:]}'. ")

print('-'*25)

# check if the letter of the user is the start of her name
letter = input("enter the Letter to check :").strip()
if letter == name[0] :
    print("Your Name Start With the letter you entered")
else :
    print("Your Name does not start with the letter you entered")

print('-'*25)

# the number of the letter in name of user 
Letter = input("Enter Letter To count the number of the char in your name :").strip()
if len(Letter) > 1 :
    while len(Letter)!= 1 :
        Letter = input("Enter Letter To count the number of the char in your name :").strip()

somme =(name.count(Letter))+(name.count(Letter.swapcase())) 
print(f"The nuber of Letter in Your Name Is :'{somme}'")

print('-'*25)

# print info of the user 
print("======== User Info ========")
print(f"Name    : {name}\nAge     : {age}\nCountry  : {country}")

print('-'*25)

# find and some methods
a = input("Enter Letter To find in your name :").strip()
if len(a) > 1 :
    while len(a)!= 1 :
        a = input("Enter Letter To find in your name :").strip()
if (name.find(a))!=-1 :
    print("the charactere there is in your name")
else : 
    print("the charactere there is not in your name")

print('-'*25)

# replace
na = input("enter the name that you would to replace :").strip()
replace = input("enter the new string :").strip()
print(f"the new name after replace Is : {name.replace(na,replace)}")
print('-'*25)
 
#startswith
b = input("Enter Letter :").strip()
if len(b) > 1 :
    while len(b)!= 1 :
        b = input("Enter Letter  :").strip()

print(name.startswith(b))

print('-'*25)

#endswith
c = input("Enter Letter  :").strip()
if len(c) > 1 :
    while len(c)!= 1 :
        c = input("Enter Letter :").strip()


print(name.endswith(c))

print('-'*25)






# Project 01 :
print("Project 01".center(50,"="))


def empli_dict(stud_dict):
    Name = input("Enter Name Of Students :  ").strip().title()
    stud_dict[Name] = {}
    stud_dict[Name].setdefault("Math Grade",int(input("Enter The Grade Of Math  : ")))
    stud_dict[Name].setdefault("Science Grade",int(input("Enter The Grade Of Science  : ")))
    stud_dict[Name].setdefault("English Grade",int(input("Enter The Grade Of English  : ")))

def average(student):
    total,countkey = 0,0
    for key,value in student.items():
        countkey += 1
        total += value
    return total / countkey

def get_grad(student):
    avg = average(student)
    if avg >= 90 :
        return "A"
    elif avg >= 80 :
        return "B"
    elif avg >= 70 :
        return "C"
    elif avg >= 60 :
        return "D"
    else :
        return "F"


students = {}
number_stud = int(input("Enter Number Of Students :  ").strip())
for i in range(1,number_stud+1):
    empli_dict(students)

print(students)

print("Results".center(25,"-"))

for name in students :
    print(f"- {name} => Average : {average(students[name])} => Grade : {get_grad(students[name])}")

choice = input("Do You Want To Add Another Student? (yes/no):  ").lower()
if choice == "yes" :
    number_stud = int(input("Enter the number of students you want to add :  ").strip())
    for i in range(1,number_stud+1):
        empli_dict(students)
    for name in students :
        print(f"- {name} => Average : {average(students[name])} => Grade : {get_grad(students[name])}")
elif choice == "no" :
    print("Thanks For Use The Program")
else :
    print("enter yes or no")
    





# Project 02 : (X-O)
print("Project 02".center(50,"="))

board =[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "],
]