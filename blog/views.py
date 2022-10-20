from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse
from django.template.response import TemplateResponse

from blog.models import Post # adicionada

def index(request):
	# return HttpResponse('Olá Django - index')
    return TemplateResponse(request, 'index.html', {'nome': 'Wanderson'})


def ola(request):
	# return HttpResponse('Olá Django')
	posts = Post.objects.all()
	return TemplateResponse(
			request,
			'posts_tpl.html',
			{'posts_list': posts }
		)

def post_detail(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'post/detail.html', {'post': post})


class PostDetailView(DetailView):
	model = Post
	template_name = 'post/detail.html'
	context_object_name = 'post'


class PostCreateView(CreateView):
	model = Post
	template_name = 'post/create.html'
	fields = ('body_text', 'pub_date', )
	success_url = reverse_lazy('posts_list')

class PostUpdateView(UpdateView):
	model = Post
	template_name = 'post/post_form.html'
	fields = ('body_text', 'pub_date', )
	success_url = reverse_lazy('posts_list')

class PostDeleteView(DeleteView):
	model = Post
	template_name = 'post/post_confirm_delete.html'
	success_url = reverse_lazy('posts_list')
	success_message = 'Post excluído com sucesso.'
	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(PostDeleteView, self).delete(request, *args, **kwargs)
