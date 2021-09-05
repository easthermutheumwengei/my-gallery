from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def home(request):
    title ='Home'
    images = Image.display_all_image_items()
    locations= Location.display_all_image_locations()
    categories = Categories.display_all_image_Categories()
    context = {
        "title": title,
        "images":images,
        "locations":locations,
        "categories": categories
    }
    return render(request, 'gallery/index.html',context)