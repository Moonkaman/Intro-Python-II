import random


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use_item(self):
        if self.name.lower() == 'dice':
            print(f'dice 1: {random.randint(1, 6)}')
            print(f'dice 2: {random.randint(1, 6)}')
