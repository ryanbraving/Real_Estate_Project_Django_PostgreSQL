from django.shortcuts import render
from .models import Listing

# Create your views here.

def index(request):
    listings = Listing.objects.all()
    # if you get an error : class 'Listing' has no 'Objects' member
    # ignore it as it is pylint error, to fix it:
    # https://stackoverflow.com/questions/45135263/class-has-no-objects-member
    
    context = {
        'listings': listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    return render(request, 'listings/listing.html', {'listing_id': listing_id})

def search(request):
    return render(request, 'listings/search.html')