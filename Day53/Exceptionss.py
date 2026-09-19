

# an abnormal flow of the program that is a mistake by User
# in runtime

ls = [1,2,3] #0,1,2
try:
    print(ls[2])
except ArithmeticError as e:
    print(e)
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
else :
    print("no exceptions we are good")

finally:
    print("Exceptions are done , and Exceptions chain is completed")
    print("Program  settled and objects or memory got cleared")






print("Hi Cyber t")
print("Program finished")
