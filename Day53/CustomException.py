


class LessThen18Excpetion(Exception):
    pass




def _funcCreate(a):
    if a<18:
        raise LessThen18Excpetion("Exception The users age is less than 18")
    else:
        print("The users age 18")


try:
    _funcCreate(17)
except LessThen18Excpetion as e:
    print(e)
