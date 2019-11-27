from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    # listings = Listing.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    # if you get an error : class 'Listing' has no 'Objects' member
    # ignore it as it is pylint error, to fix it:
    # https://stackoverflow.com/questions/45135263/class-has-no-objects-member

    paginator = Paginator(listings, 6)  # Show 6 listings per page
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    return render(request, 'listings/listing.html', {'listing_id': listing_id})


def search(request):
    return render(request, 'listings/search.html')
