amt = float(input("Total bill amount? "))
lvl = input("Level of service? ")
people = float(input("Split how many ways? "))
if lvl == "good":
    print ("Tip amount: ${}".format (amt * .20))
    print ("Total amount: ${}".format (amt * 1.20))
    print ("Amount per person: ${}".format (amt * 1.20 / people))
elif lvl == "fair":
    print ("Tip amount: ${}".format (amt * .15))
    print ("Total amount: ${}".format (amt * 1.15))
    print ("Amount per person: ${}".format (amt * 1.15 / people))
elif lvl == "bad":
    print ("Tip amount: ${}".format (amt * .10))
    print ("Total amount: ${}".format (amt * 1.10))
    print ("Amount per person: ${}".format (amt * 1.10 / people))
