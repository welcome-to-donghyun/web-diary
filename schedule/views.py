import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.detail import DetailView
from django.utils import timezone

from schedule.utils import ScheduleCalendar

def index(request):
    return render(request, 'common/index.html', {})

# @login_required()
def to_do_list_calendar(request, date=ScheduleCalendar.today):

    today = ScheduleCalendar.today
    this_year = ScheduleCalendar.this_year
    this_day = ScheduleCalendar.this_day
    this_month = ScheduleCalendar.this_month
    result, _year = ScheduleCalendar.month_list(request.user)
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
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])
    find_date = datetime.date(year, month, day)
    #     to_do_list = request.user.todolist_set.get(date=find_date, user=request.user)
    # except ToDoList.DoesNotExist:
    #     return render(request, 'task/calendar.html', context)

    # context['to_do_list'] = to_do_list
    context['date'] = date
    # context['today'] = TaskCalendar.today_to_str()
    return render(request, 'schedule/calendar.html', context)
