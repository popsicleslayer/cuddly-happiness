from django import forms
from django.contrib.admin import widgets
from django.forms import ModelForm

from pet_food_diary.models import Veterinarian, PetModel, MealModel, PetFoodAmountModel


class PetForm(forms.Form):
    name = forms.CharField(max_length=64, label="Pet's name", required=True)
    vet = forms.ModelChoiceField(queryset=Veterinarian.objects.filter(is_vet=True), label="Vet's name", required=False)
    date_of_birth = forms.DateField(label="Pet's birth date",
                                    widget=forms.DateInput(format='%d%m%Y', attrs={'class':'form-control',
                                                                                   'placeholder':'Select a date',
                                                                                   'type':'date'}))
    comments = forms.CharField(widget=forms.Textarea, required=False)


class MealForm(ModelForm):
    class Meta:
        model = MealModel
        fields = ('pet', 'date')

    def __init__(self, *args, **kwargs):
        self.pet = forms.ModelChoiceField(queryset=PetModel.objects.filter(owner=kwargs.pop('user', None)))

        super(MealForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget = widgets.AdminSplitDateTime()

class PetFoodAmountForm(ModelForm):
    class Meta:
        model = PetFoodAmountModel
        fields = '__all__'