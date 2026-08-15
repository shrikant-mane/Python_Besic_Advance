
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def instance_display(self):
        print("instance")
        print(self.name)
        print(self.age)

    @classmethod
    def class_display(cls,obj):
        print("class")
        print(obj.name)
        print(obj.age)

    @staticmethod
    def static_display(obj):
        print("static")
        print(obj.name)
        print(obj.age)
        # print(Student.static_display())
student = Student("shrikant", 18)
# student.instance_display()
student.static_display(student)
student.class_display(student)