if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sortedArr = sorted(arr,reverse=True)    
    highest = sortedArr[0]
    for x in (sortedArr):
        if(x == highest):
            continue
        else:
            secondHighest = x
            break
    print(secondHighest)
