from django.urls import path

from helpdesk import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('requests/', views.RequestsListView.as_view(), name='requests'),
    path('requests/<int:id>', views.RequestPageView.as_view()),
    path('requests/create', views.CreateRequestView.as_view(), name='create')
]
