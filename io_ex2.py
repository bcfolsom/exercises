#2 Write a program that prompts the user to enter a file name, then prompts the user to enter the contents of the file, and then saves the content to the file.

file_name = input('Give me a file name to write: ')
contents = input('Enter what you would like to write: ')
def x (file_name):

    file_handle = open(file_name, 'w')
    file_handle.write(contents)
    file_handle.close()
    print(x)

x(file_name)
