from django import forms
from .models import LatexExpression


class LatexForm(forms.ModelForm):
    class Meta:
        model = LatexExpression
        fields = ['expression']
