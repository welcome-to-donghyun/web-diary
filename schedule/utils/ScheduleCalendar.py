import calendar
import datetime

from django.utils import timezone
from ..models import Diary

DAY = {
    0: 'Sun',
    1: 'Mon',
    2: 'Tue',
    3: 'Wed',
    4: 'Thu',
    5: 'Fri',
    6: 'Sat',
}

YEAR = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}


def today_to_str():
    return timezone.localtime(timezone.now()).strftime('%Y%m%d')

today = today_to_str()
this_year = int(today[:4])
this_month = int(today[4:6])
this_day = int(today[6:])





_year = {}


def month_list(user, current):
    this_year = int(current[:4])
    this_month = int(current[4:6])
    this_year_calendar = calendar.Calendar(calendar.SUNDAY).yeardays2calendar(this_year, 1)
    result = []

    for num, month_wrap in enumerate(this_year_calendar):
        _year.update({YEAR[num + 1]: []})
        for month in month_wrap:
            for week in month:
                _year[YEAR[num + 1]].append(week)

    for week in _year[YEAR[this_month]]:
        for day in week:
            # 일자가 포함되어있다면
            if day[0] != 0:
                if day[0] < 10:
                    if this_month <10:
                        date='{}0{}0{}'.format(this_year, this_month, day[0])
                    else:
                        date='{}{}0{}'.format(this_year, this_month, day[0])
                else:
                    if this_month <10:
                        date='{}0{}{}'.format(this_year, this_month, day[0])
                    else:
                        date='{}{}{}'.format(this_year, this_month, day[0])
            else:
                date = 0
            print (date)
            # 다이어리가 있는지 없는지 여부

            if date != 0:

                diary = Diary.objects.filter(date=date, user=user)
                print (diary)
                if diary:
                    # 다이어리가 있을 경우
                    result.append((day[0], day[1], date, 1))
                else:
                    # 다이어리가 없을 경우
                    result.append((day[0], day[1], date, 0))
            else:
                # 해당 날짜가 없을 경우
                result.append((day[0], day[1], date, -1))
    print (result)

    return result, _year, this_year, this_month



def pack_one_week(result):

    pack_result = []
    for i in range(5):
        i *= 7
        pack_result.append(result[i:i+7])
    return pack_result
