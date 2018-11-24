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


class ProfileEngaged(VerboseException):
    code = 102
    verbose_msg = "Аккаунт с указанным номером телефона уже существует"


class FirstNameNotEntered(VerboseException):
    code = 103
    verbose_msg = "Не введено имя"


class LastNameNotEntered(VerboseException):
    code = 104
    verbose_msg = "Не введена фамилия"


class CodesDoNotMatch(VerboseException):
    code = 105
    verbose_msg = "Коды не совпадают"


class NoUdid(VerboseException):
    code = 106
    verbose_msg = "Нет udid"


class UdidsDoNotMatch(VerboseException):
    code = 107
    verbose_msg = "udids не совпадают"

