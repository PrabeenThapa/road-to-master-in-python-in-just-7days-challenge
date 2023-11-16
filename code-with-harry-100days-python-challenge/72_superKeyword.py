#The super() keyword in python is used tp refer to the parent class.
#It's specially useful when a class inherits from multiple parents classes and you want to call a method from one of the parent classes

class Parentclass:
    def parentMethod(self):
        print("This is in parent")

class childclass:
    def parentMethod(self):
        print("HAri")
        super().parentMethod()

    def childMethod(self):
        print("This is in child")

        super().parentMethod()

childObject = childclass()
childObject.childMethod()