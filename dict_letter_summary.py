# Write a letter_histogram function that takes a word as its input, and returns
# a dictionary containing the tally of how many times each letter in the
# alphabet was used in the word. For example:
# >>> letter_histogram('banana')
# {'a': 3, 'b': 1, 'n': 2}
dic = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
dic2={}

def letter_histogram(str):
    for x in str:
        dic[x] = dic[x]+1

        for key, value in dic.1tems():
            if value != 0:
                dic2[key] = value

        print(dic2)
letter_histogram('banana')
