def input_():
    var = int(input('Введите желаемое действие: 1 - Просмотреть БД, 2 - Внести нового ученика, 3 - Удалить ученика из БД,\
    4 - Перевести учеников в следующий учебный год'))

    return var


def input_del():
    d = input('Введите фамилию: ')

    return d


def get_last_name():
    return input('ФИО ученика:')


def get_class():
    return input('Класс:')


def get_liter():
    return input('Литера:')


def get_teacher():
    return input('Классный руководитель:')


def get_address():
    return input('Адрес проживания:')


def get_parent():
    return input('Родитель:')


def get_phone_parent():
    return input('Телефон родителя:')