from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
import dateutil.parser
from mafqood.models import Mafqood
from disaster.models import Disaster
from mafqood.forms import ReportMissing, NewPerson


@login_required()
def mafqood_update(request, disaster, id):
    mafqood = get_object_or_404(Mafqood, id=id)
    disaster = get_object_or_404(Disaster, id=disaster)
    request.disaster = disaster
    request.mafqood = mafqood

    # Create your views here.
    if request.method == "POST":
        report_form = ReportMissing(request.POST, request.FILES, request=request, instance=mafqood)

        if report_form.is_valid():
            report_form.save()
            messages.success(request, ('Report Updated!'))
            return redirect("mafqood_search", disaster.id)
        else:
            print(report_form.errors)
            messages.error(request, 'Error In Updating Report - Please report to Admin')

    report_form = ReportMissing(request=request, instance=mafqood)
    context = {'disaster': disaster, 'mafqood':mafqood, 'report_form': report_form, 'submit_btn_txt':"Update Changes"}

    return render(request=request, template_name="form_mafqood.html", context=context)


@login_required()
def mafqood_delete(request, disaster, id):
    disaster = get_object_or_404(Disaster, id=disaster)
    mafqood = get_object_or_404(Mafqood, id=id)
    request.disaster = disaster
    request.mafqood = mafqood

    mafqood.delete()
    return redirect("mafqood_search", disaster.id)


@login_required()
def mafqood_search(request, disaster):
    disaster = get_object_or_404(Disaster, id=disaster)

    # Search
    query = request.GET.get('q')
    type = request.GET.get('t')

    if query:
        if type == 'name':
            mafqoods = Mafqood.objects.filter(name=query)
        elif type == 'surname':
            mafqoods = Mafqood.objects.filter(surname=query)
        elif type == 'full_name':
            mafqoods = Mafqood.objects.filter(full_name=query)
        elif type == 'date_of_birth':
            dob = dateutil.parser.parse(query)
            mafqoods = Mafqood.objects.filter(date_of_birth=dob)
        elif type == 'contact_number':
            mafqoods = Mafqood.objects.filter(contact_number=query)
        elif type == 'reporter_number':
            mafqoods = Mafqood.objects.filter(Q(reporter_contact_number=query) | Q(reporter_contact_number_2=query))
        else:
            mafqoods = Mafqood.objects.filter(Q(full_name__icontains=query) | Q(name__icontains=query) | Q(surname__icontains=query))
    else:
        mafqoods = Mafqood.objects.all()

    # Paginator
    paginator = Paginator(mafqoods, 20)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    content = {'disaster': disaster,
               'mafqoods': mafqoods, 'page_obj':page_obj,
               'query':query,
               'type':type}
    return render(request, "mafqoods_list.html", content)


def report_missing(request, disaster):
    disaster = get_object_or_404(Disaster, id=disaster)
    request.disaster = disaster

    # Create your views here.
    if request.method == "POST":
        report_form = ReportMissing(request.POST, request.FILES, request=request)

        if report_form.is_valid():
            report_form.save()
            messages.success(request, ('تم ايصال النموذج. نشكركم جزيل الشكر'))
            return redirect("main")
        else:
            print(report_form.errors)
            messages.error(request, 'كان هناك خطاء في ارسال التبليغ. نرجو تكرار المحاولة')

    report_form = ReportMissing(request=request)
    context = {'disaster': disaster, 'report_form': report_form, 'submit_btn_txt':"ارسل التبليغ"}

    return render(request=request, template_name="form_mafqood.html", context=context)


@login_required()
def missing_dashboard(request, disaster):
    disaster = get_object_or_404(Disaster, id=disaster)

    # Update Age:
    age_update_set = disaster.missings.filter(Q(age__isnull=True) | Q(age=0)).filter(date_of_birth__isnull=False)
    for i in age_update_set:
        i.age = i.calc_age()
        i.save()

    # Geta ll missings date
    mafqood_data = disaster.missings.all()

    context = {'disaster': disaster,
               'total_count': mafqood_data.count(),
               'male_count': mafqood_data.filter(gender='male').count(),
               'female_count': mafqood_data.filter(gender='female').count(),
               'age': {'less than 3': mafqood_data.filter(age__lte=3, age__gt=0).count(),
                       '3 - 16': mafqood_data.filter(age__lte=16,age__gt=3).count(),
                       '16 - 30 ': mafqood_data.filter(age__lte=30, age__gt=16).count(),
                       '30 - 60 ': mafqood_data.filter(age__lte=60, age__gt=30).count(),
                       '60+': mafqood_data.filter(age__gt=60).count(),
                       'Unknown': mafqood_data.filter(Q(age__isnull=True) | Q(age=0)).count()
                    }
               }

    return render(request=request, template_name="dashboard.html", context=context)


@login_required()
def report_new_person(request, disaster):
    disaster = get_object_or_404(Disaster, id=disaster)
    request.disaster = disaster

    # Create your views here.
    if request.method == "POST":
        new_person_form = NewPerson(request.POST, request.FILES, request=request)

        if new_person_form.is_valid():
            new_person_form.save()
            messages.success(request, ('تم ايصال النموذج. نشكركم جزيل الشكر'))
            return redirect("main")
        else:
            print(new_person_form.errors)
            messages.error(request, 'كان هناك خطاء في ارسال التبليغ. نرجو تكرار المحاولة')

    new_person_form = NewPerson(request=request)
    context = {'disaster': disaster, 'report_form': new_person_form}

    return render(request=request, template_name="form_person.html", context=context)


