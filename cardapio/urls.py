from django.urls import path

from cardapio.views import lojas, loja_detail, LojaCreateView, LojaUpdateView


urlpatterns = [
	path('lojas', lojas, name="lojas_list"),
	path('loja/<int:loja_id>', loja_detail, name="show_loja"),
	path('loja/add', LojaCreateView.as_view(), name="loja_add"),
	path('loja/<int:pk>/edit', LojaUpdateView.as_view(), name="loja_edit"),
]
