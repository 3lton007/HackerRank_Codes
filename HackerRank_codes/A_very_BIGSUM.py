"""

Sum of big integers
@eltonaloys
"""


def bigsum(arr):
    sum = 0
    for ele in arr:
        sum = sum + ele
    print(sum)

def main():
    print("Enter Digits\n")
    a = input()
    arr = [int(item) for item in input().split()]
    bigsum(arr)

main()