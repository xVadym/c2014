import random
class Vadym:
    def __init__(self,name):
        self.name=name
        self.gladness=50
        self.progress=0
        self.alive=True
        self.energy=5

    def to_wakeup(self):
        print("I get up")
        self.progress+=4
        self.gladness-=3
        self.energy+=10
    def to_brush_my_teeth(self):
        print("I am brushing my teeth")
        self.progress+=2
        self.gladness -= 3
        self.energy += 10
    def to_have_breakfast(self):
        print("time to have a breakfast")
        self.progress+=2
        self.gladness -= 5
        self.energy+=5
    def to_go_to_the_school(self):
        print("time to go to the school")
        self.progress+=3
        self.gladness-=3
        self.energy -= 2
    def to_have_lunch(self):
        print("time to have a lunch")
        self.progress+=2
        self.gladness+=3
        self.energy += 7
    def to_doing_homework(self):
        print("time to doing homework")
        self.progress+=1
        self.gladness-=1
        self.energy -= 3
    def to_chill(self):
        print("I am tired...\n I want to chill")
        self.progress += 2
        self.gladness -= 4
        self.energy += 6
    def to_have_dinner(self):
        print("I want to eat")
        self.progress += 1
        self.gladness -= 3
        self.energy += 7

    def to_go_to_the_bed(self):
        print("I want to go to the bad")
        self.progress += 1
        self.gladness -= 2
        self.energy += 15

    def is_alive(self):
        if self.progress < -5:
            print("i want to do something")
            self.alive = False
        elif self.gladness <= 0:
            print("I am bored")
            self.alive = False
        elif self.progress > 5:
            print("Passed externaly")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress,2)}")

    def live(self,day):
        day="Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube=random.randint(1,3)
        if live_cube==1:
            self.to_wakeup()
        elif live_cube==2:
            self.to_have_breakfast()
        elif live_cube==3:
            self.to_go_to_the_school()
        self.end_of_day()
        self.is_alive()
class cat:
    def __init__(self,name):
        self.name=name
        self.gladness_less=50
        self.alive=True

    def to_feed_cat(self):
        print("Let`s feed Persyk")
        self.gladness_less -= 4
    def to_play_with_cat(self):
        print("Let`s play with him")
        self.gladness_less -= 5
    def to_pet(self):
        print("I want to pet him")
        self.gladness_less -= 4

Vadym=Vadym(name="Vadym")
for day in range(365):
    if Vadym.alive==False:
        break
    Vadym.live(day)
