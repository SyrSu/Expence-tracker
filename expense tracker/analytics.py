def filtered_by_date_range(expenses, start_date, end_date):
    e_list = []
    for e in expenses:
        if start_date<=e.date<=end_date:
            e_list.append(e)
    return e_list

def sorted_by_amount(expenses, descending=True):

    def mykey(e):
        return e.amount

    return sorted(expenses, key=mykey,reverse=descending)

def filter_by_category(expenses, category):
    filtered = []
    for e in expenses:
        if e.category == category:
            filtered.append(e)
    return filtered

def total_by_category(expenses):
    new_dict = {}
    for e in expenses:
        new_dict[e.category] = new_dict.get(e.category, 0) + e.amount
    return new_dict

def total_expenses(expenses):
    summary = 0
    for e in expenses:
        summary += e.amount
    return summary

def top_n_by_amount(expenses, n=3):
    sorted_list = sorted_by_amount(expenses, descending=True)
    return sorted_list[:n]

def report(expenses, start_date, end_date, top_n = 3):
    filtered = filtered_by_date_range(expenses, start_date, end_date)
    new_dict = {}
    new_dict['filtered'] = filtered
    new_dict['count'] = len(filtered)
    new_dict['total'] = total_expenses(filtered)
    new_dict['by_category'] = total_by_category(filtered)
    new_dict['top'] = top_n_by_amount(filtered, top_n)
    return new_dict