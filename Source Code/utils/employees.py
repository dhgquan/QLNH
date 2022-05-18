from .other import dict_from_entries

keys = ('id', 'name', 'last_name', 'position')


def get_employees():

    employees = []

    file = open('employees.csv')

    for line in file:
        id, name, last_name, position = line.split(',')

        employees.append(dict_from_entries(keys, (
            int(id),
            name,
            last_name,
            position.rstrip()
        )))

    file.close()
    return tuple(employees)
