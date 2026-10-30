# class father:
#     def __init__(self,age,id,weight):
#         self.age = age
#         self.id = id
#         self.weight = weight
#
# class son(father):
#     def __init__(self,age,id,weight):
#         #用 super().__init__()来继承父类
#         #例如人类是动物，那么人类可以继承动物的属性和方法等
#         #或者新能源车是车，可以继承车的各个属性
#         super().__init__(age,id,weight)
#         self.has_tail = False

#写一个全职和兼职员工的类
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"员工名字：{self.name},工号：{self.id}")

class fullemployee(Employee):
            def __init__(self,name,id,monthly_salary):
                super().__init__(name,id)
                self.monthly_salary = monthly_salary

            def calculate_salary(self):
                return self.monthly_salary

class parttimeemployee(Employee):
    def __init__(self,name,id,daily_salary,work_day):
        super().__init__(name,id)
        self.daily_salary = daily_salary
        self.work_day = work_day

    def calculate_salary(self):
        return self.daily_salary * self.work_day

zhangsan = fullemployee("张三",2005,8000)

lisi = parttimeemployee("李四",2006,60,20)

zhangsan.print_info()
print(zhangsan.calculate_salary())
lisi.print_info()
print(lisi.calculate_salary())

