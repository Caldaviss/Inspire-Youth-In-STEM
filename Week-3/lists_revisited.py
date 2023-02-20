#!/usr/bin/env/python3

#This is a single line comment
#python program should illustrate lists
#Name : Caldavis
#Email: caldavis118@gmail.com
#Date :20th Feb 2023
#File :lisis_revisited.py

myFavoriteFruits=["banana","apple","orange","pineapple"]

for fruit in myFavoriteFruits:
    print(fruit)

    print(len(myFavoriteFruits))


friends=["Phoebe","Joy","Monicah","Chandler"]
print(friends)
friends[0] = "Mary"
print(friends)

print("---------------------------")
new_friends = friends.copy()
print(new_friends)

new_friends.sort()
print(new_friends)

new_friends.pop()
print(new_friends)








