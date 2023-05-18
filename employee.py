# Employee class
class Employee:
    """
    Constructor:

    :param id - ID_Employee
    :param f - Last_Name
    :param i - First_Name
    :param o - Patronymic
    :param id_hotel - ID_Hotel
    :param login - Login
    :param password - Password
    """

    def __init__(self, id, f, i, o, id_hotel, login, password):
        self.id = id
        self.last_name = f
        self.first_name = i
        self.patronymic = o
        self.id_hotel = id_hotel
        self.login = login
        self.password = password

    def get_fio(self):
        return ' '.join([self.last_name, self.first_name, self.patronymic])
