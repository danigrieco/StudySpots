from django.shortcuts import get_object_or_404, redirect, render
from .models import Place, Review
from django.views import generic
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from django.contrib.auth.decorators import login_required



class ApprovalView(generic.ListView):
    template_name = "approval.html"
    context_object_name = "places_list"
    # def results(request, question_id):
    #     question = get_object_or_404(Question, pk=question_id)
    #     return render(request, "polls/results.html", {"question": question})

    def get_queryset(self, request):
        if request.user.is_authenticated:
            return Place.objects.all
        else:
            return redirect('home')
    
def see_place(request, place_id):
    if request.user.is_authenticated:
        place = getPlace(place_id)
        return render(request, "place.html", {"place":place})
    else:
        return redirect('home')
    

def admin_approval(request):
    places_list = Place.objects.all()
    if request.method == "POST":
        id_list = request.POST.getlist('boxes')
        did_list = request.POST.getlist('Dboxes')
        # uncheck all boxes before updating because you can't pass in an unchecked box
        places_list.update(delete_place = False)
        places_list.update(admin_approved = False)
        # update the database with these values
        for id in id_list:
            Place.objects.filter(pk=int(id)).update(admin_approved = True)
        for id in did_list:
            Place.objects.filter(pk=int(id)).delete()
        return redirect('places')
    else:
        return render(request, "approval.html", {"places_list":places_list})

def suggest(request):
    if request.user.is_authenticated:
        template_name = "suggest.html"
        if request.method == "POST":
            place_name = request.POST.get('nameInput')
            place_details = request.POST.get('detailInput')
            place_address = request.POST.get('addressInput')
            place_area = request.POST.get('locationInput')
            place = Place(name=place_name, details=place_details, address=place_address, location=place_area)
            place.save()
            return redirect('places')
        return render(request,"suggest.html")
    else:
        return redirect('home')


def getPlace(id):
    return Place.objects.get(id=id)


class PlacesView(generic.ListView):
    template_name = "places.html"
    context_object_name = "places_list"
    def get_queryset(self):
        places = Place.objects.all()
        for place in places:
            place.avg_busy_rating, place.avg_wifi_outlet_rating = place.get_average_review()
        return places
    
    
def ReviewForm(request, place_id):
    if request.user.is_authenticated:
        place = getPlace(place_id)
        template_name = "reviewForm.html"
        if request.method == "POST":
            review_busy = float(request.POST.get('busyInput'))
            review_wifi = float(request.POST.get('wifiOutletInput'))
            review_description = request.POST.get('detailInput')
            review = Review(Place=place, busy_rating=review_busy, wifi_outlet_rating=review_wifi, description=review_description)
            review.save()
            place.avg_busy_rating, place.avg_wifi_outlet_rating = place.get_average_review()
            place.save()
            return redirect('places')
        return render(request,"reviewForm.html", {"place":place})
    else:
        return redirect('home')



class RecommendView(generic.ListView):
    template_name = "recommend.html"
    context_object_name = "places_list"
    def recommend(request):
        busy_rating = int(request.POST.get('busyInput'))
        wifi_outlet_rating = int(request.POST.get('wifiOutletInput'))
        min = 5
        for place in Place.objects.all():
            if place.location == location:
                t1 = abs(place.avg_busy_rating - busy_rating)
                t2 = abs(place.avg_wifi_outlet_rating - wifi_outlet_rating)
                diff = (t1 + t2)/2
                if min > diff:
                    min = diff
                    suggested_place  = place.objects.get_suggested_place(location, busy_rating, wifi_outlet_rating)
            # algorithm to detemrine which spot here
            return render(request, 'suggestion.html', {'suggested_place': suggested_place})

    def get_queryset(self):
        return Place.objects.all
    
def suggest_place(request):
    if request.user.is_authenticated:
        template_namee = "suggestion.html"
        if request.method == 'POST':
            location = request.POST.get('locationInput')
            busy_rating = int(request.POST.get('busyInput'))
            wifi_outlet_rating = int(request.POST.get('wifiOutletInput'))
            min = 5
            for place in Place.objects.all():
                if place.location == location:
                    t1 = abs(place.avg_busy_rating - busy_rating)
                    t2 = abs(place.avg_wifi_outlet_rating - wifi_outlet_rating)
                    diff = (t1 + t2)/2
                    if min > diff:
                        min = diff
                        suggested_place  = place.objects.get_suggested_place(location, busy_rating, wifi_outlet_rating)
            # algorithm to detemrine which spot here
            return render(request, 'suggestion.html', {'suggested_place': suggested_place})

        return render(request, 'suggestion.html')
    else:
        return redirect('home')


