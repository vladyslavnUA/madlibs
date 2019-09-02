# madlibs
location = input("Enter a very specific location: ")
vehicle = input("Enter a vehicle: ")
number = input("Enter a number: ")
verb = input("Enter a verb: ")
time = input("Enter a length of time: ")
option = input("In minutes/hours? ")
color = input("Enter a colour: ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")

"""def option(select):
    imp = input("minutes/hours? (m/h)")
    if imp == "m":
        print("minutes")
    else:
        print("hours")
"""

def list(option):
    print("In minutes/hours? ")
    lst = ["minutes", "hours"]
    for i in range("minutes", "hours"):
        ele = input()
    if ele == "minutes":
        print("minutes")
    elif ele == "hours":
        print("hours")

print(" ")
print("Today we will take a trip to the amusement park that is inside the " + str(location) + ".")
print("Let's use the " + str(vehicle) + " I got for my birthday!")
print("The speed limit is only " + str(number) + " mph, yet there is still so much traffic!")
print("As we drive down the road, many 'No " + str(verb) + "ing' signs begin to appear.")
print("We have finally reached the destination in " + str(time) + " " + str(option) + ".")
print("As we enter the amusement park with big " + str(color) + " coloured gates, we see")
print("a lot of " + str(adjective) + " people who are roaming around.")
print("Suddenly, out of the blue, a " + str(animal) + " runs across to hide in the bush.")
print(" ")
print("End of story, I hope you enjoyed. :)")
print(" ")
