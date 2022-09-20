#!/usr/bin/python3
def yield_test():
	yield_str="This will print the first string"
	yield yield_str
	yield_str="This will print the second string"
	yield yield_str

multi_obj=yield_test()
print(next(multi_obj))
print(next(multi_obj))


