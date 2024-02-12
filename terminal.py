from models import Contact
from phonebook import PhoneBook
from utils import COMMANDS, RU_FIELDS


class Terminal():
    '''Терминал с интерфейсом.'''

    def __init__(self) -> None:

        self.commands = COMMANDS
        self.phonebook: PhoneBook = PhoneBook()

    def all_commands(self) -> None:
        '''Вывод списка доступных команд.'''

        for id, command in self.commands.items():
            print(f'{id}. {command[1]}')
        print()

    def create_contact(self):
        '''Добавить контакт.'''

        content = []
        print()
        for field in RU_FIELDS.values():
            input_text = input(f'Заполните поле {field}: ')
            content.append(input_text)
        try:
            contact = Contact(*content)
        except ValueError as e:
            print()
            print(e)
            return
        self.phonebook.post_contact(contact)
        print('Контакт добавлен\n')

    def read_page(self) -> None:
        '''Вывести страницу телефонной книги.'''

        count_contacts = self.phonebook.count_contacts()
        if count_contacts % self.phonebook.page_size:
            count_pages = count_contacts // self.phonebook.page_size + 1
        else:
            count_pages = count_contacts // self.phonebook.page_size

        print(f'\nКоличество контактов: {count_contacts}')
        print(f'Размер страницы: {self.phonebook.page_size}')
        print(f'Страниц в телефонной книге: {count_pages}\n')
        num_page = input('Введите номер страницы: ')
        print()

        try:
            num_page = int(num_page)
        except ValueError:
            print('Неверный формат - введите целое число\n')
            return

        if num_page > count_pages or num_page < 1:
            print('Такой страницы не существует\n')
            return
        for contact in self.phonebook.get_page(num_page):
            print(contact)

    def edit_contact(self) -> None:
        '''Редактировать контакт.'''

        num = input('\nВведите id контакта для редактирования: ')
        print()

        try:
            num = int(num)
        except ValueError:
            print('Некорректный формат id контакта. Только целое число\n')
            return
        try:
            contact = self.phonebook.get_contact(num)
        except ValueError as e:
            print(e)
            return

        contact = [field.strip() for field in str(contact).split(' / ')]
        new_contact = []

        for i in range(6):
            print(f'\nЗначение поля {list(RU_FIELDS.values())[i]} сейчас: {contact[i]}')
            input_text = input(
                'Введите новое значение или пропустите, оставив пустое значение: '
            )
            if input_text == '':
                new_contact.append(contact[i])
            else:
                new_contact.append(input_text)

        new_contact = Contact(*new_contact)
        self.phonebook.patch_contact(new_contact, num)
        print('\nКонтакт изменен.')

    def search_contact(self) -> None:
        '''Поиск контакта.'''

        print('Вводите через знак ' + '/' + ' без пробелов', end='')
        print(', если параметров несколько.')

        fields = input('\nВведите данные одной строкой: ').split('/')
        print()
        try:
            search_result = self.phonebook.search_contact(fields)
        except ValueError as e:
            print(e)
            return
        if len(search_result) == 0:
            print('Результат завершен. Ничего не найдено.\n')
            return
        print(f'Найдено {len(search_result)} совпадений:', end='\n')

        for contact in search_result:
            print(contact)

    def command_detect(self, command_key: str) -> None:
        '''Обработка и вызов команды.'''

        command = getattr(self, self.commands[command_key][0])
        command()

    def stop(self) -> None:
        '''Завершить работу.'''

        print('\nТелефонная книга завершает работу')
        exit()

    def run(self) -> None:
        '''Запустить интерфейс.'''

        print('Телефонная книга запущена\n')

        while True:
            print('\nДоступные команды:\n')
            self.all_commands()
            command = input('Введите id команды: ')
            if command not in self.commands:
                print('\nТакой команды не существует')
                continue
            self.command_detect(command)
