from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from mafqood.models import Mafqood
from disaster.models import Disaster
from mafqood.forms import ReportMissing, NewPerson


def mafqood_update(request, id):
    mafqood = get_object_or_404(Mafqood, id=id)
    content = {'mafqood': mafqood}
    return render(request, "main.html", content)


def report_missing(request, disaster):
    disaster = get_object_or_404(Disaster, id=disaster)
    request.disaster = disaster

    # Create your views here.
    if request.method == "POST":
        report_form = ReportMissing(request.POST, request.FILES, request=request)

        if report_form.is_valid():
            report_form.save()
            messages.success(request, ('Thank you for your Report'))
            return redirect("disaster:main")
        else:
            print(report_form.errors)
            messages.error(request, 'Error sending this report')

    report_form = ReportMissing(request=request)
    context = {'disaster': disaster, 'report_form': report_form}

    return render(request=request, template_name="mafqood.html", context=context)


@login_required()
def report_new_person(request, disaster):
    disaster = get_object_or_404(Disaster, id=disaster)
    request.disaster = disaster

    # Create your views here.
    if request.method == "POST":
        new_person_form = NewPerson(request.POST, request.FILES, request=request)

        if new_person_form.is_valid():
            new_person_form.save()
            messages.success(request, ('Thank you for your Report'))
            return redirect("disaster:main")
        else:
            print(new_person_form.errors)
            messages.error(request, 'Error sending this report')

    new_person_form = NewPerson(request=request)
    context = {'disaster': disaster, 'report_form': new_person_form}

    return render(request=request, template_name="report_new_person.html", context=context)


