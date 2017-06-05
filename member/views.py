from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,\
    login as auth_login
from member.forms import SignUpModelForm, SignInModelForm


def signup(request):
    if request.method == 'POST':
        form = SignUpModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member:signup')
        form = SignUpModelForm()
    else:
        form = SignUpModelForm()
    return render(request, 'member/signup.html',{'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInModelForm(request.POST)
        email = form.data['email']
        password = form.data['password']
        user = authenticate(
            email=email,
            password=password,
        )

        if user is not None:
            auth_login(request, user)
            return redirect('member:signup')
        else:
            form = SignInModelForm()
            return render(request, 'member/signin.html', {'form': form})
    else:
        form = SignInModelForm()
        return render(request, 'member/signin.html', {'form': form})
