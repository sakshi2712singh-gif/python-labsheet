#dictionary is used to store datavalues in key:value pairs
#they are unordered ,mutable (changeble)and dont't allow duplicate keys.
#"key" :value          (dict["key"]="value" =for to assign or add new)
#dict ={
    #    "name" : "sakshi"      =dict["name"]
    #    "cgpa" : 72.90         =dict["cgps"]
    #   "markes": [78, 78, 90,] =dict["marks"]}

info ={ 
    "name":"sakshi singh",
    "address":"jafferpur ansu",
    "study":("10th, 12th , bsc computerscience,"),
    "age": "22",
    "marks in bsc 3rd year": "72.90",
    "pg college student": "true",
    "current college name":"core university roorkee",
}

print(info)    # for print full dicti
print(type(info))
print(info["name"])  #for printing a perticular key value
info["post"] = "bahaderpur sarfudin husan",  # this way we can aad new key to our dictionary.
info["name"] = "sakshi"  # thats how we can make changes in the key value.
print(info)


null_dictionary = {}
null_dictionary["name"] = "sakshi"
print(null_dictionary)
 
 
#nested dictioonary
# stu = {
#     "name":"sakshi",
#     "sub" : {
#         "daa":35,
#         "network":42,
#         "eng":36,
#         "maths":35
#     }
# }
# # print(stu)
# print(stu["sub"] ["maths"])

# methords in dict
my_dic = {
    "sub" : "marks",
    "c" : "45",
    "m" : "67",
    "p" : "43"
}
print(my_dic.keys())   #return all keys.
print(list(my_dic.keys()) )     #for making the list of dict keys.
print( len(list(my_dic.keys()) ) )    # for printing the length of the dict.
print(my_dic.values())  #returns all keys.
print(my_dic.items())  #returns all (key,val)pairs as tuples.
pairs = list(my_dic.items())   #for making the dic into a listb or tuple form.
print(pairs[2])   # for printing a singe pair of the list by its index value call.
print(my_dic.get("c"))    # returns the according to values.
my_dic.update({"e" : "78"})    #insert the specified items to the dictionary.
print(my_dic)



#practice:
dic = {}

x = int (input("MARKS PHY"))
dic.update({"phy " : x})

x = int (input("MARKS eng"))
dic.update({"eng " : x})

x = int (input("MARKS chm"))
dic.update({"chm" : x})
print(dic)
