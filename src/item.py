import random


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use_item(self):
        if self.name.lower() == 'dice':
            print(f'dice 1: {random.randint(1, 6)}')
            print(f'dice 2: {random.randint(1, 6)}')
        if self.name.lower() == 'guitar':
            print(f'You start playing some really bad music and get a headache')
        if self.name.lower() == 'sword':
            print(f'You swipe the sword in the air, that\'s about it')
        if self.name.lower() == 'key':
            print('You try turning the key in the air and as expected nothing happens')
