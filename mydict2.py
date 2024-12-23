from typing import Any
# решение коллизии через поиск свободного индекса
class MyDict:
    def __init__(self):
        self.size: int = 8
        self.mydict: list = [None] * self.size


    def gethash(self, key) -> int:
        return hash(key) % self.size


    def free_index(self) -> int:
        for i in range(self.size):
            if self.mydict[i] is None:
                return i


    def resize(self, to_do_key, to_do_value) -> None:
        old_dict = self.mydict
        self.size *= 2
        self.mydict = [None] * self.size
        for item in old_dict:
            key, value = item
            self.__setitem__(key, value)
        self.__setitem__(to_do_key, to_do_value)


    def search_index(self, key) -> int | None:
        for i in range(len(self.mydict)):
            if self.mydict[i] is not None and self.mydict[i][0] == key:
                return i


    def __setitem__(self, key, value: Any) -> None:
        key_hash: int = self.gethash(key)
        if self.mydict[key_hash] is None:
            self.mydict[key_hash] = (key, value)

        else:
            free_index = self.free_index()
            if free_index is not None:
                self.mydict[free_index] = (key, value)

            else:
                self.resize(key, value)


    def __getitem__(self, key) -> Any | None:
        key_hash: int = self.gethash(key)
        if self.mydict[key_hash] is not None and self.mydict[key_hash][0] == key:
            return self.mydict[key_hash][1]

        else:
            item_index: int = self.search_index(key)
            if item_index is not None:
                return self.mydict[item_index][1]
        return None


    def __delitem__(self, key) -> None:
        key_hash: int = self.gethash(key)
        if self.mydict[key_hash] is not None and self.mydict[key_hash][0] == key:
            self.mydict[key_hash] = None

        else:
            item_index: int = self.search_index(key)
            if item_index is not None:
                self.mydict[item_index] = None


    def keys(self) -> list:
        keys = []
        for i in self.mydict:
            if i is not None:
                keys.append(i[0])
        return keys


    def values(self) -> list:
        values = []
        for i in self.mydict:
            if i is not None:
                values.append(i[1])
        return values


    def items(self) -> list[tuple]:
        all_items = []
        for i in self.mydict:
            if i is not None:
                all_items.append(i)
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
print(my_dict)
print(my_dict['name'])
print(my_dict['university'])
my_dict['car'] = 'BMW'
print(my_dict['name'])
print('city' in my_dict)
del my_dict['age']
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())



