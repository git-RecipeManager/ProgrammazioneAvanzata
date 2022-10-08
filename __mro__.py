class X:
    var1 = "varX"
    var2 = 2
    var3 = 4.5
    var4 = True


class T:
    var5 = "varT"
    var6 = 2
    var7 = 4.5
    var8 = True


class Z(T):
    var9 = "varZ"
    var10 = 2
    var11 = 4.5
    var12 = True
    sec1 = []
    sec2 = ()
    map1 = {}

    def __init__(self):
        self.a = 5
        self.b = 10


class ClasseB(X, Z):
    var13 = 2
    var14 = False

    def conta_var_classe(self, t: object, n: int) -> int:
        """
        Counts the number of occurrences of class variables encountered while traversing
        the class hierarchy as listed in the __mro__ attribute.
        :param t: the type to look for in the hierarchy
        :param n: search boundary
        :return:the number of occurrences of the type t
        """

        break2 = False
        count = 0

        # We go through the tuple that contains the classes that make up the
        # order of resolution of the methods.
        for index, cls in enumerate(ClasseB.__mro__):

            for attribute, value in cls.__dict__.items():

                # the variable "selected" belongs to the global scope
                # if isinstance(value, choose_type[selected - 1]): # not appropriate
                if type(value) == choose_type[selected]:
                    count += 1
                    print(f" I'm in {cls.__name__} and the variable is -> {attribute} : {value}")

                if n < len(ClasseB.__mro__) and n == index:
                    break2 = True
                    break

            if break2:
                break

        return count


# Driver section
choose_type = (str, int, bool, float, list, tuple, dict)


def prompt():
    global layers
    if layers > 5: layers = 5
    template = "for count the class's variables of"
    print(f"type-in  <0> {template} {str}  ")
    print(f"type-in  <1> {template} {int}  ")
    print(f"type-in  <2> {template} {bool}  ")
    print(f"type-in  <3> {template} {float}  ")
    print(f"type-in  <4> {template} {list} ")
    print(f"type-in  <5> {template} {tuple}  ")
    print(f"type-in  <6> {template} {dict}  ")
    selected = int(input("Please make a choose: "))
    return selected


layers = 100
selected = prompt()
b = ClasseB()

c = b.conta_var_classe(choose_type[selected], layers)
print(f"There are {c} class's variables of {choose_type[selected]} type in the firsts {layers} layers of the "
      f"hierarchy")
