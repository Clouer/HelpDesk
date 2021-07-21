from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from helpdesk.forms import SignUpForm, CreateRequestForm
from helpdesk.models import User, Request, Department
from helpdesk.scripts import register_user, create_request, close_request


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
        if request.user.is_anonymous:
            return redirect(reverse('login'))
        return render(request, 'helpdesk/index.html')


class RequestsListView(View):
    def get(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('login'))
        active_requests = Request.objects.filter(owner=request.user.id, status__in=['new', 'in_work'])
        status = 'active_requests'

        return render(request, 'helpdesk/requests_list.html', context={
            'current_requests': active_requests,
            'status': status
        })

    def post(self, request):
        page_status = request.POST['page_status']
        if page_status == 'closed_requests':
            closed_request = Request.objects.filter(owner=request.user.id, status='closed')
            return render(request, 'helpdesk/requests_list.html', context={
                'current_requests': closed_request,
                'status': page_status
            })
        else:
            return redirect(reverse('requests'))


class DepartmentRequestsView(View):
    def get(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('login'))
        if not request.user.is_super_support and not request.user.is_support:
            return redirect(reverse('requests'))
        user_departments = request.user.departments.all()
        active_requests = Request.objects.filter(departments__in=user_departments,
                                                 status__in=['new', 'in_work']).distinct()
        status = 'active_requests'
        return render(request, 'helpdesk/department_requests.html', context={
            'current_requests': active_requests,
            'status': status
        })

    def post(self, request):
        page_status = request.POST['page_status']
        if page_status == 'closed_requests':
            user_departments = request.user.departments.all()
            closed_request = Request.objects.filter(departments__in=user_departments, status='closed').distinct()
            return render(request, 'helpdesk/requests_list.html', context={
                'current_requests': closed_request,
                'status': page_status
            })
        else:
            return redirect(reverse('department_requests'))


class NewRequestsView(View):
    def get(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('login'))
        if not request.user.is_super_support:
            return redirect(reverse('requests'))
        departments = Department.objects.all()
        new_requests = Request.objects.filter(status='new')
        return render(request, 'helpdesk/new_requests.html', context={
            'departments': departments,
            'new_requests': new_requests
        })

    def post(self, request):
        form = request.POST
        departments = form.getlist('departments')
        current_request = Request.objects.get(pk=form['request_id'])
        for department in departments:
            current_request.departments.add(department)
        current_request.status = 'in_work'
        current_request.save()
        return redirect(reverse('new'))


class RequestPageView(View):
    def get(self, request, request_id):
        if request.user.is_anonymous:
            return redirect(reverse('login'))
        request_object = get_object_or_404(Request, pk=request_id)
        return render(request, 'helpdesk/request_page.html', context={
            'request_object': request_object
        })


class CreateRequestView(View):
    def get(self, request):
        if request.user.is_anonymous:
            return redirect(reverse('login'))
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


class CloseRequestView(View):
    def post(self, request):
        close_request(Request, request.POST['request_id'])
        previous_page = request.POST['current_url']
        if not previous_page:
            return redirect(reverse('main'))
        return redirect(previous_page)
