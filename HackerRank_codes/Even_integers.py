
"""

Even Integers 

"""

def even(start, n):
    result = list()

    if start % 2 == 1:
        # Make start even
        start += 1

    while len(result) < n:
        # Adding start to the result list
        result.append(start)
        # Incrementing start by 2
        start += 2

    return result

def main():
    start = int(input())
    n = int(input())

    print(even(start, n))

main()
