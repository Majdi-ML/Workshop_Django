from django.shortcuts import render
from .models import Livre
from django.views.generic import ListView

# Create your views here.


def list(req):
    livres = Livre.objects.all()

    return render(req, 'livre.html', {'livre': livres})


class ListLivres(ListView):

    model = Livre
    template_name = "livre.html"

    context_object_name = "livre"
