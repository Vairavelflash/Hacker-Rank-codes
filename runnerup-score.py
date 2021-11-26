# my code
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    zes = max(arr)
    i=0
    while(i<n):
        if zes ==max(arr):
            # print(arr)
            arr.remove(max(arr))
            # print(arr,zes)
        i+=1
    print(max(arr))



# standard code
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr), reverse=True)[1])