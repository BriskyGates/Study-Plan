"""
题目描述
找出一个包含三个连续双字符的单词。我将给你一系列几乎能够符合条件但实际不符合的单词。
比如，committee这个单词，c-o-m-m-i-t-t-e-e。 如果中间没有i的话，就太棒了。
或者Mississippi这个单词: M-i-s-s-i-s-s-i-p-p-i。假如将这些i剔除出去，
就会符合条件。但是确实存在一个包含三个连续的单词对， 而且据我了解，
它可能是唯一符合条件的单词。 当然也可能有500多个，但是我只能想到一个。那么这个单词是什么？
"""
"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""


def is_triple_double(word):
    """Tests if a word contains three consecutive double letters.

    word: string

    returns: bool
    """
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2  # 跳过当前字符和下一个字符
        else:
            i = i + 1 - 2 * count
            count = 0
    return False


def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


print('Here are all the words in the list that have')
print('three consecutive double letters.')
find_triple_double()
print('')
