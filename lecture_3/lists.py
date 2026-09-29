#how to make the list in the paython:- a built in data type that store set of values
#   we can store elements of different types (int,float,string,etc)
# in the list the changes occure in the main list once then the changed list is work ase the main list and the next change occure in the this chenged list ( not alwayse in the first given list)
# marks = [67,89,"sakshi",67.9,"good"]
# marks[3]="sakshi",len(marks) = return len "5"
# we can swap the position or 2 elements
# we can also change the element by index value
marks = [52.6, 58.6, 59.7, 24.8, 79.6]
print(marks)
print(type(marks))

print(marks [0])
print(marks [1])

print(len(marks))

print(marks[3])
marks[3] = "sakshi"
print(marks)

#list slicing: same as substring = sublist(last index not including)
print(marks[1:4])
print(marks[-3:-1])

#methods of list 
 #list.append() = adds one element at the end 

list = [5,3,2,8]
list.append(8)
print( list )   #this change in the list is also called the mutation(changable)

#list.sort() = sorts in ascending order
list.sort()
print( list )

#list.sort(reverse=True) = sorts in descending order
list.sort(reverse=True)
print (list)

mixed_list =[3, "apple", 1.5, "banana",2]
sorted_list = sorted(mixed_list,key=lambda x: (0 , x) if isinstance(x, (int, float)) else (1 , x))
print (sorted_list)

#list.reverse() 
list.reverse()
print(list)

#list.insert(idx,el)  = insert element at index but rest of values till the index is as it is in the list after the insert value in the list and also the the value of the before the insert index elements also same 
# in simple thier is no change in the befor and after elements only the element is insert at the given index and the past value of that index is save +1  as on

list.insert(4,9)
print(list)

# remove method = it remove the first occurrence of element
list.remove(8)
print(list)

#pop method = it will delete the value by index
list.pop(3)
print(list)


# examples

movie_list = input(" enter first movie , enter second movie; enter third movie:")
print( movie_list )

#palindrome list check programm
list1 = [1, 2, 1,]
list2 = ["m", "a", "a", "m",]

copy_list1 = list1.copy()   #copy() = returns as shellow copy.
copy_list1.reverse()        #is reverse the list.

if(copy_list1 == list1):
    print("palindrome")
    print(copy_list1)
else: 
    print("not palindrome")

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("palindrome")
    print(copy_list2)
else:
    print("not palindrome")

    
    
  