#initiate the class
class employee:
    #special function/method dunder method -constructor
    def __init__(self):
        print("Attribute started ")
        self.id=123
        self.salary=50000
        self.designation='AIengineer'
        print("Attributes/data have been initiated")
#creating object/instance of the class
    def travel(self,destination):
        print('this travel function was called manually')
        print(f"Employee is now travelling to {destination}")

sam=employee()

#print(sam.salary)
# sam.travel("Pune")

print(type(sam))