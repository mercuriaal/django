import time
from datetime import datetime
from django import template


register = template.Library()


@register.filter
def format_date(value):

    time_diff = time.time() - value
    if time_diff < 600:
        return 'Меньше 10 минут назад'
    elif 600 <= time_diff < 86400:
        hours = int(time_diff/3600)
        return f'Опубликовано {hours} часов назад'
    elif time_diff >= 86400:
        return datetime.fromtimestamp(value)


@register.filter()
def format_votes(value):

    if value:
        if value < -5:
            return 'Всё плохо'
        elif -5 <= value <= 5:
            return 'Нейтрально'
        elif value > 5:
            return 'Хорошо'


@register.filter
def format_num_comments(value):

    if value == 0:
        return 'Оставьте комментарий'
    elif 0 < value <= 50:
        return value
    elif value > 50:
        return '50+'


@register.filter()
def format_text(value, count):

    listed = value.split(' ')
    front = ' '.join(listed[0:count])
    back = ' '.join(listed[-count:])
    return f'{front} ... {back}'



