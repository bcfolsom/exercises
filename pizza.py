pizza = input("Would you like some pizza?: ")
if pizza == 'yes':
    slices = int(input("How many slices would you like?: "))
    if pizza == 'yes' and slices >= 1:
        print("Call Papa John.")
else:
    print ("Have a salad.")
    if pizza == 'no':
        print("Have a salad.")
