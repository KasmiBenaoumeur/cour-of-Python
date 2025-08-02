# =============== Ex7 (47 - 55) ==========================
print(" ========================= EX 07 ==========================")
print("----------- Test 01 ---------------------")


# Question 01 :
print("------------- Question 01 : -----------")

num = -1
while num < 0 :
    num = int(input("Please enter a Number :  ").strip())
    if num > 0 :
        print("You number is > 0")
    elif num == 0 :
        print("Your number is = 0")
    else :
        print("Your number < 0")

i = num
count = 0
while i > 1 :
    i-=1
    if i == 6 :
        continue
    print(i)
    count += 1 
print(f"{count} Numbers Printed Successfully.")
  



# Question 02 :
print("------------- Question 02 : -----------")

friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

i = 0
count = 0
while i < len(friends) :
    name = friends[i]
    if name.istitle() :
        print(name)
        i += 1
    else :
        i += 1
        count += 1
        continue

print(f"Friends Printed And Ignored Names Count Is {count} ")


# Question 03 :
print("------------- Question 03 : -----------")

skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills :
    print(skills.pop(0))


# Question 04 :
print("------------- Question 04 : -----------")

my_friends = []
i = 1
while len(my_friends) < 4 :
    name = input("enter name of your name :   ").strip()
    test = name 
    while test.isupper() :
        print("Invalid name")
        name = input("enter name of your name :   ").strip()
        test = name 
    my_friends.append(name.lower().title())
    print(f"Friend {name.lower().title()} Added => {i}st Letter Become Capital")
    print(f"Names Left in List Is { 5 - i}")
    i += 1
else :
    print("The List Of Your friends Is Not Empty")
print(f"Your Friends Is {my_friends}")






print("----------- Test 02 ---------------------")



# Question 01 :
print("------------- Question 01 : -----------")

my_nums = [15, 81, 5, 17, 20, 21, 13]
i = 1
for num in sorted(my_nums, reverse= True) :
    if num % 5 == 0 :
        print(f"{i} => {num}")
        i += 1
else : 
    print("All Numbers Printed")


# Question 02 :
print("------------- Question 02 : -----------")

rang20 = range(1,21)
for num in rang20 :
    if num in [6,8,12] :
        continue
    print(f"- {str(num).zfill(2)}")
else :
    print("All Numbers Printed")


# Question 03 :
print("------------- Question 03 : -----------")

my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
total = 0
for rank in my_ranks :
    if my_ranks[rank] == 'A' :
        total += 100
    elif my_ranks[rank] == 'B' :
        total += 80 
    else :
        total += 40
    print(f"My Rank in {rank} Is {my_ranks[rank]} And This Equal {100 if my_ranks[rank] == 'A' else (80 if my_ranks[rank] == 'B' else 40 )} Pionts")
else :
    print(f"Total Pionts Is {total}")


# Question 04 :
print("------------- Question 04 : -----------")

students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

for name in students :
    print("-"*25)
    print(f"-- Student Name => {name}")
    print(f"-"*25)
    total = 0
    for model in students[name] :
        print(f"- {model} => {100 if students[name][model] == 'A' else (80 if students[name][model] == 'B' else (40 if students[name][model] == 'C' else 20 ))} Pionts")
        if students[name][model] == 'A' :
            total += 100
        elif students[name][model] == 'B' :
            total += 80 
        elif students[name][model] == 'C' :
            total += 40
        else :
            total +=20
    print(f"Total Pionts Of {name} Is {total}")

print("=" * 30)

for nom , mod in students.items():
    print("-"*25)
    print(f"-- Student Name => {nom}")
    print(f"-"*25)
    total = 0
    for nmod,piont in mod.items() :
        print(f"- {nmod} => {100 if piont == 'A' else (80 if piont == 'B' else (40 if piont == 'C' else 20 ))} Pionts")
        if piont == 'A' :
            total += 100
        elif piont == 'B' :
            total += 80 
        elif piont == 'C' :
            total += 40
        else :
            total +=20
    print(f"Total Pionts Of {nom} Is {total}")
    


