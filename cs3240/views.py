from django.shortcuts import get_object_or_404, redirect, render
from .models import Place
from django.views import generic

class ApprovalView(generic.ListView):
    template_name = "approval.html"
    context_object_name = "places_list"
     # def results(request, question_id):
    #     question = get_object_or_404(Question, pk=question_id)
    #     return render(request, "polls/results.html", {"question": question})

    def get_queryset(self):
        return Place.objects.all
    
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
    place_name = request.POST.get('nameInput')
    place_details = request.POST.get('detailInput')
    place = Place(name=place_name, details=place_details)
    place.save()
    return render(request,"index.html")

class PlacesView(generic.ListView):
    template_name = "places.html"
    context_object_name = "places_list"

    def get_queryset(self):
        return Place.objects.all