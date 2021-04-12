import datetime
import os

from django.shortcuts import render
from django.conf import settings


def file_list(request, date=None):

    template_name = 'index.html'
    files_list = os.listdir(settings.FILES_PATH)

    files_info = []
    for file in files_list:
        file_path = os.path.join(settings.FILES_PATH, file)
        data = dict(name=file,
                    ctime=datetime.datetime.fromtimestamp(os.stat(file_path).st_ctime),
                    mtime=datetime.datetime.fromtimestamp(os.stat(file_path).st_mtime))
        files_info.append(data)

    if date is not None:
        result = [file for file in files_info if file['ctime'].date() == date.date()]
    else:
        result = files_info

    context = {
        'files': result,
        'date': date
    }

    return render(request, template_name, context)


def file_content(request, name):

    content = ''
    if name in os.listdir(settings.FILES_PATH):
        with open(os.path.join(settings.FILES_PATH, name)) as f:
            for line in f.readlines():
                content += line

    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )

