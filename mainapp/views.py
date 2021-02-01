from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Phonebook


class HomeView(ListView):
    model = Phonebook
    template_name = 'index.html'
    context_object_name = 'phones'


class AddPhoneView(CreateView):
    model = Phonebook
    fields = ['phone', 'lastname', 'firstname', 'patronymic', 'city', 'street', 'house', 'apartment','whatsupp','telegram']
    template_name = 'add_phone.html'
    success_url = '/'


class EditPhoneView(UpdateView):
    model = Phonebook
    fields = ['phone', 'lastname', 'firstname', 'patronymic', 'city', 'street', 'house', 'apartment','whatsupp','telegram']
    template_name = 'edit_phone.html'
    success_url = '/'


class DeletePhoneView(DeleteView):
    model = Phonebook
    template_name = 'delete_phone.html'
    success_url = reverse_lazy('index')


class SearchPhoneView(HomeView):
    template_name = 'search_phone.html'
    context_object_name = 'search_result'

    def get_queryset(self):
        return Phonebook.objects.filter(
            Q(phone__icontains=self.request.GET.get('s')) |
            Q(lastname__icontains=self.request.GET.get('s')) |
            Q(firstname__icontains=self.request.GET.get('s')) |
            Q(patronymic__icontains=self.request.GET.get('s')) |
            Q(city__icontains=self.request.GET.get('s')) |
            Q(street__icontains=self.request.GET.get('s')) |
            Q(house__icontains=self.request.GET.get('s')) |
            Q(apartment__icontains=self.request.GET.get('s')) |
            Q(whatsupp__icontains=self.request.GET.get('s'))    |
            Q(telegram__icontains=self.request.GET.get('s'))
        )
