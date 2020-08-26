from django import forms
from .models import KeywordSearch, KeywordList
from .dataforseo_functions import paises_v3

class KeywordFinderForm(forms.ModelForm):
 
    class Meta:
        model = KeywordSearch
        fields = ['method', 'keyword', 'language', 'limit', 'depth', 'filters', 'result', 'user']
        widgets = {
            'method': forms.TextInput(attrs={'value':'KeywordFinder'}),
            'keyword': forms.TextInput(attrs={'class':'', 'placeholder':'Ingrese palabra clave'}),
            'language': forms.Select(attrs={}, choices=paises_v3()),
            'limit': forms.NumberInput(attrs={'class':'', 'min':1, 'max':1000, 'value':20}),
            'depth': forms.NumberInput(attrs={'class':'', 'min':1, 'max':4, 'value':2}),
            'filters': forms.Textarea(),
            'result': forms.Textarea(),
            'user': forms.TextInput(),
        }
        labels = {
            'method':'', 'keyword':'Keyword', 'language': 'Idioma/Región', 'limit':'Límite', 'depth':'Profundidad', 'filters': 'Filtros', 'result':'', 'user':''
        }

class KeywordBulkForm(forms.ModelForm):
    class Meta:
        model = KeywordList
        fields = ['method', 'keywords', 'language', 'result', 'user']
        widgets = {
            'method': forms.TextInput(attrs={'class':'', 'value':'KeywordList'}),
            'keywords': forms.Textarea(attrs={'class':'textarea', 'placeholder':'Keywords'}),
            'language': forms.Select(attrs={}, choices=paises_v3()),
            'result': forms.Textarea(),
            'user': forms.TextInput(),
        }
        labels = {
            'method':'', 'keywords':'Listado de keywords', 'language': 'Idioma/Región', 'result':'', 'user':''
        }
