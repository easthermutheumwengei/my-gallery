from .models import Location,Categories

def categories(request):
    categories = Categories.objects.all()
    return {'categories': categories}

def locations(request):
    locations = Location.objects.all()
    return {'locations': locations}
