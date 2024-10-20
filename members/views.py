from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib import messages

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('registered')
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', { 'form': form})
# Create your views here.


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, ('You were logged out!'))
        return redirect('post_list')
    return HttpResponse('Only POST requests are allowed', status=405)