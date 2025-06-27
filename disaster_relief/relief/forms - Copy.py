from django import forms
from .models import Disaster
from .models import Donation
from .models import MissingPerson

class DisasterForm(forms.ModelForm):
    class Meta:
        model = Disaster
        fields = ['name', 'location', 'severity', 'description']


class DonationForm(forms.ModelForm):
    model = Donation
    fields = ['name', 'email', 'amount']  # Ensure 'email' is included

class MissingPersonForm(forms.ModelForm):
    class Meta:
        model = MissingPerson
        fields = ['name', 'age', 'gender', 'last_seen_location', 'date_last_seen', 'contact_info', 'photo']
        widgets = {
            'date_last_seen': forms.DateInput(attrs={'type': 'date'}),
        }
