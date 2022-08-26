from doctest import Example
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from . import models

# Create your views here.
def phrasal_verbs_view(request):
    #p = models.PhrasalVerb.objects.create(verb='Run out', definition='To use something completely so that nothing is left', traduction='Quedarse sin', example='The policeman ran out of bullets while chasing the robber.')
    #p.save()
    phrasal_verbs = models.PhrasalVerb.objects.all()
    return render(request, 'phrasal_verbs/index.html', {'phrasal_verbs': phrasal_verbs})

def phrasal_verbs_detail_view(request, pk):
    phrasal_verb = models.PhrasalVerb.objects.get(pk=pk)
    return render(request, 'phrasal_verbs/phrasal_verb_view.html', {'p': phrasal_verb})