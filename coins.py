coins = 0
while True:
    print("You have {} coins.".format(coins))
    want = input("Do you want a coin? ")
    if want == "yes":
        coins += 1
    elif want == "no":
        break

print ("Bye")
