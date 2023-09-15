from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from disaster.models import Disaster


def disaster(request, disaster=None):
    if disaster:
        disaster = Disaster.objects.get(name=disaster)
    else:
        disaster = Disaster.objects.get(is_main_focus=True)

    counter = int(280) + int(disaster.missings.all().count())
    if counter < 10000:
        counter = f'0{counter}'
    content = {'disaster':disaster, 'counter':str(counter)}

    return render(request, "disaster.html", content)
