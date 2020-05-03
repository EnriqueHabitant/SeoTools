from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from django.views.generic import TemplateView, CreateView, DetailView
from django.urls import reverse, reverse_lazy
import json, datetime, calendar
from operator import itemgetter
from django.template.base import Variable
from .dataforseo_functions import related_keywords_v3, keyword_suggestions_v3
from .models import KeywordSearch, KeywordBulk
from .forms import KeywordFinderForm, KeywordBulkForm

# Create your views here.
class KeywordFinderCreateView(CreateView):
    model = KeywordSearch
    template_name = "dataforseo/keywordfinder_form.html"
    form_class = KeywordFinderForm

    def get_success_url(self, *args, **kwargs):        
        print(self.object.pk)
        return reverse_lazy('dataforseo:keywordfinder_detail', kwargs={'pk':self.object.pk})

class KeywordFinderDetailView(DetailView):
    model = KeywordSearch
    template_name = "dataforseo/keywordfinder_form.html"
    form = KeywordFinderForm()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(KeywordFinderDetailView, self).get_context_data(**kwargs)
        # Funciones EXTRAS.
        def monthdelta(date, delta):
            m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
            if not m: m = 12
            d = min(date.day, calendar.monthrange(y, m)[1])
            return date.replace(day=d,month=m, year=y)
        def _property_resolver(arg):
            try:
                float(arg)
            except ValueError:
                return Variable(arg).resolve
            else:
                return itemgetter(arg)
        # Cargando JSON.
        res = json.loads(context['object'].result)
        
        for items in res['result']:
            if 'items' in items:
                for item in items['items']:
                    index = items['items'].index(item)
                    if 'keyword_data' in item:
                        items['items'][index] = item['keyword_data']

                    for a in items['items'][index]['keyword_info']['monthly_searches']:
                        date_str = "1"+"/"+str(a['month'])+"/"+str(a['year'])
                        format_str = '%d/%m/%Y'
                        datetime_obj = datetime.datetime.strptime(date_str, format_str)
                        a["date"]= datetime_obj
            else:
                items['items'] = None

        count = 1
        meses_atras = list()
        while count < 13:
            next_month = monthdelta(datetime.datetime.now(), -(count+1))
            meses_atras.append(next_month.strftime("%b, %Y"))
            count = count+1

        context['form'] = self.form
        context['meses_atras'] = meses_atras
        context['resultado'] = res['result']
        return context
    
# KewordList
class KeywordBulkCreateView(CreateView):
    model = KeywordBulk
    template_name = "dataforseo/keywordbulk_form.html"
    form_class = KeywordBulkForm

    def get_success_url(self, *args, **kwargs):        
        print(self.object.pk)
        return reverse_lazy('dataforseo:keywordfinder_detail', kwargs={'pk':self.object.pk})


# Vistas de Dataforseo
def keyword_research(request, keyword, country_code, language_code, depth, limit, filters):
    resultados = dict()
    resultados['result'] = list()
    filtros = list()

    if filters != 'False':
        for row in filters.split('&&'):
            filtros.append(row.split(','))
            filtros.append('and')
        filtros.pop()
    else:
        filtros = False

    resultados['result'].append(keyword_suggestions_v3(keyword, country_code, language_code, limit, filtros))
    resultados['result'].append(related_keywords_v3(keyword, country_code, language_code, depth, limit, filtros))
    return  JsonResponse(resultados)

# Template del includes
class Filter(TemplateView):
    template_name = "dataforseo/includes/filter.html"

class Loading(TemplateView):
    template_name = "dataforseo/includes/loading.html"