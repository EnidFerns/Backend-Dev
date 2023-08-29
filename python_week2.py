# functions and data structures
#function is a set of instruction sthat take an input and return an output

# def name(params):
#     task to complete


#scoping in python  ---- variable scopes - scopes purpose is to protect the variable so ot doesnt get changed by parts of code.
#local scope --> enclosing scope -->( global scope --> built-in scope-=reserved scope., both accessed anywhere in code) -------LEGB

# Local scope
# Local scope refers to a variable declared inside a function. 

# Enclosing scope
# Enclosing scope refers to a function inside another function or what is commonly called a nested function. 

# Global scope
# Global scope is when a variable is declared outside of a function. This means it can be accessed from anywhere. - discouraged due to errors

# Built-in scope
# Built-in scope refers to the reserved keywords that Python uses for its built-in functions, such as print, def, for, in, and so forth.  Functions with built-in scope can be accessed at any level.

#data structures in python ----> built in data structures & user-defined data structures

#built in - list, tuple, dict, set } These are all considered non-primitive data structures, meaning they are classed as object

#user defined ----- stack, queue, tree, ll, graph, hashmap

# Mutability refers to data inside the data structure that can be modified. - list
# An immutable data structure will not allow modification once the data has been set.- tuple

# list -index based, nested lists,
list1 = [1,2,3,4,5]
print(*list1) #prints al items in list
list1.insert(len(list1), 6)
list1.append(6)
list1.extend([7,8,9,20])
list1.pop(5)#pop index 5
del list1[1] #delete index 1
print(list1, sep=' ')
#iteration
for x in list1:
    print('value : ',x)

#tuples -- immutable
my_tuple =(1,'stirng', 4.5, True) #works without parenthesis also
print(my_tuple[1])
print(type(my_tuple))

print(my_tuple.count('stirng')) #number of occurences in tuple
print(my_tuple.index(4.5))

for x in my_tuple:
    print(x)

#sets -- unique -- unordered(not based on index)
seta ={1,2,3,4.5,5}
print(seta)
seta.add(6) #add method
seta.remove(6); seta.discard(2) #remove and discard method
#math operations on sets - 2 operations - union and intersection
setb = {1,6,8,3,1}
#union
print(seta.unioni(setb)) # minus duplicates
print(seta | setb) # or symbol works the same
print(seta.intersection(setb))
print(seta & setb)

#set difference
print(seta.difference(setb)) #in seta not in setb
print(seta - setb)

#symmetric difference
print(seta.symmetric_difference(setb)) # all elements in seta or setb but not in both sets
print(seta ^ setb) #carrot operator does the same as symmetrical operator

#dictionary -- access based on keys key: value pair, mutable
sampledict = {1:'coffee',2:'tea'}
print(sampledict[1])

sampledict[2]= 'mint tea' #changing itsem

del sampledict[2] # deletin gkey 2

#3 diff methods to iterate dicts :  standard, itsems(), values()

mydict = {1:'test', 'name':'enid'}
print(type(mydict))

print(mydict[1])
mydict[2] = 'test2'
#no duplicate keys

for x in mydict: # only prints keys
    print(x)

for key,value in mydict.items(): # usew items method to print both 
    print(str(key), " : ", value)

#kwargs - keyword args - pass any number of non-keyword variables and keyword arguments

#args -- you can pass any amount of non-keyword variables!
# def sumof(a,b):
#     return a+b
# print(sumof(1,2,3)) #will give error, here you use args, will be able to pass n arguments

def sumof(*args):
    sum = 0
    for x in args:
        sum +=x
    return sum
print(sumof(1,2,3))

#kwargs - you can pass any amount of keyword arguments!
def sumof(*kwargs):
    sum = 0
    for k,v in kwargs.items:
        sum +=v
    return round(sum, 2)
print(sumof(cooffee = 12.8, tea = 8.4))


#errors, exceptions and file handling