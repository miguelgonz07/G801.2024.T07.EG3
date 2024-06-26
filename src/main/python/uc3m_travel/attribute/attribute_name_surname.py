from .attribute import Attribute


class NameSurname(Attribute):

    def __init__(self, name_surname):
        super().__init__()
        self._attr_pattern = r'^(?=^.{10,50}$)([a-zA-Z]+(\s[a-zA-Z]+)+)$'
        self._error_message = "Invalid name format"
        self._attr_value = self._validate(name_surname)
