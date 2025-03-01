def filter_by_state(list_of_value):
    new_list = []
    for i in list_of_value:
        for k,v in i.items():
            if v == 'EXECUTED':
                new_list += i
            else:
                continue
    return new_list


from datetime import datetime
def sort_by_date(data, descending=True):
    return sorted(data, key=lambda x: datetime.fromisoformat(x['date']), reverse=descending)
