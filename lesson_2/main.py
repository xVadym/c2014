import random
class Human:
    def __init__(self, name="Human", car=None, job=None, home=None):
        self.name=name
        self.money=100
        self.gladness=50
        self.satiety=50
        self.job=job
        self.home=home
        self.car=car

    def get_home(self):
        self.home=House()
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_reapir()
            return
        self.job=Job(job_list)
    def get_car(self):
        self.car=Auto(brand_of_car)
    def eat(self):
        if self.home.food<=0:
            self.shopping("food")
        else:
            if self.satiety>=100:
                self.satiety=100
                return
        self.satiety+=5
        self.home.food-=5
    def work(self):
        pass
    def shopping(self,manage):
        pass
    def chill(self):
        pass
    def clean_home(self):
        pass
    def to_reapir(self):
        pass
    def days_indexes(self,day):
        pass
    def is_alive(self):
        pass
    def live(self):
        pass

class Auto:
    def __init__(self, brand_list):
        self.brand=random.choice(list(brand_list))
        self.fuel=brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strenght"]
        self.consumption = brand_list[self.brand]["consumption"]


    def drive(self):
        if self.strength>0 and self.fuel>=self.consumption:
            self.fuel-=self.consumption
            self.strength-=1
            return True
        else:
            print("The car can not move")
            return False

class House:
    def __init__(self):
        self.food=0
        self.mess=0
brand_of_car = {
    "BMW": {"fuel": 100, "strenght": 100, "consuption": 12},
    "Toyota": {"fuel": 500, "strenght": 60, "consuption": 10},
    "Volvo": {"fuel": 70, "strenght": 150, "consuption": 8},
    "Ferrari": {"fuel": 80, "strenght": 150, "consuption": 14}}

job_list={
    "Java developer":{"salary":50, "gladness_less":10},
    "Python developer":{"salary":40, "gladness_less":3},
    "C++ developer":{"salary":45, "gladness_less":25},
    "Rust developer":{"salary":70, "gladness_less":1}}


class Job:
    def __init__(self,job_list):
        self.job=random.choice(list(job_list))
        self.salary=job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]




