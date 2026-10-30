try:
    weight = float(input("请输入体重："))
    height = float(input("请输入身高："))
    BMI = weight / height ** 2

except:
    print("输入错误，请重新运行程序，并输入正确数字")

else:
    print("您的BMI值为：" + str(BMI))

finally:
    print("程序结束运行")