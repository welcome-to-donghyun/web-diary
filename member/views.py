from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,\
    login as auth_login, \
    logout as auth_logout
from member.forms import SignUpModelForm, SignInModelForm
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = SignUpModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member:signin')
        messages.error(request, '이미 존재하는 이메일/닉네임이거나, 비밀번호가 같지 않습니다.')
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
            return redirect('schedule:memo_main')
        else:
            form = SignInModelForm()
            messages.error(request, '아이디 또는 비밀번호를 다시 확인하세요.')
            return render(request, 'member/signin.html', {'form': form})
    else:
        form = SignInModelForm()
        return render(request, 'member/signin.html', {'form': form})

def signout(request):
    auth_logout(request)
    return redirect('member:signin')
