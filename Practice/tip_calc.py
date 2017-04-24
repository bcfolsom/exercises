sub = float(input("Total bill amount? $"))
lvl = input("Level of service? good/fair/bad ")
if lvl == "good":
    print("Tip amount: ${:.2f}".format(sub * .2))
    print("Total amount: ${:.2f}".format(sub * 1.2))
elif lvl == "fair":
    print("Tip amount: ${:.2f}".format(sub * .15))
    print("Total amount: ${:.2f}".format(sub * 1.15))
elif lvl == "bad":
    print("Tip amount: ${:.2f}".format(sub * .1))
    print("Total amount: ${:.2f}".format(sub * 1.1))
