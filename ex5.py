# =============== EX5(33 - 40) ==========================

# ============= Test1 (33 -37) ===========
print(" ========================= Test 01 ==========================")



# Question 01 :
print("------------- Question 01 : -----------")

print(bool(5))
print(bool(10 > 5))
print(bool("KASMI"))
print(bool({1,2,3,4}))

print(bool(0))
print(bool(10>20))
print(bool([]))
print(bool(()))



# Question 02 :
print("------------- Question 02 : -----------")

python = 70
pascal = 80
java = 60

print(python > 50 and pascal > 50 and java > 50)



# Question 03 :
print("------------- Question 03 : -----------")

num_one = 10
num_two = 20
num = 20

print(num > num_one or num > num_two)
print(num > num_one and num > num_two)



# Question 04 :
print("------------- Question 04 : -----------")

num_one = 10
num_two = 20
result = num_one + num_two
print(result)
Exponent = result ** 3
print(Exponent)
rest = Exponent % 26000
print(rest)
division = rest / 5
print(division)
print(type(division))
division =str(division)
print(type(division))



# ============= Test2 (38 - 40) ===========
print(" ================== Test 02 =============================")



# Question 01 :
print("------------- Question 01 : -----------")

name = input("What's Your Name ? ").strip().capitalize()
print(f"Hello {name}, Happy To See You Here")



# Question 02 :
print("------------- Question 02 : -----------")

age = int(input("What's Your Age ?"))
if age < 16 :
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else : 
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")


# Question 03 :
print("------------- Question 03 : -----------")

first_name = input("What's Your First Name ?").strip().capitalize()
second_name = input("What's Your Second Name ?").strip().capitalize()

print(f"Hello {first_name} {second_name[0]}.")

# Question 04 :
print("------------- Question 04 : -----------")

email = input("What's Your Email ?").strip()
print(email)
email = email.lower()
print(email)
nom = email[:email.index("@")]
print(nom.capitalize())
website = email[email.index("@")+1:email.index(".")]
print(website)
domain = email[email.index(".")+1:]
print(domain)