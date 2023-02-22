#Mutable vs immutable

#Mutable are datatypes that can change during the life cycle of the program i.e you can add or change them
#Immutable are datatypes that cannot be edited during the lifecycle of the program

#1) Lists (Mutable)


#4) sets

friends=["Mark","Anita","John","Joy"]
# or [] for an empty list
# add elements to the list -----> append(), extend(), 

students =["Marie","Kigen","Serphine"]

friends.extend(students)
print(friends)

friends.append("James")
print(friends)

friends.sort()
print(friends)

#2) Tuples (Immutable)
#Tuples---->type of lists that are not editable
stationaries =("ruler","clipboard","pencil","rubber")

for stationary in stationaries:
    print(stationary)

numbers =(1,2,3,4,5,6,7,8,9,)

#3) Dictionaries aka dict
# uses key and value pair

student={"Name" : "Caldavis" , "age" :24, "gender" : "Male","is tall":True}
#"name" : "Bob" ---> name(key)  Bob(value)

print(student["Name"])
print(student["age"])
print(student["gender"])
print(student["is tall"])

print(student.values())
print(student.keys())
print("---------------------")

friend={"fav_color" : "Blue" , "Hobby": "Listening to music", "Weight": 54,"Height": 183}

print(friend["fav_color"])
print(friend["Hobby"])
print(friend["Weight"])
print(friend["Height"])