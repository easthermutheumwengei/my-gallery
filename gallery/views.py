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
    return render(request, 'gallery/home.html',context)

def gallery(request):
    title= 'Gallery'
    images = Image.display_all_image_items()
    locations= Location.display_all_image_locations()

    context = {
        "title": title,
        "images":images,
        "locations":locations
    }

    return render(request, 'gallery/gallery.html',context)

class LocationView(ListView):
    model= Location
    template_name= 'gallery/gallery.html'

class galleryView(ListView):
        model = Image
        template_name = 'gallery/gallery.html'

class detailsView(DetailView):
            model = Image
            template_name = 'gallery/details.html'

def image_location(request, location_name):
                images = Image.filter_by_location(location_name)
                # print(images)
                context = {
                    "title": location_name,
                    "header": location_name,
                    'location_images': images

                }
                return render(request, 'gallery/location.html', context)

def image_category(request, category):
                images = Image.filter_by_category(category)
                # print(images)

                context = {
                    "title": category,
                    "header": category,
                    'category_images': images

                }
                return render(request, 'gallery/category.html', context)

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_category = request.GET.get("category")

        searched_category_images = Image.search_by_category(search_category)

        message = f"{search_category}"

        return render(request, 'gallery/search.html',{"message":message,"category_images": searched_category_images})

    else:
        message = "No such word"
        return render(request, 'gallery/search.html',{"message":message})