#!/usr/bin/python3
def magic_string():
    magic_string.iteration = getattr(magic_string, "iteration", 0) + 1
    return ", ".join(["BestSchool"  for i in range(magic_string.iteration)])
