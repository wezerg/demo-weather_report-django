from django.shortcuts import render
from datetime import datetime
import pytz
from django.http import JsonResponse


def get_date(tz):
    x = datetime.now(tz)
    return x.strftime('%Y-%m-%d')


def get_time(tz):
    x = datetime.now(tz)
    return x.strftime('%H:%M:%S')

def index(request):

    timeZ_Kl = pytz.timezone('Asia/Kolkata')
    timeZ_Ny = pytz.timezone('America/New_York')
    timeZ_Ma = pytz.timezone('Africa/Maseru')
    timeZ_Ce = pytz.timezone('US/Central')
    timeZ_At = pytz.timezone('Europe/Athens')

    context = {
        'tabDates': [
                                    {
                                        "localisation": "Asia/Kolkata",
                                        "date":get_date(timeZ_Kl),
                                        "heure":get_time(timeZ_Kl),
                                    },{
                                        "localisation": "America/New_York",
                                        "date":get_date(timeZ_Ny),
                                        "heure":get_time(timeZ_Ny)
                                    },{
                                        "localisation": "Africa/Maseru",
                                        "date":get_date(timeZ_Ma),
                                        "heure":get_time(timeZ_Ma),
                                    },{
                                        "localisation": "US/Central",
                                        "date":get_date(timeZ_Ce),
                                        "heure":get_time(timeZ_Ce),
                                    },{
                                        "localisation": "Europe/Athens",
                                        "date":get_date(timeZ_At),
                                        "heure":get_time(timeZ_At)
                                    }
                                 ]
    }
    return render(request, 'timer/index.html', context)

def test1(request):
    print(request)
    return JsonResponse({"message":"Hello World"})