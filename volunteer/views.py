from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from volunteer.forms import NewVolunteer


def new_volunteer(request):
    # Create your views here.
    if request.method == "POST":
        new_volunteer_form = NewVolunteer(request.POST, request.FILES, request=request)

        if new_volunteer_form.is_valid():
            new_volunteer_form.save()
            messages.success(request, ('نشكركم لتعاون معنا. عضو من فريقنا سيتصل بكم قريبا!'))
            return redirect("main")
        else:
            print(new_volunteer_form.errors)
            messages.error(request, 'Error in sending this form!')

    new_volunteer_form = NewVolunteer(request=request)
    context = {'volunteer_form': new_volunteer_form}

    return render(request=request, template_name="form_volunteer.html", context=context)