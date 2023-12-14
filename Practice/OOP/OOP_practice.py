
class Student:
  def __init__(self, name, house):
    #This assignment should not have underscore as then the setter function would be accessed
    #With the underscore, then the attribute assignment would be independent of the setter function
    self.name = name
    self.house = house

  def __str__(self):
    #Instead of printing the cryptic hex-decimal location of the object memory address, it prints this easier read sentence
    print(f"{self.name} from {self.house}")

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    if not name:
      raise ValueError("Missing Name")
    self._name = name

  #Getter (Gets attribute)
  @property
  def house(self):
    #Put underscore to not collide with the self.house = house in __init__ 
    return self._house
  
  #Setter (Sets Attribute)
  @house.setter
  #The function and the call must have the same name for the setter function to be executed
  #This function would always be called if anything in form instance_name.house is called 
  def house(self, house):
    if house not in ["Gryffindor, Hufflepuff", "Ravenclaw", "Slytherin"]:
      raise ValueError("Invalid House")
    self._house = house

  # Classmethods allows function to be called without an instance, but directly using the class name like Student.get()
  @classmethod
  def get(cls):
    name = input("Name: ")
    house = input("House: ")
    return cls(name, house)    


def main():
  student = Student.get()
  #This allows users to change the attribute of the class, making it not secure NEEDS ERROR CHECKING!
  #By setting the setter function, it would execute the setter function automatically to prevent users to change the value
  student.house = "Number Four, Privet Drive"
  #studnet._house = "Number Four, Privet Drive" with an underscore would still change it (Private)
  print(student)

if __name__ == "__main__":
  main()