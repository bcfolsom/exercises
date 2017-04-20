height = int(input("How tall is the box?: "))
width = int(input("How wide is the box?: "))

for i in range(height):
    if i in[0]:
        print("* "*(width))
    elif i in[(height - 1)]:
        print("* "*(width))
    else:
        print("*"+"  "*(width-2)+" *")
