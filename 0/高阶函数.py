def function1(num):
    num *= 7
    return num

def function2(num,result):
    print(f"传入参数；{num},\n计算结果为:{result}")

def calculation_print(num,function1,function2):
    result = function1(num)
    function2(num,result)

calculation_print(5,function1,function2)