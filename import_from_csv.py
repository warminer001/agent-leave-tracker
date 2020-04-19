import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AgentLeaveTracker.settings')

import django
django.setup()

from django.db import models
from alt.models import UserModel
import csv
from datetime import datetime
from dateutil.parser import parse 

def import_to_db():
    with open('Book1.csv') as f:
        emp = csv.reader(f)
        next(emp)
        for e in emp:
            add_user = UserModel()
            print(f'Adding Employee {e[0]}...')
            add_user.employee_id = e[0]
            add_user.employee_iex_id = e[1]
            add_user.employee_name = e[2]
            add_user.employee_wave = e[3]
            add_user.employee_team_leader = e[4]
            add_user.employee_manager = e[5]
            add_user.employee_hire_date = e[6]
            add_user.save()
            

if __name__ == '__main__':
    import_to_db()
    print('Done')
