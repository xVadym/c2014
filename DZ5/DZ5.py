import random
class Student:
    def __init__(self,name):
        self.name=name
        self.gladness=45
        self.progress=20
        self.alive=True

    def to_wakeup(self):
        print("i wake up")
        self.progress+=5
    def to_brush_the_teeth(self):
        print("I brushed my teeth")
        self.progress+=8
    def to_have_a_breakfast(self):
        print("I have a breakfast")
        self.progress+=12
        self.gladness+=60
    def to_get_dressed(self):
        print("I get dressed")
        self.progress+=4
    def to_go_to_the_school(self):
        print("I am going to the school")
        self.progress+=7
    def to_have_the_class(self):
        print("I am on the lesson")
        self.progress+=15
        self.gladness-=50
    def is_alive(self):
        if self.progress < -0.5:
            print("i want to eat ")
        self.alive = False
    def live(self,day):
        day="Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube=random.randint(1,3)
        if live_cube==1:
            self.to_wakeup()
        elif live_cube==2:
            self.to_brush_the_teeth()
        elif live_cube==3:
            self.to_have_a_breakfast()
        self.to_get_dressed()
        self.to_go_to_the_school()
        self.to_have_the_class()
    class Part_Time_job:
        def __init__(self, job_list):
            self.job = random.choice(list(job_list))
            self.salary = job_list[self.job]["salary"]
            self.gladness_less = job_list[self.job]["gladness_less"]

    job_list = {
            "Java developer": {"salary": 50, "gladness_less": 10},
            "Python developer": {"salary": 40, "gladness_less": 3},
            "C++ developer": {"salary": 45, "gladness_less": 25},
            "Rust developer": {"salary": 70, "gladness_less": 1}}
    Student.live(day)


