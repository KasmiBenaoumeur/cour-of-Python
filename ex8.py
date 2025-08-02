# =============== Ex8(56 -64) ====================
print(" ========================= EX 08 ==========================")
print("----------- Test 01 ---------------------")


# Question 01 :
print("------------- Question 01 : -----------")

def calculate(n1,n2,choice = 'unknown'):
    if choice.lower() in ['+','add','a','unknown'] :
        return n1 + n2
    elif choice.lower() in ['-','subtract','s'] :
        return n1 - n2
    elif choice.lower() in ['*','multiply','m'] :
        return n1 * n2
    else :
        return "Your Choice it is not + - * "
# Tests
print(calculate(10, 20)) # 30
print(calculate(10, 20, "AdD")) # 30
print(calculate(10, 20, "a")) # 30
print(calculate(10, 20, "A")) # 30

print(calculate(10, 20, "S")) # -10
print(calculate(10, 20, "subTRACT")) # -10

print(calculate(10, 20, "Multiply")) # 200
print(calculate(10, 20, "m")) # 200


# Question 02 :
print("------------- Question 02 : -----------")

def addition(*numbers):
    total = 0
    for num in numbers :
        if num not in [5,10] :
            total += num
        else :
            if num == 5 :
                total -= num
            else :
                continue
    return total

print(addition(10, 20, 30, 10, 15)) 
print(addition(10, 20, 30, 10, 15, 5, 100)) 



# Question 03 :
print("------------- Question 03 : -----------")

def show_skill(name,*skills):
    if  not skills :
        print(f'Hello {name} You Have No Skills To Show')
    else :
        print(f'Hello {name} Your Skills Is : ')
        for skill in skills :
            print(f"- {skill}")

show_skill("Osama", "HTML", "CSS", "JS", "Python")
show_skill("Ahmed")



# Question 04 :
print("------------- Question 04 : -----------")


def say_hello(name ='Unknown',age ='Unknown',country ='Unknown'):
    return f"Hello {name} Your Age Is {age} And You Live In {country}"
    
print(say_hello("Osama", 38, "Egypt"))
print(say_hello())





print("----------- Test 02 ---------------------")


# Question 01 :
print("------------- Question 01 : -----------")

def get_score(**materials):
    for material,piont in materials.items() :
        print(f"{material} => {piont}")
    
get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)


# Question 02 :
print("------------- Question 02 : -----------")

def get_people_scores(name ='unknown',**materials):
    if name != 'unknown' :
        if materials :
            print(f"Hello {name} This Is Your Score Table: ")
            for material,piont in materials.items() :
                print(f"{material} => {piont}")
        else :
            print(f"Hello {name} You Have No Scores To Show ")
    else :
        for material,piont in materials.items() :
            print(f"{material} => {piont}")

    

get_people_scores("Osama", Math=90, Science=80, Language=70)
get_people_scores("Mahmoud", Logic=70, Problems=60)
get_people_scores(Logic=70, Problems=60)
get_people_scores("Ahmed")




# Question 03 :
print("------------- Question 03 : -----------")

score ={
    "Math" : 90,
    "Science" : 80,
    "Language" : 70
}

def get_the_scores(name ='unknown',**scores_list):
    if name != 'unknown' :
        if scores_list :
            print(f"Hello {name} This Is Your Score Table:")
            for modile,note in scores_list.items() :
                print(f"{modile} => {note}")
        else :
            print(f"Hello {name} You Have No Scores To Show")
    else :
        for modile,note in scores_list.items() :
            print(f"{modile} => {note}")
        
get_the_scores("Osama", **score)       
get_the_scores("Osama")
get_the_scores(**score)
