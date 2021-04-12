from django.urls import path, register_converter
from app.views import file_list, file_content
from datetime import datetime


class Converter:
    regex = '[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}'
    format = '%Y-%m-%d'

    def to_python(self, value: str) -> datetime:
        return datetime.strptime(value, self.format)

    def to_url(self, value: datetime) -> str:
        return value.strftime(self.format)


register_converter(Converter, 'dt')


urlpatterns = [
    path('', file_list, name='file_list'),
    path('<dt:date>/', file_list, name='file_list'),
    path('file/<name>/', file_content, name='file_content')
]
