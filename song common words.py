# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 16:02:36 2018

@author: pgaiton
"""

def lyrics_to_freq(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

def most_common_words(freq_dict):
    values = freq_dict.values()
    max1 = max(values)
    words = []
    for keys in freq_dict:
        if freq_dict[keys] == max1:
            words.append(keys)
    return (words,max1)

def words_often(freq_dict, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freq_dict)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freq_dict[w])
        else:
            done = True
    return result
