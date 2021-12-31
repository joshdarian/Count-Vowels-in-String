# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 10:41:38 2021

@author: josh2
"""

def countVowels(s, v):
    vowelCount=0
    for letter in s:
        for vowel in vowels:
            if letter==vowel:
                vowelCount+=1
    return vowelCount

string='abcdefghijklmnopqrstuvwxyz'
vowels='aeiou'
print(countVowels(string, vowels))