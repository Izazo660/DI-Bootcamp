class Door:
    def __init__(self, is_opened=False):
        self.is_opened = is_opened

    def open_door(self):
        if not self.is_opened:
            self.is_opened = True
            print("The door is now open.")
        else:
            print("The door is already open.")

    def close_door(self):
        if self.is_opened:
            self.is_opened = False
            print("The door is now closed.")
        else:
            print("The door is already closed.")


class BlockedDoor(Door):    
    def open_door(self):
        raise Exception("Error : A blocked door cannot be opened.")

    def close_door(self):
        raise Exception("Error : A blocked door cannot be closed.")