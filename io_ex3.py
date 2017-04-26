file_name = input('Enter a file name: ')
def x (file_name):
    file_handle = open(file_name, 'r')
file=open(file_name, 'r')
wordcount = {}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print (word,wordcount)
file.close();

dic = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0, ' ': 0, '.': 0, '\n': 0}
dic2 = {}
file=open(file_name, 'r')
words = file.read()
def letter(words):
    for x in words:
        dic[x] = dic[x]+1
    for key, value in dic.items():
        if value != 0:
            dic2[key] = value
    print(dic2)
letter(words)
