amt = float(input("Total bill amount? "))
lvl = input("Level of service? ")
if lvl == "good":
    print ("Tip amount: ${}".format (amt * .20))
    print ("Total amount: ${}".format (amt * 1.20))
elif lvl == "fair":
    print ("Tip amount: ${}".format (amt * .15))
    print ("Total amount: ${}".format (amt * 1.15))
elif lvl == "bad":
    print ("Tip amount: ${}".format (amt * .10))
    print ("Total amount: ${}".format (amt * 1.10))
