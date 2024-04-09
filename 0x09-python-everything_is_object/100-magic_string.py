#!/usr/bin/python3
def magic_string():
    magic_string.n += 1
    return ", ".join(["BestSchool" for i in range(magic_string.n)])
magic_string.n = 0
