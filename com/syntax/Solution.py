import math

a = 1
if a < 1:
    print("Hello World")
elif a == 0:
    print("Hello Zero")
else:
    print("Hellow")

while a < 5:
    print(a)
    a += 1
print("end while")

for number in 1, 2, 3, 4, 5:
    print(number)

foo_bar = ('Apple', 'Banana', 'Mango')  # tuple
for index in range(0, len(foo_bar)):
    print(index, " : ", foo_bar[index])

for letter in "PYTHON":
    if letter == 'O':
        break
    if letter == 'H':
        continue
    print(letter)

sample_list = [11, 22, 33, 44, 55, 11, 1, 2, 3]
for item in sample_list:
    print(item)
print(sample_list)
sample_list.append(66)  # append an item at the last
sample_list.insert(0, 77)  # insert an item at a specified index
sample_list.insert(13, 88)  # if item is inserted at an index out of range then it inserted at the last
print(sample_list)
p = sample_list.pop(0)  # removes/pop an item from index and return the value
sample_list.remove(11)  # removes the first occurrence of a particular value of the list
print(sample_list)
sample_list.reverse()  # reverse a list
print(sample_list)
sample_list.sort()  # sort a list ascending
print(sample_list)
sample_list = sample_list[0: 5]
print(sample_list)
print(p)

foo = {"Name": "Maddy", "Age": 18, 1.2: 144, 2.5: "6.25"}  # dict can have multiple data types as key and val
print(foo)
print(foo.get("Name"))  # return an element corresponding the key passed None if no such key
print(foo.get("name"))  # key is case-sensitive
foo_dict = {"Address": "India"}  # new dictionary
print(foo_dict)
foo.update(foo_dict)  # appending foo_dict at the tail of foo
print(foo)

foo_string = "I love python python"
print(foo_string)
var_count = foo_string.count("o")
print(var_count)
var_replace = foo_string.replace("t", "T")  # create a new string variable with replaced element
print(var_replace)
var_find_sub = foo_string.find("python")  # returns the index of the first occurrence of the sub str
print(var_find_sub)
var_startswith = foo_string.startswith("I")  # checking a particular string start with the element passed
print(var_startswith)
var_endswith = foo_string.endswith("on")  # checking a particular string ends with the element passed
print(var_endswith)
foo_string.isdigit()
foo_string.upper()
foo_string.lower()
var_split = foo_string.split(" p")  # split the string according the elements passed
print(var_split)
var = foo_string[0:3]  # refactor string into given start and end position end excluded
print(var)

print("math starts here")
print(math.ceil(9.6))
print(math.floor(9.6))
print(math.factorial(5))
print(math.fabs(-9.6))

dictTest = {"a": 100, "b": 500, "c": 300}
print(dictTest.keys())

for key in dictTest:
    print(key, dictTest[key])

for keys, vals in dictTest.items():
    print(keys, vals)

