from typing import Any
# решение коллизии через создание списка элементов с полученным одинаковым индексом
class MyDict:
    def __init__(self) -> None:
        self.size: int = 8
        self.mydict: list = [None] * self.size


    def gethash(self, key) -> int:
        return hash(key) % self.size


    def __setitem__(self, key, value: Any) -> None:
        key_hash: int = self.gethash(key)
        if self.mydict[key_hash] is None:
            self.mydict[key_hash] = (key, value)


        else:
            if type(self.mydict[key_hash]) is not list:
                item: tuple = self.mydict[key_hash]
                self.mydict[key_hash] = [item, (key, value)]

            else:
                self.mydict[key_hash].append((key, value))


    def __getitem__(self, key) -> Any | None:
        key_hash: int = self.gethash(key)
        if type(self.mydict[key_hash]) is not list and self.mydict[key_hash] is not None:
            if self.mydict[key_hash][0] == key:
                return self.mydict[key_hash][1]

        elif type(self.mydict[key_hash]) is list:
            for i in self.mydict[key_hash]:
                if i[0] == key:
                    return i[1]

        else:
            return None


    def __delitem__(self, key) -> None:
        key_hash: int = self.gethash(key)
        if type(self.mydict[key_hash]) is not list and self.mydict[key_hash] is not None:
            if self.mydict[key_hash][0] == key:
                self.mydict[key_hash] = None

        elif type(self.mydict[key_hash]) is list:
            for i in self.mydict[key_hash]:
                if i[0] == key:
                    self.mydict[key_hash].remove(i)
                    if len(self.mydict[key_hash]) == 0:
                        self.mydict[key_hash] = None
                    break


    def keys(self) -> list:
        keys = []
        for i in self.mydict:
            if type(i) is not list and i is not None:
                keys.append(i[0])

            elif type(i) is list:
                for j in i:
                    keys.append(j[0])
        return keys


    def values(self) -> list:
        values = []
        for i in self.mydict:
            if type(i) is not list and i is not None:
                values.append(i[1])

            elif type(i) is list:
                for j in i:
                    values.append(j[1])
        return values


    def items(self) -> list[tuple]:
        all_items = []
        for i in self.mydict:
            if type(i) is not list and i is not None:
                all_items.append(i)

            elif type(i) is list:
                for j in i:
                    all_items.append(j)
        return all_items


    def __str__(self):
        result = ''
        all_items = self.items()
        for i in range(len(all_items) - 1):
            result += f'{all_items[i][0]}: {all_items[i][1]}, '
        last = f'{all_items[-1][0]}: {all_items[-1][1]}'
        result += last
        return '{' + result + '}'


    def __contains__(self, key):
        keys = self.keys()
        return key in keys


my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
my_dict['eye_color'] = 'blue'
my_dict['height'] = 170
my_dict['weight'] = 60
my_dict['hair_color'] = 'blond'
my_dict['pet'] = 'cat'
my_dict['university'] = 'FEFU'
my_dict['city'] = 'Vdk'
print(my_dict['name'])
print('city' in my_dict)
del my_dict['age']
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict)
