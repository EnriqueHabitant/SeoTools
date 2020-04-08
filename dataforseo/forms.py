from django import forms
from .models import KeywordSearch
from .dataforseo_functions import paises_v3

class KeywordFinderForm(forms.ModelForm):
 
    class Meta:
        # Petición de códigos de leguajes a la api.
        model = KeywordSearch
        fields = ['method', 'keyword', 'language', 'limit', 'depth', 'filters', 'result']
        widgets = {
            'method': forms.TextInput(attrs={'class':'input is-hidden', 'value':'KeywordFinder'}),
            'keyword': forms.TextInput(attrs={'class':'input', 'placeholder':'Keyword'}),
            'language': forms.Select(attrs={}, choices=paises_v3()),
            'limit': forms.NumberInput(attrs={'class':'input', 'min':1, 'max':1000, 'value':20}),
            'depth': forms.NumberInput(attrs={'class':'input', 'min':1, 'max':4, 'value':2}),
            'filters': forms.Textarea(attrs={'class':'input'}),
            'result': forms.Textarea(attrs={'class':'input is-hidden'}),
        }
        labels = {
            'method':'', 'keyword':'Keyword', 'language': 'Idioma/Región', 'limit':'Límite', 'depth':'Profundidad', 'filters': 'Filtros', 'result':''
        }

class KeywordData(forms.Form):
    pass
