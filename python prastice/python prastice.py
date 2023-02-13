# This is a single line cooments

'''This is a multiline 
cooments'''

#VARIABLES

x=5
print(x)
print(type(x))

y=1j
print(type(y))

x='5'
print(type(x)) # now x is string
x=55.757
print(type(x))

x=5
X=7
print(x)#5
print(X)#7


x,y=2,3
print(x)
print(y)

x=y=z="string"
print(z)


print(x,y,z) #print multiple variables
print(x+y+z)


#STRING

a="string"
b="str"# both are string

print(len(a))      #find length
print(a[:2])        #slicing
print("r" in a)        #boolean

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

txt = "The best things in life are free!"
if "free" in txt:
  print("yes, 'free' is present.")


a="hello"
print(a.upper())

a="HELLO"
print(a.lower())

a="  hello e i am  "
print(a.strip())        #remove whitespaces in beggininhg or end

a="hello"
b='world'
print(a+b)

c=5
txt="hy i am {}"
print(txt.format(c))


#LISTS

list=[1,2,3,3,4,5]
l2={"syr",'ali', 'ahmad'}
l3=((True,False,True))      #this is also a list
print(list)         #allow duplicates
print(type(list))

print(list[:-1])

list[0]=40
print(list)

#list methods

list.insert(2,98)
print(list)

list.append(100)
print(list)

list=[1,89,3,45,76,23]
list.sort()
print(list)

list.reverse()
print(list)

list.pop(3)
print(list)

list.remove(3)
print(list)


thislist = ["apple", "banana", "cherry"]
thistuple = ("ali", "ahmd")
thislist.extend(thistuple)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


thislist.clear()
print(thislist)


# TUPLES

a=(1,3,4,4,6,5)

print(type(a))

print(a.count(4))

print(a)
print(a.index(6))


#DICTIONARY

a={'ali':25,'ahmd':45,'arslan':23,'list':[1,3,5]}
print(type(a))

print(a['list'])

print(a.items())
print(a.keys())

a.update({'safdar':656})
print(a)

print(a.get("ali"))



#SET

s={1,7,8,3,9,0}
print(type(s))

print(len(s))

s.remove(8)
print(s)

s.pop()
print(s)

#s.clear()
#print(s)

print(s.union({8,3}))
print(s.intersection({8,3}))


#IF ELSE

a=54
if(a>5):
    print("greater")

else:
    print("less")

a=55
if(a<5):
    print("less")
elif(a==55):
    print("equal")
else:
    print("greater ")


#LOOOOP
i=0
while(i<10):
    print(i)
    
    if i==8:
        break
    i=i+1


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def add(x,y):
    print(x+y)
  
add(5,7)
