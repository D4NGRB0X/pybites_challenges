def get_profile(**kwargs):
    for arg in kwargs:
        if arg not in ['name', 'profession']:
            raise TypeError

    name = kwargs['name'] if 'name' in kwargs.keys() else 'julian'
    profession = kwargs['profession'] if 'profession' in kwargs.keys() else 'programmer'
    return f'{name} is a {profession}'
