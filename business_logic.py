import view


def read_file(path='data_file.csv'):
    import csv
    import view

    view.view()

    with open(path, 'r') as file:
        print(file.read())

    return path


def write_file(path='data_file.csv'):
    import UI

    last_name = UI.get_last_name()
    class_ = UI.get_class()
    liter = UI.get_liter()
    teacher = UI.get_teacher()
    address = UI.get_address()
    parent = UI.get_parent()
    phone = UI.get_phone_parent()

    with open(path, 'a') as file:
        file.write('{},{},{},{},{},{},{}\n'
                   .format(last_name, class_, liter, teacher, address, parent, phone))

    return path


def delete_row(path='data_file.csv'):
    import csv
    import UI
    import os

    d = UI.input_del()

    input_ = open(path, 'r')
    output = open('data_file1.csv', 'w')
    writer = csv.writer(output)
    for row in csv.reader(input_):
        if row[0] != d:
            writer.writerow(row)

    input_.close()
    output.close()
    os.remove('data_file.csv')
    os.rename('data_file1.csv', 'data_file.csv')

    return path


def next_class(path='data_file.csv'):
    import csv
    import os

    input_ = open(path, 'r')
    output = open('data_file2.csv', 'w')
    writer = csv.writer(output)
    for row in csv.reader(input_):
        if row != '\n':
            row[1] = str(int(row[1]) + 1)
        writer.writerow(row)

    input_.close()
    output.close()
    os.remove('data_file.csv')
    os.rename('data_file2.csv', 'data_file.csv')

    return path
