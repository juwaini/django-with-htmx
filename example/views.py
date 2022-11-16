from .models import Word
from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.edit import UpdateView
from django.shortcuts import render


class IndexView(ListView):
    template_name = 'index.html'
    model = Word


class WordDemoView(TemplateView):
    template_name = 'word-demo.html'

    def get_context_data(self, **kwargs):
        context = super(WordDemoView, self).get_context_data(**kwargs)
        context['words'] = Word.objects.all()
        return context


class DefaultButtonView(TemplateView):
    template_name = 'default-create-button.html'


class WordCreateView(CreateView):
    template_name = 'word-create.html'

    model = Word

    fields = '__all__'

    success_url = '/get-default-button'


class ClickToEditView(TemplateView):
    template_name = 'click-to-edit.html'


class WordEditView(UpdateView):
    model = Word
    fields = '__all__'
    template_name = 'click-edit.html'
    success_url = '/get-default-button'


class ClickDemo(TemplateView):
    template_name = 'click-demo.html'


def clicked(request):
    return render(request, template_name='clicked.html')
