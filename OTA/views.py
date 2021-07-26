from django.shortcuts import render
from .models import Oven, Temp
from django.http import Http404, HttpResponse
import datetime as dt

# Create your views here.
def index(request):
     oven_data = Oven.objects.all()
     temp_data = Temp.objects

     context = {'ovens': oven_data, 'temps': temp_data}
     return render(request, 'index.html', context)

def temps(req, oven_id):
     try:
          temp = Temp.objects.filter(oven = oven_id).order_by('date', 'time')
          
          dates = [i.date for i in temp]
          times = [i.time for i in temp]

          x = []

          for d, t in zip(dates, times):
               x.append(str(dt.datetime.combine(d, t)))

          
          y = [i.temperature for i in temp]
     
          print(x)
          context = {
               'temp': temp,
               'oven_id': oven_id,
               'x': x,
               'y': y,
          }
     except Temp.DoesNotExist:
        raise Http404("Temp Data does not exist")
     
     return render(req, 'temps.html', context)