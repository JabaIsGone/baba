def filter_by_state(list_of_value):
    new_list = []
    for i in list_of_value:
        for k,v in i.items():
            if v == 'EXECUTED':
                new_list += i
            else:
                continue
    return new_list

