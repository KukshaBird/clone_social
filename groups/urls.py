#GROUPS URL.PY
from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
	path('',views.ListGroups.as_view(),name='all'),
	path('new/',view.CreateView.as_view(),name='create'),
	path('post/in/<str:slug>/',views.SingleGroup.as_view(),name='single'),
]
