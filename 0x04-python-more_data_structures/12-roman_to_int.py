#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    rom_num = 0
    rom_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    for i, j in zip(roman_string, roman_string[1:]):
        if i not in rom_dict.keys():
            return 0
        elif rom_dict[i] >= rom_dict[j]:
            rom_num += rom_dict[i]
        else:
            rom_num -= rom_dict[i]
    rom_num += rom_dict[roman_string[-1]]
    return rom_num
