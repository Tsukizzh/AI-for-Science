class Person:
    def __init__(self,name):
        self.name = name

    def __call__(self, name):
        print("hello"+self.name)

    def call(self):
        print("hheello"+self.name)

person1 = Person()
person1()

class Person:
    def __init__(self, name, age):
        self.name = name  # 设置 name 属性
        self.age = age    # 设置 age 属性

    

# 创建实例
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
