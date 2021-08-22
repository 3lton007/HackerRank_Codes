  """

To Compare triplets
@eltonaloys
"""

def cmp_triplets(a,b):
    """ To compare triple values """
    alice = 0
    bob = 0
    for i in range(3):
        if a[i] > b[i]:
            alice = alice + 1
        elif a[i] < b[i]:
            bob = bob + 1

    print(alice,bob)
    

def main():
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]

    (cmp_triplets(a,b))
    

main()