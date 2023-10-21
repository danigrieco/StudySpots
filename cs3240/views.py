from django.shortcuts import get_object_or_404, render
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