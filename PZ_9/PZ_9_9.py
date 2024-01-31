# Дана строка '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15', отражающая средние температуры по месяцам в году.
# Преобразовать информацию из строки в словарь, с использованием функции найти среднюю и минимальные температуры,
# результаты вывести на экран.

def convert_string_to_dict(temp_string):
    temp_list = temp_string.split()
    months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
              'Декабрь']

    temp_dict = {}
    for i in range(12):
        month = months[i]
        temp_dict[month] = int(temp_list[i + 1])

    return temp_dict


def find_average_temperature(temp_dict):
    average_temp = sum(temp_dict.values()) / len(temp_dict)
    return average_temp


def find_min_temperature(temp_dict):
    min_temp = min(temp_dict.values())
    return min_temp


temp_string = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'

temperature_dict = convert_string_to_dict(temp_string)

average_temp = find_average_temperature(temperature_dict)

min_temp = find_min_temperature(temperature_dict)

print(f"Средняя температура: {average_temp},\nМинимальная температура: {min_temp}")
