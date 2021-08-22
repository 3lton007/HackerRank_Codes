"""
Neice will blow the tallest candles \ 
in her birthday 
@eltonaloys
"""

def candles(a):
    print(a.count(max(a)))


def main():
    s = int(input())
    a = [int(item) for item in input().split()]
    candles(a)
main()