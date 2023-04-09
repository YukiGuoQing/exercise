class Person:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    def get_age(self):
        return self._age

    def get_gender(self):
        return self._gender


def ste_dv(person_list):
    """

    :param person_list:
    :return:
    """
    sum_age = 0
    sum_sq = 0
    num = len(person_list)
    print(num)
    for person in person_list:
        sum_age += person.get_age()
    ave = sum_age / num
    print(ave)
    for person in person_list:
        sum_sq +=(person.get_age() - ave)**2
        print(sum_sq)
    ste = (sum_sq / num)**0.5
    return ste



def how_many_male(person_list):
    """
    Returns the amount of male persons in the person_list
    """
    num_male = 0
    for person in person_list:
        if person.get_gender() == "male":
            num_male += 1
    return num_male


def how_many_children_male(person_list):
    """
    Returns the amount of male persons(under 18) in the person_list
    """
    num_male_child = 0
    for person in person_list:
        if person.get_gender() == "male" and person.get_age() < 18:
            num_male_child += 1
    return num_male_child



p1 = Person("Kyoungmin", 73, "male")
p2 = Person("Mercedes", 24, "female")
p3 = Person("Beatrice", 48, "female")
p4 = Person("Ceatrice", 48, "male")
p5 = Person("Deatrice", 48, "female")
p6 = Person("Peatrice", 7, "male")
p7 = Person("Featrice", 15, "female")
p8 = Person("Geatrice", 48, "female")
p9 = Person("Jack", 4, "male")

test_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
test_list_2 = [p1, p2, p3]

print(ste_dv(test_list))

print(how_many_male(test_list))
print(how_many_children_male(test_list))
print(ste_dv(test_list_2))