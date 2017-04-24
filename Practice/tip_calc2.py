sub = float(input("Total bill amount? $"))
lvl = input("Level of service? good/fair/bad ")
split = int(input("Split how may ways? "))
if lvl == "good":
    print("Tip amount: ${:.2f}".format(sub * .2))
    print("Total amount: ${:.2f}".format(sub * 1.2))
    print("Amount per person: ${:.2f}".format(sub * 1.2 / split))
elif lvl == "fair":
    print("Tip amount: ${:.2f}".format(sub * .15))
    print("Total amount: ${:.2f}".format(sub * 1.15))
    print("Amount per person: ${:.2f}".format(sub * 1.15 / split))
elif lvl == "bad":
    print("Tip amount: ${:.2f}".format(sub * .1))
    print("Total amount: ${:.2f}".format(sub * 1.1))
    print("Amount per person: ${:.2f}".format(sub * 1.1 / split))
