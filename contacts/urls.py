from django.urls import path
from .views import ContactPageDetailView
app_name = 'contacts'
urlpatterns = [
    path('', ContactPageDetailView.as_view() , name='contact_page_form_view'),
    
]