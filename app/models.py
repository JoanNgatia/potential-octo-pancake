"""Models.py.

Define base classes for Spaces and people.
"""


class Person(object):
    """Define person features."""

    def __init__(self, name):
        """
        Initialise new person.

        Arguments:
            name {[string]} -- [person's name]
        """
        self.name = name
        self.office = None

    def allocate_office(self, office):
        """Assign anyone an office."""
        self.office = office


class Fellow(Person):
    """Define specific fellow features."""

    def __init__(self, wants_housing='N'):
        """Initialize with option to choose housing."""
        self.livingspace = None
        self.wants_housing = True if wants_housing == 'Y' else False


class Staff(Person):
    """Define Staff subclass."""

    pass


class Room(object):
    """Define room space at Amity."""

    max_occupancy = 0

    def __init__(self, name):
        """
        Initialize new room.

        Arguments:
            name {[string]} -- room name
        """
        self.name = name
        self.members = []

    def get_members(self):
        return self.members

    def check_max_occupancy(self):
        return len(self.members)


class Office(Room):
    """Model office space."""

    max_occupancy = 6


class LivingSpace(Room):
    """Model office space."""

    max_occupancy = 4
