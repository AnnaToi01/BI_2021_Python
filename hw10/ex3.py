class PositiveSet(set):
    def __init__(self, collection):
        self.data = [element for element in collection if isinstance(element, (int, float)) and element > 0]
        super(PositiveSet, self).__init__(self.data)

    def add(self, element):
        """
        Add a positive element to a set.
        @param element: object
        @return: None
        """
        if isinstance(element, (int, float)) and element > 0:
            super(PositiveSet, self).add(element)
        return

    def update(self, collection):
        """
        Update the set with a collection of positive numbers
        @param collection: list/tuple/set
        @return: None
        """
        for element in collection:
            self.add(element)
        return

    def __ior__(self, other):
        """
        In place union operator - set1 |= set2
        @param other: set
        @return: self, updated set
        """
        self.update(other)
        return self

    def __or__(self, other):
        """
        In place union operator - set1 = set1 | set2
        @param other: set
        @return: self, updated set
        """
        self.update(other)
        return self


a = PositiveSet([1, 2, 3, 4, -100])
b = [-1, -2, -5, 6, 10, -20, 50]
a.add(-1)
print(a)
a.update(b)
print(a)
c = {5, 6, 7, -1, -14}
a |= c
print(a)
a = a | c
print(a)
