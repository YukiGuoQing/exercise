def rev_string_list(list1):
    """rev_string_list1 = list1[::-1]"""
    list2 = [x[::-1] for x in list1]
    return list2

print(rev_string_list(["Wayne", "Katie", "Daryl", "Dan"]))

