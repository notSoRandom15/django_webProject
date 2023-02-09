import csv
import psycopg2  

from sqlalchemy import true
from .our_Models import Employee, ActorInMovie

def get_employees(count = 10):
    data = []    
    toSkipFirstRow = true
    for emp in map(Employee._make, csv.reader(open(r"C:\python\IO\CSV\employees.csv", "r"))):
        if toSkipFirstRow: 
            toSkipFirstRow = False
            continue
        data.append(emp)                
        if count <= 0: break
        count -= 1
    return data

       
def get_actors(rows = 20):
    conn = psycopg2.connect("dbname=dvdrental user=hristo3 password=sa123")
    
    cursor = conn.cursor()

    query = f'''
    SELECT
        a.first_name, a.last_name, 
        f.title, f.release_year,f.length
    FROM actor as a
        inner join 	film_actor as fa
            on a.actor_id = fa.actor_id
        inner join film f
            on fa.film_id = f.film_id
    where f.length > 180
    limit {rows}
    '''

    cursor.execute(query)
    
    data = [ActorInMovie(row)
            for row in cursor.fetchall()]   
    
    return data