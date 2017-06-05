from django.shortcuts import render, redirect
from member.forms import SignUpModelForm


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
