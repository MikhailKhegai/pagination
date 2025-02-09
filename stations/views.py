import csv

from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):

    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        station = []
        for row in reader:
            station.append(row)
        bus_stations = Paginator(station, 10)
        page_number = int(request.GET.get('page', 1))

        context = {
            'bus_stations': bus_stations.get_page(page_number),
            'page': bus_stations.get_page(page_number),
        }
        return render(request, 'stations/index.html', context)
