# Количество записей на странице
PAGE_SIZE = 5

# Путь до файла с базой данных (относительно основной папки)
FILE_PATH = 'base_contact.txt'

# Команды для терминала
COMMANDS = {
    '1': ('read_page', 'Показать телефонную книгу'),
    '2': ('create_contact', 'Добавить контакт'),
    '3': ('edit_contact', 'Редактировать контакт'),
    '4': ('search_contact', 'Найти контакт'),
    '5': ('stop', 'Выйти'),
}

# Поля контакта
RU_FIELDS = {
    'last_name': 'Фамилия',
    'first_name': 'Имя',
    'patronymic': 'Отчество',
    'organization': 'Организация',
    'work_phone': 'Рабочий телефон',
    'mobile_phone': 'Личный телефон',
}
