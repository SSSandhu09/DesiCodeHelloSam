class human:
  def detailsInput(self):
    self.name = input("Enter your name:");
    self.age = input("Enter your age:");
    self.profession = input("Enter your Profession:")
  def printDetails(self):
    print(f"Name:{self.name} \nAge:{self.age} \nProfession:{self.profession}")

samnit = human()
samnit.detailsInput()
samnit.printDetails()
