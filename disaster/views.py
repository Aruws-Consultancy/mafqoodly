from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from disaster.models import Disaster


def media(request):
    return render(request, "media.html")

def disaster(request, disaster=None):
    if disaster:
        disaster = Disaster.objects.get(id=disaster)
    else:
        disaster = Disaster.objects.get(is_main_focus=True)

    counter = int(280) + int(disaster.missings.all().count())
    if counter < 10000:
        counter = f'0{counter}'
    content = {'disaster':disaster, 'counter':str(counter)}

    return render(request, "disaster.html", content)


# Errors
# -----------------------------------------------------------------------------------------
def error_404(request, exception):
    status_code = 404
    context = {"status_code": status_code}
    response = render(request, "errors.html", context=context)
    response.status_code = status_code
    return response


def error_500(request):
    status_code = 500
    context = {"status_code": status_code}
    response = render(request, "errors.html", context=context)
    response.status_code = status_code
    return response


def error_403(request, exception):
    status_code = 403
    context = {"status_code": status_code}
    response = render(request, "errors.html", context=context)
    response.status_code = status_code
    return response
