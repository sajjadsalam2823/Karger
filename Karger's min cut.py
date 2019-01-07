"""
Assignment 4
200 vertices
randomized contraction algorithm is implemented to determine 
min cut
"""

import csv
import random

def makelist_list(A):
    """
    input: the read list of lists
    output: list of nodes (the first items)
    """
    nodes = []
    for item in A:
        nodes.append(item[0])
    return nodes

def readlist_list(filename):
    """
        input: the name of the txt file
        output: a list of lists containing the element of the array 
        in the txt file
    """
    array_lst = []
    with open(filename, "rt", newline = '') as csv_file:
        csv_read = csv.reader(csv_file)
        for row in csv_read:
            num_lst = row[0].split("\t")
            temp_lst = []
            for idx in num_lst:
                if idx != "":
                    temp_lst.append(int(idx))

            array_lst.append(temp_lst)

        
    return array_lst

    
def mincut(listn, listm):
    """
    input: two lists
           listn: list of nodes
           listm: list of edges
    output: min cut number!
    """
    
    while len(listn) > 2:
       A = random.randint(0, len(listn)-1)
       B = random.randint(0, len(listn)-1)
       if A != B:
           for palang in listm:
               if palang[0] == listn[A]:
                   target = palang
           for inq in listm:
               if inq[0] == listn[B]:
                   for idy in inq[1:]:
                       if idy != listn[A]:
                           target.append(idy)
                   listm.remove(inq)
           listn.remove(listn[B])
       else:
           pass
    min_cut = 0
    for entry in listm: 
        for item in entry:
            if item == listn[0] or item == listn[1]:
                min_cut += 1
    return min_cut-2

vals = [mincut(makelist_list(readlist_list("data.txt")),
               readlist_list("data.txt")) for i in range(20)]
print(vals)
              