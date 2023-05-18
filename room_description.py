# Room description class
class RoomDescription:
    """
    Constructor:

    :param id - ID_Room_Description
    :param room_type - Room_Type_Name
    :param capacity - Capacity
    :param balcony - Balcony
    :param price - Price_Per_Day
    """

    def __init__(self, id, capacity, balcony, price, room_type):
        self.id = id
        self.room_type = room_type
        self.capacity = capacity
        self.balcony = balcony
        self.price = price