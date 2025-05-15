#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self,name = 'Ray',job = 'ITC'):
        self.name = name
        self.job = job
        pass

    @property
    def name(self):
        return self._name.title()
    
    @name.setter
    def name(self,name):
        if isinstance (name,str) and 1 <= len(name) <= 25:
            self._name = name
        
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job
    
    @job.setter
    def job(self,job):
        if isinstance (job,str) and job in APPROVED_JOBS:
            self._job = job
        
        else:
            print( "Job must be in list of approved jobs.")

    pass
