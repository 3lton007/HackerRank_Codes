

def rearange(arr):

    arry = [(bin(x).count('1'), x) for x in arr]
    arry.sort()
    return [x[1] for x in arry]



def main():
    ele = [int(item) for item in input().split()]
    print(rearange(ele))
    
main()

""" 
def sort_asc_binary(arr):
    arr = [(bin(x).count('1'), x) for x in arr]
    arr.sort()
    return [x[1] for x in arr]

"""