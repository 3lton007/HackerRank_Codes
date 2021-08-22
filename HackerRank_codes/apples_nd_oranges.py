"""

To see if apples or oranges fall on sams house 
@eltonaloys
"""

def app_oran(s,t,a,b,apples,oranges):
    apples_add = []
    cnt_a = 0
    cnt_o = 0

    for items in apples:
        k = a + items
        if k >= s and k <= t:
            cnt_a += 1
    print(cnt_a)

    for items in oranges:
        l = b + items
        if l >=s and l <= t:
            cnt_o += 1
    print(cnt_o)
    
    

def main():
    st = (input().split())
    s = int(st[0])  #starting of sams house
    t = int(st[1])  #ending of sams house
    
    ab = input().split()
    a = int(ab[0])  #apple tree
    b = int(ab[1])  #orange tree
    
    jk = input().split()

    apples = [int(item) for item in input().split()]
    oranges = [int(item) for item in input().split()]
    
    app_oran(s,t,a,b,apples,oranges)
    
if __name__ == "__main__":
    main()
