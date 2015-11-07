# coding=utf-8
from django import template
from apps.ticket.context import WorkoutCalendar
from apps.ticket.models import Ticket

register = template.Library()

@register.simple_tag
def calendar(year, month):
  my_workouts = Ticket.objects.order_by('travel_start').filter(
    travel_start__year=year, travel_start__month=month
  )
  cal = WorkoutCalendar(my_workouts).formatmonth(year, month)
  return cal