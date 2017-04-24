coins = 0
print("You have {} coins.".format(coins))
want = input("Do you want a another? ")
while want == "yes":
    coins += 1
    print("You have {} coins.".format(coins))
    want = input("Do you want a another coin? ")
    # if want == "yes":
    #     coins += 1
    # elif want == "no":
        # break

print ("Bye")
