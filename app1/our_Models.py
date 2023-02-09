
from collections import namedtuple

Employee = namedtuple(
    'Employee',
    'employ_id, first_name, last_name,email,phone_number,hire_date,job_id,salary,commission_pct,manager_id,department_id')

class ActorInMovie:
    def __init__(self, row):
        self.first_name = row[0]
        self.last_name = row[1]
        self.title  = row[2]
        self.release_year = row[3]
        self.length = row[4]
        