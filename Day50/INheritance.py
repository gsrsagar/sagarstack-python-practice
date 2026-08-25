class Engine:
    def __init__(self,name):
        self.name = name

    def start(self):
        print(self.name,"started")

    def stop(self):
        print(self.name,"stopped")

class Engine2:
    def __init__(self,name):
        self.name = name



class ToyataEngine(Engine,Engine2):
    def __init__(self,name):
        super().__init__(name)

    def display(self):
        print(self.name,"display")


class ToyataEngine2(ToyataEngine):
    def __init__(self,name):
        super().__init__(name)

engine = Engine("Electric")
engine.start()
engine.stop()


obj = ToyataEngine("Hydrogen")
obj.display()
obj.start()
obj.stop()
