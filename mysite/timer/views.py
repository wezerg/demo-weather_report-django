from django.shortcuts import render
from datetime import datetime
import pytz
from django.http import JsonResponse

class GetTime:
    def __init__(self):
        pass

    def get_date(self, country):
        x = datetime.now(country)
        return x.strftime('%d/%m/%Y')

    def get_time(self, country):
        x = datetime.now(country)
        return x.strftime('%H:%M:%S')
    
    def get_all(self):
        time_kl = pytz.timezone('Asia/Kolkata')
        time_ny = pytz.timezone('America/New_York')
        time_ma = pytz.timezone('Africa/Maseru')
        time_ce = pytz.timezone('US/Central')
        time_at = pytz.timezone('Europe/Athens')
        tab = [
            {
                "localisation": "Asia/Kolkata",
                "date": self.get_date(time_kl),
                "heure": self.get_time(time_kl),
            }, {
                "localisation": "America/New_York",
                "date": self.get_date(time_ny),
                "heure": self.get_time(time_ny)
            }, {
                "localisation": "Africa/Maseru",
                "date": self.get_date(time_ma),
                "heure": self.get_time(time_ma),
            }, {
                "localisation": "US/Central",
                "date": self.get_date(time_ce),
                "heure": self.get_time(time_ce),
            }, {
                "localisation": "Europe/Athens",
                "date": self.get_date(time_at),
                "heure": self.get_time(time_at)
            }
        ]
        return tab

def index(request):
    gt = GetTime()
    context = {
        'tabDates': gt.get_all()
    }
    return render(request, 'timer/index.html', context)

def refreshTime(request):
    gt = GetTime()
    tab_dates = gt.get_all()
    return JsonResponse({"message": tab_dates })