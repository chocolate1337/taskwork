from django.contrib import admin

from .models import Phonebook


class PhonebookAdmin(admin.ModelAdmin):
    fields = ('phone', ('lastname', 'firstname', 'patronymic'), ('city', 'street', 'house', 'apartment'),'whatsupp','telegram')
    list_display = ('phone', 'lastname', 'firstname', 'patronymic', 'city', 'street', 'house', 'apartment')
    list_filter = ('lastname', 'city', 'street')
    search_fields = ['phone', 'lastname', 'firstname', 'patronymic', 'city', 'street']


admin.site.register(Phonebook, PhonebookAdmin)
