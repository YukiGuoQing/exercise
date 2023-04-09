def find_median(list1):
    list1.sort()
    list2 = list1
    num = len(list2)
    print(list2)
    num1 = 0
    median = 0
    if num % 2 == 0:
        for ele in list2:
            num1 += 1
            if num1 > num/2:
                median = (list2[num1-1]+list2[num1-2])/2
                return median
    else:
        for ele in list2:
            num1 += 1
            if num1 > num/2:
                median = list2[num1-1]
                return median


print(find_median([13, 7, -3, 82, 4]))
