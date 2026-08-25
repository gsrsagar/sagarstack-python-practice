


class Bird:
    def fly(self):
        return "it is flying"


class Peacock(Bird): #peacock

    def fly(self):
        base_fly = super().fly()
        print(f"{base_fly} and walking")


o = Peacock()
o.fly()