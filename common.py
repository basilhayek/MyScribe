import random

def choose_from_list_as_str(input_list, number = 3, join_text = 'or'):
    if number > len(input_list):
        number = len(input_list)
    random_items = random.sample(input_list, number)

    if number > 1:
        all_but_last = ', '.join(random_items[:-1])
        last = random_items[-1]
        list_str = ' {} '.format(join_text).join([all_but_last, last])
    else:
        list_str = random_items[0]

    return list_str