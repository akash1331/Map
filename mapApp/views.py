from django.http import HttpResponse
from django.shortcuts import render,redirect
import folium
import geocoder
from .models import *
from .forms import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        form=searchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=searchForm()
    address = search.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('Location not found. Enter valid address')
    m = folium.Map(location=[19,-12],zoom_start=2) #create map obj
    folium.Marker([lat,lng],tooltip='Click for more',popup=country).add_to(m)
    m = m._repr_html_() #html representation of map obj
    context = {
        'form':form,
        'm':m,
    }

    return render(request,'index.html',context)