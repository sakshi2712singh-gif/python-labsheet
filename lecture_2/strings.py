# # strings 
# str1 = "sakshi"
# print(str1)

# #concatination
# str2 = "sakshi"
# str3 = "singh"
# print(str2 + str3)

# #length of string 
# str = "sakshi"
# len1 = len (str)
# print(len1)
# str4 = "sak_shi"
# len2 = len(str4)
# print(len2)



#string functions
#endswith
str = "my name is sakshi singh"
print(str.endswith("ngh"))
print(str.endswith("igf"))


#capitalized
str = "sakshi singh"
print(str.capitalize())# it will work only one time.
# if we want to apply this permanently then store the str=str.capitalize



#replace
str = "sakshi singh"
print(str.replace("s","p"))
print(str.replace("singh","sakshi"))

#find ( indexs)
print(str.find("k"))
print(str.find("shi"))

#count
print(str.count("s"))



# conditional statements    
  #  if(condition1):
    #    statement1
  #  if(condition2):
    #    statement2
  #  elif(conditon3):
   #     statement3
  #  else:
  #        statement


light =  "green"
if(light == "red"):
        print("stop")
elif(light == "green"):
        print("go")
elif(light == "yellow"):
        print("look")
else:
        print("dont drive")   


#grade distributION   


marks = int( input("enter your no : ")) 

if(marks >= 90):
        # if(marks > 95):
               print("grade = 'A++")
        # else:
        #       print("grade = a+")

elif(marks >= 80):            
        grade = 'B'
elif(marks >= 70):
        grade = 'C'
elif(marks >= 60):
        grade = 'D'
elif(marks >= 33):
        grade = 'E'
else:
        grade = 'fail'
print("grade of all students ->", grade)
        
   

#odd even no :
no = int(input("enter your no:"))

rem = no % 2

if ( rem == 0 ):
        print("EVEN")
else:
        print("ODD")


        #greatest no of three

a = int(input("enter a no"))
b = int(input("enter a no"))
c = int(input("enter a no"))

if(a >= b and a >= c):
        print(" first largest no is ",a)
elif( b >= c):
        print("sec largest no is",b)
else:
        print("third no is largest", c)

        # multipile of 7

        z = int(input("enter a no"))

        if(z % 7 == 0):
                print("multiple of 7")
        else:
                print("not a multiple")