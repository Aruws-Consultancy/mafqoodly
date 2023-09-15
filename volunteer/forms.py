from django import forms
from volunteer.models import Volunteer


class NewVolunteer(forms.ModelForm):

    class Meta:
        model = Volunteer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(NewVolunteer, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data