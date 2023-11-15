#Sara Willems (2575861)
#Saeideh Asari(2572893)

import sys

class Bloom_Filter:

    def __init__(self, n):
        self.n = n
        self.hash_table = [0] * self.n  # Hash table of size n

    # Hash function 1
    def h1(self, s):
        hash = 5381
        for c in s:
            hash = ((hash << 5) + hash) + ord(c)
        return hash % self.n

    # Hash function 2
    def h2(self, s):
        hash = 0
        for c in s:
            hash += ord(c)
        return hash % self.n

    # Add all the elements which are given in the input file
    def add(self, element):
        self.hash_table[self.h1(element)] = 1
        self.hash_table[self.h2(element)] = 1

    # To check if the element is present in our elements_set or not.
    def contains(self, element):
        if (self.hash_table[self.h1(element)] == 1) and (self.hash_table[self.h2(element)] == 1):
            return True

        else:
            return False

    # To print out the results
    def output(self, element):
        T = {True:"T", False:"F"}
        print(str(self.h1(element))+","+(str(self.h2(element))+","+ T[self.contains(element)]))


script = sys.argv[0]
n = int(sys.argv[1])
elements = sys.argv[2]
string = sys.argv[3]

# object a
a = Bloom_Filter(n)


#to get set_of_elements
with open('input.txt', 'r') as input_file:
    for element in input_file.readlines():
        a.add(element.rstrip('\n'))


#to get the test element in order to check if
#they are available in set_of_elements or not
with open ('test.txt', 'r') as test_file:
    for string in test_file.readlines():
        a.output(string.rstrip('\n'))