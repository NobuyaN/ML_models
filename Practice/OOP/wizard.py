class Wizard:
  def __init__(self, name):
    if not name:
      raise ValueError("Missing Name")
    self.name = name

class Student(Wizard):
  def __init__(self, name, house):
    #Super() is the parent class Wizard, getting the __init__ method from it
    super().__init__(name)
    self.house = house

class Professor(Wizard):
  def __init__(self, name, subject):
    super().__init__(name)
    self.subject = subject

student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")