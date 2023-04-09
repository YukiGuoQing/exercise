def contain_string(list_contains_letter, string):

    list2 = [letter for letter in list_contains_letter if string in letter]

    return list2

print(contain_string(['cats', 'tacks', 'scat', 'stack'], "cat"))

"""

"cat" in ['cats', 'tacks', 'scat', 'stack', 'cat'] = false

"cat" in 'cats' = true
"cat" in 'tacks' = false
"cat" in 'scat' = true
"cat" in 'stack' = false

"""