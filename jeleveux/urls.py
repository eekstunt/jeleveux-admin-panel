from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view()),
    path('addpost/', include('deeplink.urls'))
]