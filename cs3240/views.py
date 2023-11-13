from django.shortcuts import get_object_or_404, redirect, render
from .models import Place
from django.views import generic
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields



class ApprovalView(generic.ListView):
    template_name = "approval.html"
    context_object_name = "places_list"
    # def results(request, question_id):
    #     question = get_object_or_404(Question, pk=question_id)
    #     return render(request, "polls/results.html", {"question": question})

    def get_queryset(self):
        return Place.objects.all
    
def see_place(request, place_id):
    place = getPlace(place_id)
    return render(request, "place.html", {"place":place})
    

def admin_approval(request):
    places_list = Place.objects.all()
    if request.user.is_superuser:
        if request.method == "POST":
            id_list = request.POST.getlist('boxes')
            # uncheck all boxes before updating because you can't pass in an unchecked box
            places_list.update(admin_approved = False)
            # update the database with these values
            for id in id_list:
                Place.objects.filter(pk=int(id)).update(admin_approved = True)
            return redirect('places')
        else:
            return render(request, "approval.html", {"places_list":places_list})
    else:
        return redirect('home')

def suggest(request):
    template_name = "suggest.html"
    if request.method == "POST":
        place_name = request.POST.get('nameInput')
        place_details = request.POST.get('detailInput')
        place_address = request.POST.get('addressInput')
        place = Place(name=place_name, details=place_details, address=place_address)
        place.save()
        return redirect('places')
    return render(request,"suggest.html")

def getPlace(id):
    return Place.objects.get(id=id)

class PlacesView(generic.ListView):
    template_name = "places.html"
    context_object_name = "places_list"

    def get_queryset(self):
        return Place.objects.all
    
    
class RecommendView(generic.ListView):
    template_name = "recommend.html"
    context_object_name = "places_list"

    def get_queryset(self):
        return Place.objects.all
    
def suggest_place(request):
    template_namee = "suggestion.html"
    if request.method == 'POST':
        location = request.POST.get('locationInput')
        busy_rating = int(request.POST.get('busyInput'))
        wifi_outlet_rating = int(request.POST.get('wifiOutletInput'))
        min = 5
        for Place in places_list:
            if Place.location == location:
                t1 = Place.busy_rating - busy_rating
                t2 = Place.wifi_outlet_rating - wifi_outlet_rating
                if min < abs((t1-t2))/2:
                    min = abs((t1-t2))/2
                    suggested_place  = Place.objects.get_suggested_place(location, busy_rating, wifi_outlet_rating)


        # algorithm to detemrine which spot here
        return render(request, 'suggestion.html', {'suggested_place': suggested_place})

    return render(request, 'suggestion.html')


