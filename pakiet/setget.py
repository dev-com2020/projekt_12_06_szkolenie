class UserAccount:
    def __init__(self, name, password):
        self.name = name
        self._password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password


    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return f'User: {self.name}, password: {self._password}'


o = UserAccount('Jan', '1234')
print(o.password)
print(o)