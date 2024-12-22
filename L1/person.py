class Person():
    def __init__(self,name,hobby,food):
        self.name = name
        self.hobby = hobby
        self.food = food
    def hi(self):
        print(f'Hi! My name is {self.name}! I like {self.hobby} and eating {self.food}!')
a = Person('A', 'reading', 'broccoli')
a.hi()
b = Person('B','swimming', 'cheese')
b.hi()