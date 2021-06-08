from django.shortcuts import render
from datetime import datetime
import pytz


def get_date(tz):
    x = datetime.now(tz)
    return x.strftime('%Y-%m-%d %H:%M:%S %Z %z')


def index(request):

    timeZ_Kl = pytz.timezone('Asia/Kolkata')
    timeZ_Ny = pytz.timezone('America/New_York')
    timeZ_Ma = pytz.timezone('Africa/Maseru')
    timeZ_Ce = pytz.timezone('US/Central')
    timeZ_At = pytz.timezone('Europe/Athens')

    context = {
        'tabDates': [
                                    {"date":get_date(timeZ_Kl)},
                                    {"date":get_date(timeZ_Ny)},
                                    {"date":get_date(timeZ_Ma)},
                                    {"date":get_date(timeZ_Ce)},
                                    {"date":get_date(timeZ_At)},
                                 ]
    }
    return render(request, 'timer/index.html', context)