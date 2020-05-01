from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choises import price_choices, state_choices, bedroom_choices

from .models import Listing


def index(request):
    listing = Listing.objects.order_by('-list_date').filter(is_published = True)

    paginator = Paginator(listing, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        "listings" : paged_listings
    }

    return render(request, "listings/listings.html", context)

def listing(request, listing_id):
    
    listing = get_object_or_404(Listing, pk = listing_id)

    context = {
        "listing":listing
    }

    return render(request, "listings/listing.html", context)

def search(request):
    get_queryset = Listing.objects.order_by('-list_date')
    #keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords :
            get_queryset = get_queryset.filter(description__icontains = keywords)

    #city
    if 'city' in request.GET:
        city = request.GET['city']
        if city :
            get_queryset = get_queryset.filter(city__iexact = city)

    #state
    if 'state' in request.GET:
        state = request.GET['state']
        if state :
            get_queryset = get_queryset.filter(state__iexact = state)

    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms :
            get_queryset = get_queryset.filter(bedrooms__lte = bedrooms)

    #price
    if 'price' in request.GET:
        price = request.GET['price']
        if price :
            get_queryset = get_queryset.filter(price__lte = price)

    context = {
    "price_choices":price_choices,
    "state_choices":state_choices,
    "bedroom_choices":bedroom_choices,
    'listings' : get_queryset,
    'values' : request.GET
    }

    return render(request, "listings/search.html", context)