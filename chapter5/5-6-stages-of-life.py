age = 0

if (age < 2):
    print("This person is a baby.")
elif (age == 2 or age < 4):
    print("This person is a toddler.")
elif (age == 4 or age < 13):
    print("This person is a kid.")
elif (age == 13 or age < 20):
    print("This person is a teenager.")
elif (age == 20 or age < 65):
    print("This person is an adult.")
elif (age >= 65):
    print("This person is an elder.")
else:
    print("Invalid input, please try again.")
