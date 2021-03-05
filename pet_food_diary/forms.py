from django import forms

from pet_food_diary.models import Veterinarian


class PetForm(forms.Form):
    name = forms.CharField(max_length=64, label="Pet's name", required=True)
    vet = forms.ModelChoiceField(queryset=Veterinarian.objects.filter(is_vet=True), label="Vet's name")
    date_of_birth = forms.DateField()
    comments = forms.Textarea()
