from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Photo,Category,Location

# Create your views here.
def photos_today(request):
    date = dt.date.today()
    photos=Photo.objects.all()
    return render(request, 'all-art/today-photos.html', {"photos": photos})

def past_days_photos(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_of_day)

    return render(request, 'all-art/past-photos.html', {"date": date})
