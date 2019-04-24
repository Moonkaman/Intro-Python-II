# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f'{self.name}: {self.description}'

    def show_items(self):
        if len(self.items) == 0:
            print('There are no items in this room.')
        else:
            print(f'\nItems in {self.name}:')
            for item in self.items:
                print(f'> {item.name}: {item.description}')
