from django.shortcuts import render
from clima.forms import ClimaForms
from clima.informacoes_clima import informacoes_clima
def index(request):
    form = ClimaForms()
    dict_clima = {}
    if request.method == 'POST':
        form = ClimaForms(request.POST)        
        cidade = form["cidade"].value()
        dict_clima = informacoes_clima(cidade)        
        
    return render(request,'clima.html', {"form": form, "dados": dict_clima})