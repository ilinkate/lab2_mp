class OBJ:
    def __init__(self, name: str, sport: str, age: float, height: float, weight: float):
        self.name = name
        self.sport = sport
        self.age = age
        self.height = height
        self.weight = weight
# >

    def __gt__(self, other):
        if self.name > other.name:
            return True
        elif self.name < other.name:
            return False
        else:
            if self.sport > other.sport:
                return True
            elif self.sport < other.sport:
                return False
            else:
                if self.age > other.age:
                    return True
                else:
                    return False
# <

    def __lt__(self, other):
        if self.name < other.name:
            return True
        elif self.name > other.name:
            return False
        else:
            if self.sport < other.sport:
                return True
            elif self.sport > other.sport:
                return False
            else:
                if self.age < other.age:
                    return True
                else:
                    return False
# >=

    def __ge__(self, other):
        if self.name > other.name:
            return True
        elif self.name < other.name:
            return False
        else:
            if self.sport > other.sport:
                return True
            elif self.sport < other.sport:
                return False
            else:
                if self.age > other.age:
                    return True
                elif self.age < other.age:
                    return False
                else:
                    return True
# <=

    def __le__(self, other):
        if self.name < other.name:
            return True
        elif self.name > other.name:
            return False
        else:
            if self.sport < other.sport:
                return True
            elif self.sport > other.sport:
                return False
            else:
                if self.age < other.age:
                    return True
                elif self.age > other.age:
                    return False
                else:
                    return True