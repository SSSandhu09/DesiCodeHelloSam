class human:
  def detailsInput(self):
    name = input("Enter your name:");
    age = input("Enter your age:");

  def printDetails(self):
    print(f"Name:{self.name} \nAge:{self.name}")

samnit = human()
samnit.detailsInput()
samnit.printDetails()
