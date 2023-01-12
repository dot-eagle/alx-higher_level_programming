#!/usr/bin/python3

def roman_to_int(value):

    roman_map = {
            1: "I", 5: "V",
            10: "X", 50: "L",
            100: "C", 500: "D",
            1000: "M",
            }
    result = ""
    remainder = value

    for i in sorted(roman_map.keys(), reverse=True):# 2
        if remainder > 0:
            multiplier = i
            roman_digit = roman_map[i]


            times = remainder // multiplier         # 3
            remainder = remainder % multiplier      # 4
            result += roman_digit * times           # 4


    return result
