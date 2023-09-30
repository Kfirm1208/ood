class Monkey:
    def __init__(self, name, strength, intelligence, agility, id):
        self.name = name
        self.str = strength
        self.int = intelligence
        self.agi = agility
        self.id = id
        
    def __repr__(self) -> str:
        return f'{self.id}-{self.name}'
    
    def __lt__(self, other):
        if self.str == other.str:
            if self.int == other.int:
                if self.agi == other.agi:
                    return self.id < other.id
                return self.agi < other.agi
            return self.int < other.int
        return self.str < other.str
    
    def __gt__(self, other):
        if self.str == other.str:
            if self.int == other.int:
                if self.agi == other.agi:
                    return self.id > other.id
                return self.agi > other.agi
            return self.int > other.int
        return self.str > other.str
    
    def __eq__(self, other):
        return self.str == other.str and self.int == other.int and self.agi == other.agi and self.id == other.id
    
    def __le__(self, other):
        return self < other or self == other
    
    def __ge__(self, other):
        return self > other or self == other

    def __ne__(self, other):
        return not self == other 

def sort_monkey(monkeys, order, attr, index):
    if len(monkeys) == 1:
        return monkeys
    mid = len(monkeys) // 2
    left = sort_monkey(monkeys[:mid], order, attr, index)
    right = sort_monkey(monkeys[mid:], order, attr, index)
    return merge(left, right, order, attr, index)

def merge(left, right, order, attr, index):
    result = []
    while len(left) > 0 and len(right) > 0:
        if order == 'A':
            if getattr(left[0], attr[index]) <= getattr(right[0], attr[index]):
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
        else:
            if getattr(left[0], attr[index]) >= getattr(right[0], attr[index]):
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result

inp = input("Enter Input: ").split('/')
order = inp[0]
attribute = inp[1].split(',')
monkeys = inp[2].split(',')
monkeys = [Monkey(monkey.split()[0], int(monkey.split()[1]), int(monkey.split()[2]), int(monkey.split()[3]), i) for i, monkey in enumerate(monkeys)]
if attribute != ['']:
    for i in range(len(attribute)-1, -1, -1):
        monkeys = sort_monkey(monkeys, order, attribute, i)
print(monkeys)