from django.contrib.auth.views import LogoutView
from django.urls import path

from helpdesk import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('login/', views.SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('requests/', views.RequestsListView.as_view(), name='requests'),
    path('requests/new/', views.NewRequestsView.as_view(), name='new'),
    path('requests/support/', views.DepartmentRequestsView.as_view(), name='department_requests'),
    path('requests/<int:request_id>/', views.RequestPageView.as_view()),
    path('requests/create/', views.CreateRequestView.as_view(), name='create'),
    path('request/close/', views.CloseRequestView.as_view(), name='close'),
    path('requests/comment/delete/', views.DeleteCommentView.as_view(), name='delete_comment')
]
