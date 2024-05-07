from django.shortcuts import render
from django.http import JsonResponse
from .models import Trackers_Info
from django.core import serializers


# Create your views here.
def home(request):
    context={}
    return render(request, "home.html", context)

def trackers_info_list(request):
    trackers_info = Trackers_Info.objects.all()
    data = serializers.serialize('json', trackers_info)
    return JsonResponse(data, safe=False)

def trackers_info_by_id(request, trackers_info_id):
    # Filter the queryset based on the provided trackersInfoId
    trackers_info = Trackers_Info.objects.filter(trackersInfoId=trackers_info_id)
    
    # Serialize the filtered queryset to JSON
    data = serializers.serialize('json', trackers_info)
    
    # Return the JSON response
    return JsonResponse(data, safe=False)

