from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from mafqood.models import Mafqood
from disaster.models import Disaster
from mafqood.forms import ReportMissing


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
        else:
            messages.error(request, 'Error sending this report')

        return redirect("disaster:main")

    report_form = ReportMissing(request=request)
    context = {'disaster': disaster, 'report_form': report_form}

    return render(request=request, template_name="mafqood.html", context=context)
