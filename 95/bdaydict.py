MSG = 'Hey {}, there are more people with your birthday!'
BIRTHDAYS = []


def check_shared_birthday(birthday):
    shared_birthday = False
    birthday_month_day = (birthday.month, birthday.day)

    if birthday_month_day in BIRTHDAYS:
        shared_birthday = True

    BIRTHDAYS.append(birthday_month_day)

    return shared_birthday


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __setitem__(self, name, birthday):
        super().__setitem__(name, birthday)
        if check_shared_birthday(birthday):  # you've created a specific version of any() built-in
            print(MSG.format(name))



