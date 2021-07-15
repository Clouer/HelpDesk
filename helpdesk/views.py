from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from helpdesk.forms import SignUpForm, CreateRequestForm
from helpdesk.models import User, Request
from helpdesk.scripts import register_user, create_request


class SignInView(LoginView):
    redirect_authenticated_user = True
    template_name = 'helpdesk/login.html'


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'helpdesk/register.html', context={
            'form': form
        })

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            cleaned_form = form.cleaned_data
            register_user(User, cleaned_form)
        return redirect(reverse('login'))


class MainView(View):
    def get(self, request):
        return render(request, 'helpdesk/index.html')


class RequestsListView(View):
    def get(self, request):
        return render(request, 'helpdesk/requests_list.html')


class RequestPageView(View):
    def get(self, request, request_id):
        request_object = get_object_or_404(Request, pk=request_id)
        return render(request, 'helpdesk/request_page.html', context={
            'request_object': request_object
        })


class CreateRequestView(View):
    def get(self, request):
        form = CreateRequestForm()
        return render(request, 'helpdesk/create_request.html', context={
            'form': form
        })

    def post(self, request):
        form = CreateRequestForm(request.POST)
        if form.is_valid():
            cleaned_form = form.cleaned_data
            create_request(Request, cleaned_form)
        return redirect(reverse('main'))
