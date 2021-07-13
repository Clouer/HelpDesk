from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View


class SignInView(LoginView):
    redirect_authenticated_user = True


class SignUpView(View):
    pass


class MainView(View):
    def get(self, request):
        return render(request, 'helpdesk/index.html')


class RequestsListView(View):
    def get(self, request):
        return render(request, 'helpdesk/requests_list.html')


class RequestPageView(View):
    def get(self, request, id):
        return render(request, 'helpdesk/request_page.html', context={
            'request_id': f'000{id}'
        })


class CreateRequestView(View):
    def get(self, request):
        return render(request, 'helpdesk/create_request.html')
