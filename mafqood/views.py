from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from disaster.models import Disaster
from mafqood.models import Mafqood


def mafqood_update(request, id):
    mafqood = get_object_or_404(Mafqood, id=id)
    content = {'mafqood': mafqood}
    return render(request, "main.html", content)


class ReportMissing(forms.ModelForm):

    class Meta:
        model = Mafqood
        fields = '__all__'
        widgets = {'disaster': forms.HiddenInput(),
                   'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
                   'last_contact_date': forms.DateInput(attrs={'type': 'date'})
                    }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(ReportMissing, self).__init__(*args, **kwargs)

        if not self.request.POST:
            # Set disaster
            self.fields['disaster'].queryset = Disaster.objects.filter(id=self.request.disaster.id)
            self.fields['disaster'].initial = self.request.disaster

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data


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
