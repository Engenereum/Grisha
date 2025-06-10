class Bike:
    def __init__(self):
        self.color = 'black'
        self.weight = 12
        self.max_speed = 12

    def get_color(self):
        print(f'цвет велосипеда {self.color}.')

    def ride(self, distance):
        time = distance / self.max_speed
        print(f'Мин время преодоления {distance} километров - {time} часов.')

    def __repr__(self):
        return "bike"


bike = Bike()
bike.get_color()
bike.color = 'чорный'
bike.get_color()
bike2 = Bike()
bike2.get_color()


class PC:
    def __init__(self,proc,tip,ves,size,points):
        self.proc = proc
        self.tip =  tip
        self.ves = ves
        self.size = size
        self.bench = points
    def get_bench(self):
        print(f'your {self.tip} get {self.bench} points')

    @staticmethod
    def poweron():
        print('pc is on')

    def __repr__(self):
        return f'обьект {self.tip} класса PC'



pc = PC('core i5','pc' , 123,123,123)

pc.poweron()
pc.get_bench()

pc.bench = '7800'
pc.get_bench()




class Laptop(PC):
    def __init__(self,proc,ves,size,points):
        super().__init__(proc, 'laptop',ves,size,points)



...

