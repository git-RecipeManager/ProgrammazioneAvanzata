from collections.abc import Hashable
import logging

logging.basicConfig(level=logging.DEBUG)


class MyDict:

    def __init__(self, l=None):
        if l is None:
            self.l = []
        else:
            self.l = l

    def __call__(self, *args, **kwargs):
        return self.l

    # Classe interna MyPair
    class MyPair:
        def __init__(self, key: Hashable, value: object):
            if isinstance(key, Hashable):
                self.key = key
                self.value = value

        def getkey(self):
            return self.key

        def getvalue(self):
            return self.value

        def setvalue(self, value: object):
            self.value = value

        def __str__(self):
            return f"({self.getkey()}, {self.getvalue()})"

    # continua MyDict
    def __len__(self):
        logging.info("I'am in __len__")
        return len(self.l)

    def __eq__(self, other: "MyDict") -> bool:
        logging.info("I'am in __eq__")
        """
               Two dictionary are exactly the same only if each pair match.
               Two pair match only if the keys match and the values match.

               :param   other: dictionary on which the comparison takes place

               :return: True if the self dictionary and other are the same
                        False otherwise.
        """

        if len(self.l) != len(other):
            return False
        # So, the two lists have the same length
        for i in range(0, len(self.l)):
            lpair = self.l[i]
            otherpair = other.l[i]
            if lpair.getkey() != otherpair.getkey():
                return False
            if lpair.getvalue() != otherpair.getvalue():
                return False
        return True

    def __contains__(self, key: Hashable) -> bool:
        logging.info("I'am in __contains__")
        if not isinstance(key, Hashable):
            raise TypeError("Un-hashable type: {}".format(str(type(key))))
        for pair in self.l:
            if pair.getkey() == key:
                return True
        return False

    def __getitem__(self, key) -> object:
        logging.info("I'am in __getitem__")
        if not isinstance(key, Hashable):
            raise TypeError("Un-hashable type: {}".format(str(type(key))))
        for pair in self.l:
            if pair.getkey() == key:
                return pair.getvalue()
        raise KeyError(key)

    def __setitem__(self, key: Hashable, value: object):
        logging.info("I'am in __setitem__")
        if not isinstance(key, Hashable):
            raise TypeError("Un-hashable type: {}".format(str(type(key))))
        for pair in self.l:
            if key == pair.getkey():
                pair.setvalue(value)
                return self
        self.l.append(self.MyPair(key, value))
        return self

    def __delitem__(self, key: Hashable):
        logging.info("I'am in __delitem__")
        if not isinstance(key, Hashable):
            raise TypeError("Un-hashable type: {}".format(str(type(key))))
        clista = self.l[:]
        for index, pair in enumerate(clista):
            if pair.getkey() == key:
                self.l.pop(index)
                return self

    def __str__(self):
        logging.info("I'am in __str__")
        if len(self.l) == 0:
            return "{}"
        stringa = "{"
        for index, pair in enumerate(self.l):
            if index < len(self.l) - 1:
                stringa += f"{pair}, "
            else:
                stringa += f"{pair}"
        stringa += "}"
        return stringa


# Make two instance of MyDict class and  check the length

soccerTeam = MyDict()
anotherSoccerTeam = MyDict()
print(soccerTeam)
print(soccerTeam)
print(f"la lunghezza del dizionario soccerTeam è: {len(soccerTeam)}")
print(f"la lunghezza del dizionario anotherSoccerTeam è: {len(anotherSoccerTeam)}")
print()

# Adding pair to the  dictionaries by  __setitem__()
soccerTeam["Avellino"] = "Avellino"
soccerTeam["Torino"] = ["Torino", "Juventus"]
print(soccerTeam)
anotherSoccerTeam["Avellino"] = "Avellino"
anotherSoccerTeam["Torino"] = ["Torino", "Juventus"]
print(anotherSoccerTeam)
print()

# Equality check by __eq__()
print(soccerTeam == anotherSoccerTeam)
print()

# # Getting value by key: __getitem__()
print(soccerTeam["Torino"])
print()

# # through the iterator object
for pair in anotherSoccerTeam():
    print(pair)
print()

# Deleting item from dictionary by key: __delitem__()

del (soccerTeam["Avellino"])
print(soccerTeam)
print(anotherSoccerTeam)

# check if a pair is contained into dictionary
print()
if "Avellino" in anotherSoccerTeam:
    print(f"Avellino appartiene al team anotherSoccerTeam")
else:
    print(f"Avellino non appartiene al team anotherSoccerTeam")

if "Avellino" in soccerTeam:
    print(f"Avellino appartiene al team soccerTeam")
else:
    print(f"Avellino non appartiene al team soccerTeam")
