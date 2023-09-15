from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from disaster.models import Disaster
from volunteer.forms import NewVolunteer


def new_volunteer(request):
    # Create your views here.
    if request.method == "POST":
        new_volunteer_form = NewVolunteer(request.POST, request.FILES, request=request)

        if new_volunteer_form.is_valid():
            new_volunteer_form.save()
            messages.success(request, ('Thank you for your Report'))
            return redirect("disaster:main")
        else:
            print(new_volunteer_form.errors)
            messages.error(request, 'Error sending this report')

    new_volunteer_form = NewVolunteer(request=request)
    context = {'volunteer_form': new_volunteer_form}

    return render(request=request, template_name="volunteer.html", context=context)