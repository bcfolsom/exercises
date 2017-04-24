

def catch_error ():
    while 1:
        try:
            x= int(input("Please enter a number: "))

        except ValueError:
            raise

if __name__ == ' __main__ ':
    catch_error()
