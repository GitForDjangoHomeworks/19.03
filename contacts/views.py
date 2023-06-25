
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView
from django.views.generic.base import TemplateView
from .forms import ContactFormDB
from .models import ContactPage
from icecream import ic
# Create your views here.

class ContactPageDetailView(TemplateView):
    template_name = 'contacts/contact_page.html'
    form_class = ContactFormDB
    success_url = reverse_lazy('contacts:contact_page_form_view')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class
        context['contacts'] = ContactPage.objects.get(pk=1)

        return context

    def post(self, request, *args, **kwargs ):
        ic('post')
        form = ContactFormDB(request.POST)
        if form.is_valid():
            form.save()
        
         
        return redirect('contacts:contact_page_form_view')
    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)