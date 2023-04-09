"""
class Building:

    def __init__(self, length, width, height, price_per_square):
        self._length = length
        self._width = width
        self._height = height
        self._price_per_square = price_per_square

    def area(self):
        area = self._length * self._width
        return area

    def get_length(self):

        return self._length

    def get_width(self):

        return self._width

    def get_height(self):

        return self._height

    def get_building_price(self):

        price = self.area() * self._price_per_square
        return price


class Customer:

    def __init__(self, name, region, money, intelligence):

        self._name = name
        self._region = region
        self._money = money
        self._intelligence = intelligence
    def get_name(self):

        return self._name

    def get_region(self):

        return self._region

    def get_money(self):

        return self._money

    def get_intelligence(self):

        return self._intelligence


class RealEstateAgent:

    def __init__(self,  num_of_employees):
        self._num_of_employees = num_of_employees

    def if_customer_rich(self, customer):
        if customer.get_money() > 100000:
            return True
        else:
            return False

    def if_perspective_customer(self, c, x):

        if c.get_money() >= x.get_building_price() and c.get_intelligence() == "smart":
            if self._num_of_employees >= 10:
                return True
            else:
                return False

        if c.get_money() >= x.get_building_price() and c.get_intelligence() == "silly":
            return True

        if c.get_money() < x.get_building_price():
            return False


def how_many_perspective_customers_for_a_certain_company(x, list_customer, house):

    num = 0
    for person in customer_list:
        if x.if_perspective_customer(person, house):
            num += 1

    return num


customer_1 = Customer("Ally", "Shanghai", 200000, "silly")
customer_2 = Customer("JingLiu", "Ningbo", 90000, "smart")
customer_3 = Customer("JingLu", "Beijing", 50000, "silly")
customer_4 = Customer("Jiu", "Guangzhou", 150000, "smart")
customer_5 = Customer("xu", "Guangzhou", 300000, "smart")
customer_list = [customer_1,customer_2,customer_3,customer_4,customer_5]

building_1 = Building(20, 5, 3, 1000)
print(building_1.get_building_price())

company_1 = RealEstateAgent(5)
company_2 = RealEstateAgent(20)
print(how_many_perspective_customers_for_a_certain_company(company_2, customer_list, building_1))
"""


class Building:

    def __init__(self, length, width, height, price_per_square):
        self._length = length
        self._width = width
        self._height = height
        self._price_per_square = price_per_square

    def area(self):
        area = self._length * self._width
        return area

    def get_length(self):

        return self._length

    def get_width(self):

        return self._width

    def get_height(self):

        return self._height

    def get_building_price(self):

        price = self.area() * self._price_per_square
        return price


"""
class Customer:

    def __init__(self, name, region, money, intelligence):

        self._name = name
        self._region = region
        self._money = money
        self._intelligence = intelligence

    def get_name(self):

        return self._name

    def get_region(self):

        return self._region

    def get_money(self):

        return self._money

    def get_intelligence(self):

        return self._intelligence
"""


class RealEstateAgent:

    def __init__(self,  num_of_employees):
        self._num_of_employees = num_of_employees

    def if_customer_rich(self, customer):
        if customer.get_money() > 100000:
            return True
        else:
            return False

    def if_perspective_customer(self, customer, building):
        """
        [customer is a list!!!]

        if c.get_money() >= x.get_building_price() and c.get_intelligence() == "smart":
        if self._num_of_employees >= 10:
            return True
        else:
            return False

        if c.get_money() >= x.get_building_price() and c.get_intelligence() == "silly":
            return True

        if c.get_money() < x.get_building_price():
            return False
        """
        if customer[2] >= building.get_building_price() and customer[3] == "smart":
            if self._num_of_employees >= 10:
                return True
            else:
                return False

        if customer[2] >= building.get_building_price() and customer[3] == "silly":
            return True

        if customer[2] < building.get_building_price():
            return False


def how_many_perspective_customers_for_a_certain_company(company, list_customer, building):

    num = 0
    for person in list_customer:
        if company.if_perspective_customer(person, building):
            num += 1

    return num


customer_1 = ["Ally", "Shanghai", 200000, "silly"]
customer_2 = ["JingLiu", "Ningbo", 90000, "smart"]
customer_3 = ["JingLu", "Beijing", 50000, "silly"]
customer_4 = ["Jiu", "Guangzhou", 150000, "smart"]
customer_5 = ["xu", "Guangzhou", 300000, "smart"]

customer_list_3 = [customer_1, customer_2, customer_3, customer_4, customer_5]

building_1 = Building(20, 5, 3, 1000)
print(building_1.get_building_price())

company_1 = RealEstateAgent(5)
company_2 = RealEstateAgent(20)
print(how_many_perspective_customers_for_a_certain_company(company_1, customer_list_3, building_1))
