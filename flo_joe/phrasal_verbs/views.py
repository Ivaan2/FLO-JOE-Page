from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from . import models

# Create your views here.
def phrasal_verbs_view(request):
    phrasal_verbs = models.PhrasalVerb.objects.all()
    return render(request, 'phrasal_verbs/index.html', {'phrasal_verbs': phrasal_verbs})

def phrasal_verbs_detail_view(request, pk):
    phrasal_verb = models.PhrasalVerb.objects.get(pk=pk)
    return render(request, 'phrasal_verbs/phrasal_verb_view.html', {'p': phrasal_verb})