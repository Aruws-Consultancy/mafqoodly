from django import forms
from disaster.models import Disaster
from mafqood.models import Mafqood, Person


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

        # Set disaster
        self.fields['disaster'].queryset = Disaster.objects.filter(id=self.request.disaster.id)
        self.fields['disaster'].initial = self.request.disaster

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data


class NewPerson(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'
        widgets = {'disaster': forms.HiddenInput(),
                   'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
                    }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(NewPerson, self).__init__(*args, **kwargs)

        # Set disaster
        self.fields['disaster'].queryset = Disaster.objects.filter(id=self.request.disaster.id)
        self.fields['disaster'].initial = self.request.disaster

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data