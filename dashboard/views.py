from django.shortcuts import render, redirect
import urllib
from .models import CountryData ,City ,County
from .forms import CountryDataFrom
from django.http import JsonResponse 

# Create your views here.


def index(request):
    data = CountryData.objects.all()
    if request.method == 'POST':
        form = CountryDataFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CountryDataFrom()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'dashboard/index.html', context)

def taiwan(request):
    citys = City.objects.all()
    counties = County.objects.all()
    city = citys.get(id=8)
    county = '全區'
    return render(request,'dashboard/taiwan.html',{'citys':citys,'counties':counties,'cityName':city,'countyName':county})


def ajax_refresh_county(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.POST['action'] == 'refresh_county':
            updatedData = urllib.parse.parse_qs(request.body.decode('utf-8'))
            city_id = updatedData['city_id'][0]
            counties = County.objects.filter(city=City.objects.get(id=city_id))
            # countylist = serializers.serialize('json', list(counties))
            data=[]
            for county in counties:
                item = {
                    'id':county.id,
                    'county':county.name,
                }
                data.append(item)
            print(data)
            return JsonResponse({'data':data})

def first(request):
    return render(request, 'dashboard/first.html', locals())