"""             --Simple Sorter--
    Sorts iterables by given order(str,dict or list).
    Useful if you need to sort things by an specific order you need.
"""

class Sorter:
    def __init__(self, order):
        if isinstance(order, dict):
            if not any(order.values()):
                self.order = {key: val for val, key in enumerate(order.keys())}
            else: self.order = order
        elif isinstance(order, str) or isinstance(order, list):
            self.order = {key: i for i, key in enumerate(order)}
        else:
            raise ValueError('Invalid type passed to order.It must be str,dict or list')

    def __sorter_func(self, obj) -> list:
        """
        :param obj: Any type of object which is an element of iterable.
        :return: List of object's integer values that based on given order dictionary.
        """
        result_array = list()
        for i in obj:
            is_valid = self.order.get(i)
            if is_valid:
                result_array.append(is_valid)
        return result_array

    def sort(self, iterable, reverse=False):
        return sorted(iterable, key=self.__sorter_func)

"""
letters_order1 = r"123456789abcçdefgğhıijklmnoöpqrsştuüvyz.- " #string order including turkish letters.
letters_order2 = {key: i for i, key in enumerate(letters_order1)} #dict order {key:val...}
letters_order3 = [key for key in letters_order1] #list order
letters_order4 = dict.fromkeys(letters_order3) #dict order {key:None,key2:None...}
strings = ['aac', 'aça', 'aüa', 'baa', 'bba', 'bab']

sorter1 = Sorter(letters_order1)
sorter2 = Sorter(letters_order2)
sorter3 = Sorter(letters_order3)
sorter4 = Sorter(letters_order4)
print(sorter1.sort(strings))
print(sorter2.sort(strings))
print(sorter3.sort(strings))
print(sorter4.sort(strings))

"""
