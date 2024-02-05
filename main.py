class human:
  def detailsInput(self):
    self.name = input("Enter your name:");
    selfage = input("Enter your age:");

  def printDetails(self):
    print(f"Name:{self.name} \nAge:{self.age}")

samnit = human()
samnit.detailsInput()
samnit.printDetails()
