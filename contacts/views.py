from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail

def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check  aif  user has made inquiry already
        if request.user.is_authenticated:
            user_id == request.user.id
            has_contacted =  Contact.objects.all().filter(listing_id = listing_id, user_id = user_id)
            if has_contacted:
                messages.error(request, 'You have  already applied for this lot, please wait realtor to contact you')
                return redirect('/listings/'+listing_id)


        contact = Contact(listing=listing, listing_id = listing_id, name = name, email=email, phone=phone,
        message=message, user_id = user_id)
        contact.save()

        # Send mail
        send_mail(
            "property listing inquiry" + listing,
            'There has bin an inquiry ' + listing_id + listing + '. Sign intoadmin area for more info',
            'some@email.com',
            [realtor_email, 'tech@email.ru'],
            fail_silently = True
        )


        messages.success(request, "You have successefully submitted the request, realtor will contact you soon")

        return redirect('/listings/'+listing_id)