#CLONE URLS.PY
from django.urls import path
# as auth_views because: don't mix it with our views below
from django.contrib.auth import views as auth_views
from . import views

app_name = "clone"

urlpatterns = [
	path("login/",
		auth_views.LoginView.as_view(template_name='clone/login.html'),
		name='login'),
	path("logout/",auth_views.LogoutView.as_view(),name='logout'),
	path("signup/",views.SignUp.as_view(),name='signup'),
]