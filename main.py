print("How old is Izzy? Let's find out.")
bday = 2008
today = int(input("Enter today's year in YYYY format: "))
age = today - bday
catyears = age * 5
print("Izzy is {} years old this year.".format(age))
input("Hit enter to see how old that is in cat years.")
print("Izzy is {} in cat years!".format(catyears))