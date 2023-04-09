mm = ["Mary","had","a","little","lamb"]
print(len(mm[::1][::1][::1]))
count = [1, 2, 3, 4, 5]
print(len(count))

some_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]  # list with integers
some_names = ["Groucho", "Harpo", "Chico", "Zeppo", "Karl"]  # list with strings
some_stuff = [98, "Fido", -34.925, ["Phantom", "Tollbooth"]]  # list with a mix of integer, string, float, and nested list objects
one = ["just me"]  # a singleton list
zero = []  # an empty list

print(some_primes[0])
print(some_primes[0:10:2])
print(some_names[::-2])

print(some_stuff[3])
print(some_stuff[3][1])
print(some_stuff[3][1][0])

print(13 in some_primes)
print(13 not in some_primes)
print("Fido" in some_stuff)
print("Phantom" in some_stuff)
print("Phantom" in some_stuff[3])

odds = [7, 5, 9, 1, 13, 11, 3] #odd numbers
evens = [8, 4, 10, 6, 2] #even numbers
palindromes = ["hannah", "tacocat", "bob", "mom", "dad"]
print(min(odds))
print(max(palindromes))

print(evens.sort())
print(evens)

sorted_odds = sorted(odds)
print(sorted_odds)
print(odds)

print(evens + odds)

fun_floats = [3.141, 2.718, 6.283, 1.618, 1.414, 2.502, 0.577, 1.303, 2.685, 1.282]
for number in fun_floats:
    print(number)


total = 0
for number in fun_floats:
    total += number
print(total)


class BankAccount:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance

    def get_balance(self):

        return self.balance


account_1 = BankAccount("235349", 730.29)
account_2 = BankAccount("783848", 240.89)
account_3 = BankAccount("732005", 1390.20)
account_list = [account_1, account_2, account_3]
print(account_list[0].get_balance())

print([2 * n for n in fun_floats])
print([2*x for x in range(1,11)])
print([2*x for x in range(1,11) if x % 2 == 1])


