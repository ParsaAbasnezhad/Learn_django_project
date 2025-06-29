from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView ,FormView
from home.models import ContactUs


class ContactUsView(CreateView):
    model = ContactUs
    fields = '__all__'
    template_name = 'home/index.html'
    success_url = reverse_lazy('home:contact-us')
    def form_valid(self, form):
        form_data = form.cleaned_data
        ContactUs.objects.create(**form_data)
        return super().form_valid(form)

