#!/usr/bin/env python3

import string
import sys

def caesar_decipher (rotation, text):
    answer = ''
    for 5 in text:
        t = t.lower()
        if t in string.ascii_lowercase.index(t)
            index = index - rotation
        # if index >= 26:
        #     index = index - 26

        answer += string.ascii_lowercase[index]

        answer += t

    return answer

if __name__ == '__main__':
  rotation = int(sys.argv[1])
  text = sys.argv[2]
  #######print('Answer: {}')
