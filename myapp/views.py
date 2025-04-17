from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Memorial

# Create your views here.
def index(request):
    return HttpResponse('Tuko Ndakas!')

def memorials(request):
    memorials = Memorial.objects.all()
    return render (request, 'memorials/memorials.html', {'memorials':memorials})

def memorial_detail(request, id):
    memorial = get_object_or_404(Memorial, id=id)
    context = {
        'memorial': memorial,
        'profile_image_url': memorial.profile.url if memorial.profile else None,
        'images': memorial.images.all()  # Access related MemorialImage objects
    }
    return render(request, 'memorials/detail.html', context)