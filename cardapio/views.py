from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse

from cardapio.models import Loja

from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
class LojaUpdateView(UpdateView):
	model = Loja
	template_name = 'cardapio/loja_form.html'
	fields = ('nome', 'pedido_minimo', )
	success_url = reverse_lazy('lojas_list')


class LojaCreateView(CreateView):
	model = Loja
	template_name = 'cardapio/create.html'
	fields = ('nome', 'pedido_minimo', )
	success_url = reverse_lazy('lojas_list')


def lojas(request):
    todas_lojas = Loja.objects.all()
    print()
    print(todas_lojas)
    print()
    return TemplateResponse(
			request,
			'cardapio/lojas.html',
			{'lojas': todas_lojas }
		)

def loja_detail(request, loja_id):
	loja = get_object_or_404(Loja, pk=loja_id)
	return render(request, 'cardapio/loja_detail.html', {'loja': loja})
