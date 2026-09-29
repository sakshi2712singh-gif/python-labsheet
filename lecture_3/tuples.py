 # tuples are immutable sequences of values.we not change the values ,not add new elements and not delete the elements.
#  we can use , by every single element in tuple .otherwise python understand simple understand other type of data.

tup = ( 3, 4, 6, 7, 7)
print(tup[0])
print(tup[3])

#empt tuple 
tup = ()
print( tup )
print(type( tup ))

 # slicing
print(tup[1:3])
 # methords in tuple
 #tup.index( el) = returns index of first occurrence 
tup = (3, 4, 5, 6, ) 
print(tup.index(4))



 # tup.count( el ) = counts total occurrences 
print(tup.count(5))

tup = ['A', 'R', 'T', 'A', 'O', 'A',]
tup.sort()
print(tup)