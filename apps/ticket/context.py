# coding=utf-8
from calendar import HTMLCalendar
from datetime import date, datetime
from itertools import groupby
from django.conf import settings
try:
    import pytz
except ImportError:
    pytz = None



__author__ = 'alexy'


from django.utils.timezone import UTC


def next_month(origin_date):
    day = origin_date.day
    month = origin_date.month
    year = origin_date.year
    if origin_date.month == 12:
        return datetime(year + 1, 1, 1)
    else:
        return datetime(year, month+1, 1)

def travels(requst):
    # получаем значение текущего месяца
    utc = pytz.utc if pytz else UTC()
    if settings.USE_TZ:
        current = datetime.utcnow().replace(tzinfo=utc)
    else:
        current = datetime.now()
    date1 = next_month(current)
    date2 = next_month(date1)
    date3 = next_month(date2)
    date4 = next_month(date3)
    date5 = next_month(date4)
    monts1 = [date3, date4, date5]
    return {
        'months': [current, date1, date2],
        'months1': monts1
    }


class WorkoutCalendar(HTMLCalendar):

    def __init__(self, workouts):
        super(WorkoutCalendar, self).__init__()
        self.workouts = self.group_by_day(workouts)

    def formatday(self, day, weekday):
        if day != 0:
            cssclass = self.cssclasses[weekday]
            # if date.today() == date(self.year, self.month, day):
            #     cssclass += ' today'
            if day in self.workouts:
                cssclass += ' filled'
                # body = ['<ul>']
                # for workout in self.workouts[day]:
                #     body.append('<li>')
                #     body.append('<a href="%s">' % workout.id)
                #     body.append(workout.name)
                #     body.append('</a></li>')
                # body.append('</ul>')
                return self.day_cell(cssclass, '<a href="/admin/ticket/sale/?travel_start__day=%d&travel_start__month=%d&travel_start__year=%d">%d</a>' % (day, self.month, self.year, day))
            return self.day_cell(cssclass, day)
        return self.day_cell('noday', '&nbsp;')

    def formatmonth(self, year, month):
        self.year, self.month = year, month
        return super(WorkoutCalendar, self).formatmonth(year, month)

    def group_by_day(self, workouts):
        field = lambda workout: workout.travel_start.day
        return dict(
            [(day, list(items)) for day, items in groupby(workouts, field)]
        )

    def day_cell(self, cssclass, body):
        return '<td class="%s">%s</td>' % (cssclass, body)