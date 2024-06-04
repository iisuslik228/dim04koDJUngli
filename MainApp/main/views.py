from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request, 'main/logPage.html')

def register(request):
    print('register')
    print('request: ', request)
    print('request.method: ', request.method)
    if request.method == 'POST':
        print('request.method: ', request.method)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/regPage.html', {'form': form})

def main(request):
    return render(request, 'main/main.html')
