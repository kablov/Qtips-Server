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
    code = 101
    verbose_msg = "Не введен номер"


class PhoneEngaged(VerboseException):
    code = 102
    verbose_msg = "Аккаунт с таким номером телефона уже существует"


class FirstNameNotEntered(VerboseException):
    code = 103
    verbose_msg = "Не введено имя"


class LastNameNotEntered(VerboseException):
    code = 104
    verbose_msg = "Не введена фамилия"


class CodesDoNotMatch(VerboseException):
    code = 105
    verbose_msg = "Введенный код не совпадает с отправленным в смс"


class AccessDenied(VerboseException):
    code = 106
    verbose_msg = "Токен не совпадает"
