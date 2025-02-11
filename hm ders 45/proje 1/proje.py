import os
import csv
def red_employees(file_path) :
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row
            
def increase_salary(employess, precentage):
    return list(
        map(
            lambda emp: {**emp, "salary": int(emp["salary"]) * (1 + precentage / 100)},employess
        )
    )
    
def filter_by_age(employess, min_age):
    return list(filter(lambda emp: int(emp["age"]) > min_age, employess))

def department_average_salary(employess):
    departments = {}
    for emp in employess:
        dept = emp["department"]
        salary = int(emp["salary"])
        if dept not in departments:
            departments[dept] = {"total": 0, "count": 0}
        else:
            departments[dept]["total"] += salary
            departments[dept] =["count"] += 1
            
def get_average():