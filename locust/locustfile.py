import time
import random
from locust import HttpUser, task, between

data = ({'gender':'male','married':'yes','dependents':'0','education':'graduate','self_employed':'no','applicant_income':'5849','coapplicant_income':'0','loan_amount':'128000','loan_amount_term':'360','credit_history':'1','property_area':'urban'},
        {'gender':'female','married':'yes','dependents':'1','education':'graduate','self_employed':'yes','applicant_income':'589','coapplicant_income':'99','loan_amount':'12000','loan_amount_term':'360','credit_history':'1','property_area':'rural'},
        {'gender':'male','married':'no','dependents':'2','education':'graduate','self_employed':'yes','applicant_income':'589','coapplicant_income':'100','loan_amount':'8000','loan_amount_term':'360','credit_history':'0','property_area':'semi-rural'},
        {'gender':'female','married':'no','dependents':'3','education':'graduate','self_employed':'no','applicant_income':'500849','coapplicant_income':'83720','loan_amount':'12800870','loan_amount_term':'360','credit_history':'0','property_area':'urban'})

class smartlender(HttpUser):
    
    @task
    def home(self):
        self.client.get("/")
        
    @task
    def predict(self):
        time.sleep(2)
        self.client.post("/predict.html",data = data[random.randint(0,3)])
        
    @task
    def submit(self):
        self.client.get("/submit")