#set : set is the collection of the unordered items. set is mutable.
#each element in  set must be unique and immutable.
set1 = {1, 3, 3, 5, "hellow",}
#repeated elements stored only once,so it resolved to {1,3,5,"hellow"}
#null_set = set()  = empty set syntax.
print(set1)        #output = order free 
print(type(set1))
print(len(set1))       #output = 4 (because no duplicate values)
set2 = set()
print(type(set2))
print(set2)


#some methords in the set:

set2.add(4)
set2.add(6)
set2.add("hi")
set2.add((6,8,9))     # tuple addtion
set2.remove(6)         # when we give command remove 6 it will remove frome set but not in tuple collection.
#set2.add([3,5,6 ])       #we don't add dictionary,set,lists becouse it is mutable (changeble)
set2.clear()   # it is used for clear the set  become empty set.
print(set2)
print(len(set2))

set3 = {"sakshi", "hi",4 ,5 ,7}
# print(set3.pop() )         #remove rendom value
print(set3.pop() )  
print(set3.pop() )  


#set1.union(set2)     = used to combines both set values and return new
#set.intersection(set2)   =used to combines common values and returns new
set4 = {1, 2, 3, }
set5 = {2, 3, 4, }
print(set4.union(set5))
print(set4)
print(set5)
print(set4.intersection(set5))

# practiced:
myset = { 
    "python","c++", "python", "c++", "java","python","java","c", "javascript", "java"
}
print(len(myset))


# W A Ptp print the 9.0,9 in a set ..... this to be done by the two ways.
set_values = {9, "9.0" ,}
print(set_values)

setv = {
    ("float",9.0),("int",9)
}
print(setv)