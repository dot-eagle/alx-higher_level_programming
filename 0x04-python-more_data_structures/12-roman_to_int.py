#!/usr/bin/python3

def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        sol = 0
        val = 0
        roman_map = {
                "I": 1, "V": 5,
                "X": 10, "L": 50,
                "C": 100, "D": 500,
                "M": 1000
                }
        for ele in roman_string [::-1]: # 2
            val = roman_map[ele]
            if sol < val * 5:
                sol += val
            else:
                sol -= val
        return (sol)
    else:
        return (0)


    # roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
     #       'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}


