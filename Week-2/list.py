names=["Caldavis","John","Alex","Simon"]


#Accessing items in a list
print(names)


print(names[0])

print(names[-1])

print(names[2])

print(names[0:3])

fruits=["mangoes","oranges","apples"]

print(fruits[0])

vegetables=["kales","spinach","cabbage","carrot"]

stationery=["pencil","rubbber", "pen","ruler"]

print(vegetables)
print(stationery)

shoppings=vegetables+stationery

print(shoppings)

for vegetable in vegetables:
    print(vegetable)


for shopping in shoppings:
    print(shopping)

print("My name is " + names [0] + " and my favorite fruit is " + fruits[1])

print(names[3])

def thing ():
    print("hello")
    print("mealin")

thing ()
print ("zip")
thing ()



def cladi() :
   print("shoes")
   print("shirts")
   print("trousers")


cladi()

big = max("Hello world")

print(big)

sval= "123"
rws=int(sval)


print(type (sval))


print(type(rws))

print(rws + 1)






def greet(lang):
    if lang == "es":
        return("hola")
    elif lang == "fr":
        return("bonjuor")    
    else:
        return("hello")



print(greet ("es"), "Glenn")
