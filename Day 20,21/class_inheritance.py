class Animal():
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__() # inherits properties os super class Animal

    def breathe(self):  # modify inherited method
        super().breathe()   # performs breathes method from super class
        print("Breathes under water")

    def swim(self):
        print("Moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)