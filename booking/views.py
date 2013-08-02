# -*- encoding: utf8 -*-

from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.conf import settings

from booking.models import SlotBooked, Queue
from booking.forms import BookingForm
from booking import backend

from room.models import Room

from userprofile.models import UserProfile

from paypal.standard.forms import PayPalPaymentsForm

@login_required
def status(request):
  
  try:
    userprofile = UserProfile.objects.get(pk=request.user)
  except UserProfile.DoesNotExist:
    return render(request, "booking/booking_status_empty_profile.html")
  
  try:
    queue = Queue.objects.get(user=request.user)
    count = Queue.objects.filter(dateAdded__lt=queue.dateAdded).count()
    return render(request, "booking/booking_status_queue_position.html", {
              "position": count
           })

  except Queue.DoesNotExist:
    try:    
      slotBooked = SlotBooked.objects.get(user=request.user)
      roomBooked = Room.objects.get(slot__slotbooked__pk=slotBooked.id)
      
      if slotBooked.isPaid():
        return render(request, "booking/booking_status_room_booked_paid.html", {
                "number": roomBooked.number,
                "type": roomBooked.get_type_display,
                "paymentDate": slotBooked.datePaid,
              })
      else: 
        paypal_dict = {
          "business": settings.PAYPAL_RECEIVER_EMAIL,
          "amount": settings.PAYPAL_AMOUNT,
          "currency_code": "EUR",
          "item_name": u"Réservation chambre ENPC",
          "invoice": slotBooked.id,
          "notify_url": settings.PAYPAL_NOTIFY_URL,
          "return_url": request.build_absolute_uri(), 
          "cancel_return": request.build_absolute_uri(),
        }
        
        return render(request, "booking/booking_status_room_booked_not_paid.html", {
                "number": roomBooked.number,
                "type": roomBooked.get_type_display,
                "paymentDue": slotBooked.dateLimit,
                "form": PayPalPaymentsForm(initial=paypal_dict),
              })

    except SlotBooked.DoesNotExist:
      return render(request, 'booking/booking_start.html', {
                'form': BookingForm(),
              }
            )

@login_required
def validPayment(sender, **kwargs):
  print sender.invoice

@login_required
def addQueue(request):
  try:
    userprofile = UserProfile.objects.get(pk=request.user)
  except UserProfile.DoesNotExist:
    return render(request, "booking/booking_status_empty_profile.html")
  
  try:
    if request.method == 'POST': # If the form has been submitted...
      form = BookingForm(request.POST) # A form bound to the POST data
      
      if form.is_valid(): 
        maxPeople_preference = form.cleaned_data['maxPeople_preference']
        backend.addQueue(request.user, userprofile.serie, maxPeople_preference)
        backend.refreshBooking(userprofile.serie)
        return redirect("booking.views.status") 
      else:
        render(request, 'booking/booking_start.html', {
                'form': form,
          }
        )
    else:
      return redirect("booking.views.status") 
  except: 
    return render(request, 'booking/booking_start.html', {
                'form': BookingForm(),
              }
            )
