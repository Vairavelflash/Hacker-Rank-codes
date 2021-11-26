def average(array):
    # your code goes here
    tot = 0
    for i in set(array):
        tot = tot+i
    avg = tot/len(set(array))
    # print (tot,len(array))
    
    return avg
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


# standard code
def average(array):
    # your code goes here
    array = set(array)
    return sum(array) / len(array)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)