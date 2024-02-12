
class Contact():
    '''Объект записи в телефонной книге.'''

    def __init__(self, last_name, first_name, patronymic, organization,
                 work_phone, mobile_phone) -> None:

        self.last_name: str = last_name
        self.first_name: str = first_name
        self.patronymic: str = patronymic
        self.organization: str = organization
        self.work_phone: str = work_phone
        self.mobile_phone: str = mobile_phone

    def __str__(self) -> str:
        '''Строковое представление экземпляра контакта.'''

        return (
            f'{self.last_name} / {self.first_name} / {self.patronymic} / '
            f'{self.organization} / {self.work_phone} / '
            f'{self.mobile_phone}\n'
        )
