#multilevel inheritance

class Project:
    def _init_(self):
        self.projectid = None
        self.projectname = None

    def getproj_details(self):
        self.projectname = input("Enter the name of the project: ")
        self.projectid = int(input("Enter the ID of the project: "))

    def setproj_details(self):
        print(f"Name of the project is {self.projectname} and its ID is {self.projectid}")


class Module(Project):
    def _init_(self):
        super()._init_()   # call Project constructor
        self.modulename = None

    def getmodule_details(self):
        self.modulename = input("Enter the name of the module: ")

    def setmodule_details(self):
        print(f"Name of the module is {self.modulename}")


class Task(Module):
    def _init_(self):
        super()._init_()   # call Module constructor
        self.taskname = None

    def gettask_details(self):
        self.taskname = input("Enter the name of the task: ")

    def settask_details(self):
        print(f"Name of the task is {self.taskname}")


obj = Task()  

obj.getproj_details()
obj.getmodule_details()
obj.gettask_details()

print("\n--- Project Information ---")
obj.setproj_details()
obj.setmodule_details()
obj.settask_details()