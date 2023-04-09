def add_surname(list1):
    word = "K"
    surname = "Kardashian"
    list2 = [x + " " + surname for x in list1 if word in x[0]]

    return list2

print(add_surname(["Kiki", "Krystal", "Pavel", "MaryKay", "Annie", "Koala"]))