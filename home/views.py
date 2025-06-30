from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from home.models import ContactUs, StudentsAbout




class ContactUsView(CreateView):
    model = ContactUs
    fields = '__all__'
    template_name = 'home/index.html'
    success_url = reverse_lazy('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = StudentsAbout.objects.all()
        return context

    def form_valid(self, form):
        form_data = form.cleaned_data
        ContactUs.objects.create(**form_data)
        return super().form_valid(form)







