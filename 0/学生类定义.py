class Student(object):
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.grade = {"语文":0,"数学":0,"英语":0}

    def set_grade(self,course,grade):
        if course in self.grade:
            self.grade[course] = grade

    def print_grade(self):
        print(f"学生{self.name},学号{self.id}，成绩是:")
        for course in self.grade:
            print(f"{course}：{self.grade[course]}")

zhumimi = Student("xiaozhu","2000018")
zhumimi.set_grade("语文",98)
zhumimi.set_grade("数学",95)
zhumimi.set_grade("英语",99)

zhumimi.print_grade()
