# 3 Write a program that prompts the user to enter a file name, then prints the
# letter histogram and the word histogram of the contents of the file.

file_name = input('Give me a file name to write: ')
contents = input('Enter what you would like to write: ')
def x (file_name):

    file_handle = open(file_name, 'w')
    file_handle.write(contents)
    file_handle.close()

x(file_name)

dic = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
dic2 = {}

word = input('Give me a word: ').lower()
def letter(word):
    for x in word:
        dic[x] = dic[x]+1

    for key, value in dic.items():
        if value != 0:
            dic2[key] = value

    print(dic2)

letter(word)
