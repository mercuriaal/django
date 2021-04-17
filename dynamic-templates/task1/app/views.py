from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'

    with open('inflation_russia.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        data = [row for row in reader]

    title = data.pop(0)

    new_data = []
    for row in data:
        values = []
        for str_value in row[1:13]:
            if str_value != '':
                fl_value = float(str_value)
                values.append(fl_value)
            else:
                values.append(str_value)

        new_row = dict(year=row[0], months=values, summary=row[-1])
        new_data.append(new_row)

    context = {
        'titles': title,
        'data': new_data
    }

    return render(request, template_name, context)
