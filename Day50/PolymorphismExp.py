

class Bird:

    def fly(self):
        print("flying")


class Sparrow(Bird):

    def fly(self):
        print("flying")

    def walk(self):
        print("walking")

class Peacock(Sparrow):

    def walk(self):
        print("Peacocking")
        print("walking")

    def fly(self):
        print("flying")


o = Peacock()
o.walk();