import random
class Student:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True

    def to_study(self):
        print("time to study")
        self.progress+=0.12
        self.gladness-=3
    def job(self):
        print("I want to earn money")
        self.money=100

    job_list = {
            "Java developer": {"salary": 50, "gladness_less": 10},
            "Python developer": {"salary": 40, "gladness_less": 3},
            "C++ developer": {"salary": 45, "gladness_less": 25},
            "Rust developer": {"salary": 70, "gladness_less": 1}}


    def to_sleep(self):
        print(" I will sleep ")
        self.progress+=3
    def to_chill(self):
        print("Rest time")
        self.progress-=0.1
        self.gladness+=5
    def is_alive(self):
        if self.progress>-2:
            print("I have good money")
            self.alive=True
        elif self.gladness>=5:
            print("Happy")
            self.alive=True
        elif self.progress>10:
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
            self.to_study()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()
nick=Student(name="Nick")
for day in range(365):
    if nick.alive==False:
        break


    class Job:
            def __init__(self, job_list):
                self.job = random.choice(list(job_list))
                self.salary = job_list[self.job]["salary"]
                self.gladness_less = job_list[self.job]["gladness_less"]
    nick.live(day)