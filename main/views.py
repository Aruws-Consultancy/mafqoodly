from mafqood.models import Mafqood
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import TemplateView


def landing(request):
    mafqood_count = Mafqood.objects.all().count()
    content = {'mafqood_count':mafqood_count}
    return render(request, "main.html", content)

