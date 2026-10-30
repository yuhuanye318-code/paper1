class zhumimi :
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def speak(self):


xiaodan = zhumimi("xiaozhudandan",18,165,55)
print(f"小丹的名字是{xiaodan.name},年龄是{xiaodan.age}，身高是{xiaodan.height}，体重是{xiaodan.weight}")