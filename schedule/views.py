import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.detail import DetailView
from django.utils import timezone

from schedule.utils import ScheduleCalendar
from .models import Memo, Diary
from .forms import MemoModelForm, MemoEditModelForm, DiaryModelForm, DiaryEditModelForm

def index(request):

    user = request.user
    if user.id is not None:
        return redirect('schedule:memo_main', current=ScheduleCalendar.today)
    else:
        return redirect('member:signin')

# @login_required()
def to_do_list_calendar(request, current=ScheduleCalendar.today):
    date=ScheduleCalendar.today
    today = ScheduleCalendar.today
    this_day = ScheduleCalendar.this_day
    result, _year, this_year, this_month = ScheduleCalendar.month_list(request.user, current)
    this_month_list = ScheduleCalendar.pack_one_week(result)

    context = {
        'thisday': this_day,
        'DAY': ScheduleCalendar.DAY.values(),
        'YEAR': this_year,
        'thismonth': this_month,
        'thisresult': this_month_list,
        'today': today,
    }

    # try:

    #     to_do_list = request.user.todolist_set.get(date=find_date, user=request.user)
    # except ToDoList.DoesNotExist:
    #     return render(request, 'task/calendar.html', context)

    # context['to_do_list'] = to_do_list
    context['date'] = date
    # context['today'] = TaskCalendar.today_to_str()
    context['memos'] = Memo.objects.filter(user=request.user)
    return render(request, 'schedule/calendar.html', context)

# Memo
# @method_decorator(login_required, name='dispatch')
class MemoNew(View):

    def get(self, request, *args, **kwargs):

        form = MemoModelForm()
        return render(request, 'schedule/memo_edit.html', {'form': form})

    def post(self, request,  *args, **kwargs):

        form = MemoModelForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False)
            memo.user = request.user
            memo.save()
            return redirect('schedule:memo_main', current=ScheduleCalendar.today)


# @login_required()
def memo_edit(request, pk):
    memo = get_object_or_404(Memo, pk=pk)
    if request.method == 'POST':
        form = MemoEditModelForm(data=request.POST, instance=memo)

        if form.is_valid():
            form.save()
            return redirect('schedule:memo_main', current=ScheduleCalendar.today)
    else:
        form = MemoEditModelForm(instance=memo)

    return render(request, 'schedule/memo_edit.html', {'form': form})



# @method_decorator(login_required, name='dispatch')
class MemoDetailView(DetailView):

    model = Memo
    template_name = 'schedule/memo_detail.html'

    # def get_context_data(self, **kwargs):
    #     context = super(TaskDetailView, self).get_context_data(**kwargs)
    #     context['date'] = self.object.mission.date.strftime('%Y%m%d')
    #     context['today'] = TaskCalendar.today
    #     return context


# @method_decorator(login_required, name='dispatch')
class MemoDelete(View):

    def post(self, request, *args, **kwargs):
        user = request.user
        memo = get_object_or_404(Memo, pk=kwargs['pk'])
        if memo.user == user:
            memo.delete()

        return redirect('schedule:memo_main', current=ScheduleCalendar.today)

# Diary 모델

class DiaryNew(View):

    def get(self, request, *args, **kwargs):
        context = {}
        form = DiaryModelForm()
        context['form'] = form
        context['date'] = kwargs['diary_id']

        return render(request, 'schedule/diary_edit.html', context)

    def post(self, request,  *args, **kwargs):

        form = DiaryModelForm(request.POST, request.FILES)
        if form.is_valid():
            diary= form.save(commit=False)
            diary.user = request.user
            diary.date = request.POST['date']
            diary.save()
            return redirect('schedule:memo_main', current=ScheduleCalendar.today)
        else:
            return redirect('member:index')

# @login_required()
def diary_edit(request, diary_id):
    diary = get_object_or_404(Diary, date=diary_id, user=request.user)
    if request.method == 'POST':
        form = DiaryEditModelForm(data=request.POST, instance=diary)

        if form.is_valid():
            form.save()
            return redirect('schedule:memo_main', current=ScheduleCalendar.today)
    else:
        form = DiaryEditModelForm(instance=diary)

    return render(request, 'schedule/diary_edit.html', {'form': form})



# @method_decorator(login_required, name='dispatch')
def diary_detail(request, diary_id):

    diary = get_object_or_404(Diary, date=diary_id, user=request.user)
    return render(request, 'schedule/diary_detail.html', {'diary': diary})

    # def get_context_data(self, **kwargs):
    #     context = super(TaskDetailView, self).get_context_data(**kwargs)
    #     context['date'] = self.object.mission.date.strftime('%Y%m%d')
    #     context['today'] = TaskCalendar.today
    #     return context


# @method_decorator(login_required, name='dispatch')
class DiaryDelete(View):

    def post(self, request, *args, **kwargs):
        user = request.user
        print(kwargs['diary_id'])
        diary = get_object_or_404(Diary, date=kwargs['diary_id'], user=request.user)
        if diary.user == user:
            diary.delete()

        return redirect('schedule:memo_main', current=ScheduleCalendar.today)
