#!/usr/bin/python3
"""
basic yield test script
"""
def yield_test():
    """
    basic yield test function
    """
    yield_str="This will print the first string"
    yield yield_str
    yield_str="This will print the second string"
    yield yield_str

multi_obj=yield_test()
print(next(multi_obj))
print(next(multi_obj))
