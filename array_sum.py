def array_sum(list1):
    num = 0
    for ele in list1:
        num += len(ele)
    return num

print(array_sum(["Wayne", "Katie", "Daryl", "Dan"]))


def array_sum(list1):
    num = 0
    for ele in list1:
        for ele1 in ele:
            num += 1
    return num

print(array_sum(["Wayne", "Katie", "Daryl", "Dan", "www"]))

