# ex 2 (11-18)

# Question 01 
Name = "BEnaoumeur"
Age = 18
Country = "Algeria"

print(f"\"Hello '{Name}', How You Doing \\ \"\"\" Your Age Is \"{Age}\"\" + And Your Country Is: {Country}")

print('-------------------------------------------------------------------')

# Question 02 

print(f"\"Hello '{Name}', How You Doing \\\n\"\"\" Your Age Is \"{Age}\"\" + \nAnd Your Country Is: {Country}")

print('-------------------------------------------------------------------')

# Question 03
name = "Elzero"
print(f"Second Letter Is \"{name[1]}\" \nThird Letter Is \"{name[2]}\" \nLast Letter Is \"{name[-1]}\" ")

print('-------------------------------------------------------------------')

# Question 04

print(f"\"{name[1:4]}\" \n\"{name[::2]}\" \n\"{name[4::-2]}\" ")

print('-------------------------------------------------------------------')

#  Question 05
name = "#@#@Elzero#@#@"
print(name.strip('#@'))

print('-------------------------------------------------------------------')

# Question 06
num1,num2,num3,num4,num5 = "9","15","130","950","1500"
print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))
# print(num1.zfill(4), num2.zfill(4), num3.zfill(4), num4.zfill(4), num5.zfill(4))

print('-------------------------------------------------------------------')

# Question 07
name_one,name_two = "Kasmi","Kasmi_Benaoumeur"
print(name_one.rjust(20,'@'))
print(name_two.rjust(24,'@'))

print('-------------------------------------------------------------------')

# Question 08
name_One,name_Two = "KAsmI","kasMI"
print(name_One.swapcase())
print(name_Two.swapcase())

print('-------------------------------------------------------------------')
 
# Question 09
msg = "I Love Python And Although Love Elzero Web School"
print(msg.count('Love'))

print('-------------------------------------------------------------------')
 
# Question 10
name = "Elzero"
print(name.find('z'))
print(name.index('z'))

print('-------------------------------------------------------------------')
 
# Question 11
msg2 = "I <3 Python And Although <3 Elzero Web School"
print(msg2.replace("<3","Love",1))

print('-------------------------------------------------------------------')
 
# Question 12
msg2 = "I <3 Python And Although <3 Elzero Web School"
print(msg2.replace("<3","Love"))

print('-------------------------------------------------------------------')
 
# Question 13
name1 = "Kasmi"
age = 18
country = "Algeria"
# with format new version
print(f"My Name Is {name1}, And My Age Is {age}, And My Country Is {country}")
# with format old version
print("My Name Is {}, And My Age Is {}, And My Country Is {}".format(name1,age,country))

