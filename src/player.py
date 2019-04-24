# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room, items=[]):
        self.current_room = current_room
        self.items = items

    def set_current_room(self, room):
        self.current_room = room

    def pickup_item(self, item):
        self.items.append(item)
        self.current_room.items.remove(item)

    def drop_item(self, item):
        self.items.remove(item)
        self.current_room.items.append(item)

    def show_inventory(self):
        print('Inventory:')
        if self.items:
            for item in self.items:
                print(f'> {item.name}: {item.description}')
        else:
            print('No items in your inventory yet')
