import numpy as np

def deadend(pagex,pagey):
    deadend=[]
    deletepoint=[]
    for i in range(len(pagex)):
        if pagey[i] not in pagex:
            deadend.append(pagey[i])
            deletepoint.append(i)
    print ("deadend is ")
    print (len(deadend))

    original=0
    while original!=len(deletepoint):
        original=len(deletepoint)
        for i in range(len(pagex)-len(deletepoint))
            if i not in deletepoint:
                if pagey[i] not in pagex:
                    deadend.append(pagey[i])
                    deletepoint.append(i)
        print ("deadend is ")
        print (len(deadend))

    print ("deadend is ")
    print (len(deadend))
    return deadend,deletepoint
