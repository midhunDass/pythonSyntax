try:
    print("inside try block")
    foo = 100 / 0
except:
    print("Number cannot be divisible by 0")
finally:
    print("Program is terminating")


def sumTest(a, b=7):
    val = a + b
    print(val)


def sumReturn(a, b) -> int | str:
    if a > b:
        return a + b
    return "a is less than b"


sumTest(11, 22)
sumTest(11)
print(sumReturn(11, 2))
print(sumReturn(1, 2))
print(sumReturn(b=2, a=12))


def sumVar(*params):
    sum_res = 0
    for item in params:
        sum_res = sum_res + item
    return sum_res


def sumVarList(*params):
    sum_res = 0
    for item in params:
        for val in item:
            sum_res = sum_res + val
    return sum_res


def sumCharList(*params):
    sum_res = ''
    for item in params:
        for val in item:
            sum_res = sum_res + val
    return sum_res


def sumStrList(*params):
    sum_res = ""
    for item in params:
        for val in item:
            sum_res = sum_res + val
    return sum_res


def diffDataTypes(*params):
    list_sum = 0
    params_str = ''
    params_int = 0
    params_float = 0
    for data in params:
        a = type(data)
        if a == list:
            for items in data:
                list_sum = list_sum + items
        elif a == str:
            params_str = params_str + data
        elif a == int:
            params_int = params_int + data
        elif a == float:
            params_float = params_float + data
    print('sum of elements in the list' + " : ", list_sum)
    print('sum of int params' + " : ", params_int)
    print('sum of float params' + " : ", params_float)
    print(' str params' + " : ", params_str)
    return list_sum


print("def with variable num of parameters")
testParams = [1, 2, 3, 4]
testParams1 = [1, 2, 3, 4]
print(sumVar(1, 2, 3, 4, 5))
print(sumVar(1.4, 2, 3, 4.8, 5))
# print(sumVar('a', 'b', 'c'))  # this line will throw an exception
# print(sumVar("py", "th", "on"))   # unsupported operand type(s) for +: 'int' and 'str'
print(sumVarList(testParams1, testParams))
print(sumCharList('a', 'b', 'c'))
print(sumStrList("py", "th", "on"))
print("sum of elements in the passed list " + " : ", diffDataTypes(1.4, 2, 3, 4.8, 5, 'a', "str", testParams))
print("_____________________________________________________________________________________________")
