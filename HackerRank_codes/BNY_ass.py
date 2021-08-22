import numpy as np

def mergeArrays(a,b):
    a1 = np.array(a)
    a2 = np.array(b)

    c = np.concatenate((a1,a2))

    d = sorted(c)
    return d

print(mergeArrays([1,3,5], [2,1,8]))



# def mergeArrays(a,b):  
#     c = a + b
#     return c

# print(mergeArrays([1,2,3], [2,5,5]))




# def mergeArrays(a,b):
    
#     a.extend(b)

#     return a

# print(mergeArrays([1,2,3], [2,5,5]))