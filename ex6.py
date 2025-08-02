# =============== EX5(41 - 46) ==========================

print(" ========================= EX 06 ==========================")



# Question 01 :
print("------------- Question 01 : -----------")

num1 =int(input("enter the first number :").strip())
num2 =int(input("enter the second number :").strip())
operation = input("enter the operation you want to do : (+,-,*,/,%): ").strip()
if operation == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
elif operation == "%":
    print(f"{num1} % {num2} = {num1 % num2}")
else:
    print("You Not Choose A Valid Operation, Please Try Again")


# Question 02 :
print("------------- Question 02 : -----------")

age = 17
print("You Are A Kid" if age < 18 else "You Are An Adult")
print("App Is Suitable For You" if age >= 16 else "App Is Not Suitable For You")


# Question 03 :
print("------------- Question 03 : -----------")

age = int(input("enter your age : ").strip())
choice = input("Do You Want To Transfer Your Age To Months or Weeks or Days or Hours or Minutes or Seconds  ? ").strip().lower()
if choice == "months":
    print(f"Your Age In Months Is : {age * 12}")
elif choice == "weeks":
    print(f"Your Age In Weeks Is : {age * (365.25 /7)}")
elif choice == "days":
    print(f"Your Age In Days Is : {age * 365.25}")
elif choice == "hours":
    print(f"Your Age In Hours Is : {age * 365.25 * 24}")
elif choice == "minutes":
    print(f"Your Age In Minutes Is : {age * 365.25 * 24 * 60}")
elif choice == "seconds":
    print(f"Your Age In Seconds Is : {age * 365.25 * 24 * 60 * 60}")
else :
    print("You Not Choose A Valid Option, Please Try Again")

if age >=10 and age <=100:
    print("Your Age Is Between 10 And 100")
else:
    print("Your Age Is Not Between 10 And 100")
# Question 04 :
print("------------- Question 04 : -----------")

ArabC = ["Algeria","Morocco","Tunisia","Egypt","Libya","Sudan"]
EuropeanC = ["France","Spain","Italy","Germany","Portugal","Greece"]
discount = 20
YourCountry = input("What's Your Country ? ").strip().title()
if YourCountry in ArabC:
    print("Your Country Is In Arab Countries List , You Get A Discount Of 20%")
    print("The Price After Discount Is : ", 100 - discount, "%")
elif YourCountry in EuropeanC:
    print("Your Country Is In European Countries List , You Get A Discount Of 10%")
    print("The Price After Discount Is : ", 100 - (discount / 2), "%")
else :
    print("Your Country Is Not In The List")
    print("The Price Is : 100%")