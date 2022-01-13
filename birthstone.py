# Follow the assignment instructions to code an app that
# will tell a user their birthstone.

user_input = input("Enter the number of the month you were born (1-12) > ")
month = int(user_input)
if month == 1:
    stone = "Garnet"
elif month == 2:
    stone = "Amethyst"
elif month == 3:
    stone = "Aquamarine"
elif month == 4:
    stone = "Diamond"
elif month == 5:
    stone = "Emerald"
elif month == 6:
    stone = "Moonstone"
elif month == 7:
    stone = "Ruby"
elif month == 8:
    stone = "Peridot"
elif month == 9:
    stone = "Sapphire"
elif month == 10:
    stone = "Opal"
elif month == 11:
    stone = "Citrine"
elif month == 12:
    stone = "Turquoise"
print("Your birthstone is ", stone)
