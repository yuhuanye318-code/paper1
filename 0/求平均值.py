user_input = input("请输入数字(完成所有数字后输入q结束程序):")
count = 0
total = 0

while user_input != "q":
    number = float(user_input)
    count += 1
    total += number
    user_input = input("请输入数字(完成所有数字后输入q结束程序):")

if count == 0:
    total = 0
    result = 0

else:
    result = total / count
print("您输入的数字平均值为" + str(result))