from models import Contact
from utils import FILE_PATH, PAGE_SIZE
from typing import List


class PhoneBook:
    '''Класс телефонной книги.'''

    def __init__(self):
        self.current_id: int = self.count_contacts() + 1
        self.page_size: int = PAGE_SIZE

    def count_contacts(self) -> int:
        '''Получить количество контактов в файле.'''
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            return len(file.readlines())

    def get_page(self, num_page: int) -> List[str]:
        '''Получить страницу контактов из файла.'''
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            start = ((num_page - 1) * self.page_size)
            finish = num_page * self.page_size
            # finish = num_page * self.page_size + 1
            data = file.readlines()
            page = []
            for line in range(start, finish):
                page.append(data[line])
            return page

    def get_contact(self, id: int) -> Contact:
        '''Получить контакт по id.'''
        if id >= self.current_id or id < 1:
            raise ValueError('Такого контакта не существует!')
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            data = file.readlines()[id-1]
            contact = [line.strip() for line in data.split(' / ')]
            object = Contact(
                last_name=contact[1],
                first_name=contact[2],
                patronymic=contact[3],
                organization=contact[4],
                work_phone=contact[5],
                mobile_phone=contact[6],
            )
            return object

    # Переделать строку для добавления
    def post_contact(self, contact: Contact) -> None:
        '''Добавление контакта.'''
        with open(FILE_PATH, 'a', encoding='utf-8') as file:
            file.write(str(self.current_id) + ' / ' + str(contact))
        self.current_id += 1

    def patch_contact(self, updated_contact: Contact, id: int) -> None:
        '''Изменить контакт по id.'''
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            data = file.readlines()
        data[id - 1] = str(id) + ' / ' + str(updated_contact)
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            file.writelines(data)

    def search_contact(self, query: List[str]) -> List[str]:
        '''Поиск контакта.'''
        if all(i == '' for i in query):
            raise ValueError('Вы ввели пустой запрос')
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            data = file.readlines()
            result = []
            for line in data:
                contact = line.strip()
                if all(
                    query[i] in contact.split(' / ') for i in range(len(query))
                ):
                    result.append(contact)
            return result
