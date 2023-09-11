from django.forms import ModelForm
from .models import Product, Team, Testominals
from django.contrib.auth.forms import UserCreationForm


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'


class TestimonialsForm(ModelForm):
    class Meta:
        model = Testominals
        fields = '__all__'
