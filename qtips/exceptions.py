class VerboseException(Exception):
    code = 0
    verbose_msg = "Сообщение отсутствует"

    def get_verbose(self):
        return self.verbose_msg.capitalize()

    def get_code(self):
        return self.code


class CountryCodeNotEntered(VerboseException):
    code = 100
    verbose_msg = "Не введен код страны"


class NumberNotEntered(VerboseException):
    code = 100
    verbose_msg = "Не введен номер"


class FirstNameNotEntered(VerboseException):
    code = 102
    verbose_msg = "Не введено имя"


class LastNameNotEntered(VerboseException):
    code = 103
    verbose_msg = "Не введена фамилия"
