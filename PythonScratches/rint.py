class rint:
    """
        This class is used for referencing numerical operations.
        Operations must start with an instance of this class.
        Every instance of this class contains a private dictionary
        Which is used for further operations to change and apply new values into our final instance.
        Example:
            x = rint(7)
            array = [x * 5] --correct usage.this way our class is creating another instance from our class--
                            --its equal to array[rint(x * 5)]

            x.val = 2       --you must change value by using property.setter which is val in our class--
            print(array)
            >>[10]

        Wrong usage:
            x = rint(7)
            array = [5 * x] --this way our class doesnt work properly.Because you are being used int.__mul__ instead of
                            --rint.__mul__.So that we couldnt create an instance from our class.Check rint.__mul__ and
                            --rint.__create_new to get better understanding of what is going on.


        To understand better how this class works:
            x = rint(4)
            y = rint(6)
            array = [x * y - 2]

            #step 1 : array=[rint(x.val*y.val)-2]
            #step 2 : array=[rint(   rint( x.val * y.val ) - 2   )] --> result of whole operation is always an instance of rint class
            x.val = 7
            y.val = 9
            print(array)

            >>[61]

        Sorry if I made mistakes in english.
    """
    def __init__(self,value:int):
        self.__decimal = value
        self.__dict = {'made_by':{'number_1' : None, 'number_2': None, 'operator': ""} , 'part_of': None }


    def __create_new(self,other, operator):
        number_1 = self
        number_2 = other
        if operator == "__mul__":
            new_rint = rint(self.val * other.val)
        elif operator == "__add__":
            new_rint = rint(self.val + other.val)
        elif operator == "__truediv__":
            new_rint = rint(self.val / other.val)
        elif operator == "__sub__":
            new_rint = rint(self.val - other.val)
        elif operator == "__mod__":
            new_rint = rint(self.val % other.val)
        elif operator == "__floordiv__":
            new_rint = rint(self.val // other.val)
        elif operator == "__pow__":
            new_rint = rint(pow(self.val, other.val))
        else:
            raise print("Unsupported operation.")

        new_rint.made_by['number_1'] = number_1
        new_rint.made_by['number_2'] = number_2
        new_rint.made_by['operator'] = operator
        number_2.part_of = new_rint
        self.part_of = new_rint
        return new_rint


    @staticmethod
    def __check_type(other):
        assert str(other).isnumeric(), "Value is not numeric"
        if not isinstance(other, rint):
            other = rint(other)
        return other


    @property
    def val(self):
        return self.__decimal


    @val.setter
    def val(self,other):
        self.__decimal = other
        if self.part_of:
            operator = self.part_of.made_by['operator']
            part_of = self.part_of
            number_1 = part_of.made_by['number_1'].val
            number_2 = part_of.made_by['number_2'].val
            if operator == "__mul__":
                self.part_of.val = number_1 * number_2
            elif operator == "__add__":
                self.part_of.val = number_1 + number_2
            elif operator == "__truediv__":
                self.part_of.val = number_1 / number_2
            elif operator == "__sub__":
                self.part_of.val = number_1 - number_2
            elif operator == "__mod__":
                self.part_of.val = number_1 % number_2
            elif operator == "__floordiv__":
                self.part_of.val = number_1 // number_2
            elif operator == "__pow__":
                self.part_of.val = number_1 ** number_2


    @property
    def part_of(self):
        if 'part_of' in self.__dict.keys():
            return self.__dict['part_of']


    @part_of.setter
    def part_of(self,other):
        self.__dict['part_of'] = other


    @property
    def made_by(self):
        return self.__dict['made_by']


    def __repr__(self):
        return str(self.val)


    def __str__(self):
        return str(self.val)


    def __add__(self, other):
        return self.__create_new(rint.__check_type(other),"__add__")


    def __sub__(self, other):
        return self.__create_new(rint.__check_type(other),"__sub__")


    def __mul__(self, other):
        return self.__create_new(rint.__check_type(other),"__mul__")


    def __truediv__(self, other):
        return self.__create_new(rint.__check_type(other),"__truediv__")


    def __mod__(self, other):
        return self.__create_new(rint.__check_type(other), "__mod__")


    def __floordiv__(self, other):
        return self.__create_new(rint.__check_type(other), "__floordiv_")


    def __pow__(self, power, modulo=None):
        return self.__create_new(rint.__check_type(power), "__pow__")
