from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    antecedants = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Antecedents (optional)'}),
        label='Antecedents'
    )
    bilan_biologique = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Bilan Biologique (optional)'}),
        label='Bilan Biologique'
    )

    class Meta:
        model = Patient
        fields = [
            'nss', 'date_naissance', 'addresse', 'mutuelle', 
            'medcin_traitant', 'personne_contact'
        ] 
