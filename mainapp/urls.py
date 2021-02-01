from django.urls import path

from .views import AddPhoneView, DeletePhoneView, EditPhoneView, HomeView, SearchPhoneView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('add/', AddPhoneView.as_view(), name='add_phone'),
    path('search/', SearchPhoneView.as_view(), name='search_phone'),
    path('edit/<int:pk>/', EditPhoneView.as_view(), name='edit_phone'),
    path('edit/<int:pk>/delete/', DeletePhoneView.as_view(), name='delete_phone'),
]
