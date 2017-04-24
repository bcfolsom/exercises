# coins = 0
# yes = True
# while coins < 1:
#     print(str("You have " + str(coins) + " coins."))
#     input("Do you want another? ")
#     if 'yes':
#         coins += 1
#         print(str("You have " + str(coins) + " coins."))
#     else:
#         print("Bye")
#         break

coins = 0
while want == 'yes':
    print("You have {} coins.".format(coins))
    input("Do you want another? ")
if 'yes':
    coins += 1
    print("You have {} coins.".format(coins + 1))
    input("Do you want another? ")
else:
    break

print ("Bye")
