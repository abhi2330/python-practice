# Slicing #
str = "Shivam"
print(str[:4])
print(str[:len(str)]) 

#Conditions Statement#

age = 21
if(age <= 18):
    print("Your are elisible to license")

# elif #
light = "pink"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("wait")
else:
    print("light is broken") # else #


marks = int(input("enter student marks : "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"
print("grade of the student ->", grade)


#Nesting#
age = 95
if(age >= 19):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("canot drive")
    