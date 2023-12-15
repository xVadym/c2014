import random
class Cat:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True

    def to_sleep(self):
        print("I want to sleep")
        self.progress+=0.12
        self.gladness-=3
    def to_wakeup(self):
        print(" i wake up ")
        self.progress+=3
    def to_eat(self):
        print("time to have something tasty")
        self.progress-=0.1
        self.gladness+=5
    def is_alive(self):
        if self.progress<-0.5:
            print("i want to eat something new")
            self.alive=False
        elif self.gladness<=0:
            print("Sad")
            self.alive=False
        elif self.progress>5:
            print("Passed externaly")
            self.alive=False
    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress,2)}")

    def live(self,day):
        day="Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube=random.randint(1,3)
        if live_cube==1:
            self.to_sleep()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_eat()
        self.end_of_day()
        self.is_alive()
Tom=Cat(name="Tom")
for day in range(365):
    if Tom.alive==False:
        break
    Tom.live(day)