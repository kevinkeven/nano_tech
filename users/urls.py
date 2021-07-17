from django.urls import path
from .views import SignUpView, UserChangeView
#from .forms import UserChangeForm

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]