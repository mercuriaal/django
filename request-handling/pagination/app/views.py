import csv
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
from urllib.parse import urlencode


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, newline='', encoding='cp1251') as f:
        reader = csv.DictReader(f)
        all_stations = [row for row in reader]
    paginator = Paginator(all_stations, 10)
    current_page = request.GET.get('page', 1)
    stations = paginator.get_page(current_page)
    prev_page_url, next_page_url = None, None
    if stations.has_previous():
        prev_page_url = reverse('bus_stations') + '?' + urlencode({'page': stations.previous_page_number()})
    if stations.has_next():
        next_page_url = reverse('bus_stations') + '?' + urlencode({'page': stations.next_page_number()})
    return render(request, 'index.html', context={
        'bus_stations': stations,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

