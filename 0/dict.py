dict = {"a":"1",
        "b":"2",
        "c":"3",
        "d":"4"}

dict["f"] = "5"
dict[("l","m")] = "6"

print(dict)
print(dict.keys())
print(dict.values())


a = input("请输入需要查询的字母：")

if a in dict:
    print("您查询的" + a + "含义如下：")
    print(dict[a])

else:
    print("您查询的信息暂未收录")
    print("当前收录的词条数量为" + str(len(dict)) + "条")