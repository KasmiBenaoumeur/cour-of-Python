# ================= EX4 (26 -> 32) =================

# Question 01 :
print("Question 01 :")

List = [1,5,4,3,3,2,1]
List.sort()
unique_List = list(set(List))
print(List)
print(unique_List)
print(type(unique_List))
unique_List.pop(-1)
print(unique_List)



# Question 02 :
print("Question 02 :")

SET1 = {1,2,3}
SET2 = {"A","B","C"}

NEWSET= SET1.union(SET2)
SET1.update(SET2)
SET1|SET2 
print(SET1)
print(SET1)
print(NEWSET)



# Question 03 :
print("Question 03 :")

Num ={1,2,3}
print(Num)
Num.clear()
print(Num)

Num.add("A")
Num.add("B")
print(Num)

print(Num.discard("C"))
print(Num)



# Question 04 :
print("Question 04")

SET3 = {1,2,3}
SET4 = {1,2,3,4,5,6}

print(SET4.issuperset(SET3))
print(SET3.issubset(SET4))



# Question 05 :
print("Question 05")

languages ={
    "one": {
        "name" : "python",
        "progress" : "25 %",
    },
    "two" : {
        "name" : "pascal",
        "progress" : "80 %",
    },
    "three" : {
        "name" : "Java",
        "progress" : "0 %",
    }
}

print(languages["one"]["name"],"Progress Is",languages["one"]["progress"])
print(languages["two"]["name"],"Progress Is",languages["two"]["progress"])
print(languages["three"]["name"],"Progress Is",languages["three"]["progress"])
ajout = {
    "four": {
        "name" : "kotlin",
        "progress" : "0 %",
    }
}
languages.update(ajout)
print(languages["four"]["name"],"Progress Is",languages["four"]["progress"])












