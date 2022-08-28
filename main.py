import os
import datetime

from configparser import ConfigParser
from datetime import timedelta

config = ConfigParser()
config.read('sample.ini') # maybe change this to be the value from args

def print_tasks(value):
  print(value)
  print('__________________________________\n')
  for key in config[value]:
    print(' - ' + config[value][key] + '\n')
  print('\n')

def main():
  current_date = datetime.datetime.now()
  current_week_num = current_date.strftime("%W")
  current_month = current_date.date().month
  current_year = current_date.date().year

  one_week_later = current_date + timedelta(days=7)
  one_week_later_month = one_week_later.date().month()
  one_week_later_year = one_week_later.date().year()

  print_tasks('weekly')

  # if the week number is even, print the bi-weekly tasks
  if int(current_week_num) + 1 % 2 == 0:
    print_tasks('biweekly')

  if current_month < one_week_later_month or \
     one_week_later_year > current_year:
    print_tasks('monthly')

  if one_week_later_month % 3 == 0:
    print_tasks('quarterly')

  if one_week_later_month % 6 == 0:
    print_tasks('biannually')

  if one_week_later_month % 12 == 0:
    print_tasks('annually')

if __name__ == '__main__':
  #main()
  print_tasks('weekly')
