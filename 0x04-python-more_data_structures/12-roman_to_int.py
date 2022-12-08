#!/usr/bin/python3
def roman_to_int(roman_string):
    rd = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    match_list = list(roman_string.upper())
    return sum(list(map(lambda x: rd[x], match_list)))
