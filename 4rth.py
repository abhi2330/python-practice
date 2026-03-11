info = {
    "key" : "value",
    "name" : "shivam",
    "learning" : "coding"
}
print(info)

#nested#
student = {
    "name" : "Shivam",
    "subject" : {
        "phy" : 97,
        "math" : 90,
        "english" : 95
    }
}
print(student["subject"])

# Methode#

student = {
    "name" : "Shivam",
    "subject" : {
        "phy" : 97,
        "math" : 90,
        "english" : 95
    }
}
print(list(student.keys()))


     # Sets#
collection = {1,2,3,4, "Hello I am Shivam"}
print(collection)
print(type(collection))
print(len(collection))

# set union #

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))  #{1.2.3.4}
print(set1.intersection(set2))  #{2,3}

dict = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]
}
print(dict)

#2#
 