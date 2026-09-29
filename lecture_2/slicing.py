#accessing parts of a string
#str[starting_index : ending_index]
#ending index is not included.
str = " sakshi singh"
print( str[1:4])
print (str [0:5])
print (str [5:]) # last index is missing means "it print till the last alphabet"

print ( str [4:len(str)])# we can use lenght also for long words


# negative slicing index
str = "apple" 
print(str[-3:-1])
