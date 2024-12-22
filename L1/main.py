class Robot():
    def __init__(self,name, count, battery):
        self.color = 'red'
        self.name = name
        self.battery = battery
        self.count = count
    def introduce(self):
        self.battery = 100
        print(f'Hi! My name is {self.name}, I am red! My battery is {self.battery}! I have completed {self.count} tasks!')
    def task(self):
        if self.battery >= 10:
            self.battery -=10
            print(f'I am doing the laundry! My battery is now {self.battery}!')
            self.count +=1
    def recharge(self):
        print(f'Recharging battery...')
        self.battery = 100
        print(f'Battery is now {self.battery}')
robot = Robot('Robo',0,100)
robot.introduce()
robot.task()
robot.recharge()

        
