from django.urls import path
from accounts.views import login_view, logoute_view, user_registration_view, home_view, dashboard

app_name = 'accounts'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('home/', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logoute_view, name='logout'),
    path('registration/', user_registration_view, name='registration'),
]