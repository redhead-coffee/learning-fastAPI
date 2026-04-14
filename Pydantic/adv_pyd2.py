from typing import List,Dict
from pydantic import BaseModel, EmailStr, Field, field_validator

patient_info={'name':'Nitishh','email':'bwumca22176@icic.com','age':30,'height': 75.2, 'contact_details':{'gmail':'xyz@gmail.com','phone':'2353462'}}

class patient(BaseModel):
    name:str
    email:EmailStr
    age:int
    height:float
    married:bool = False
    allergies:List[str]= None
    contact_details:Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icic.com']
        domain_name=value.split('@')[-1]


        if domain_name not in valid_domains:
            raise ValueError('Not a Valid Domain')
        return value
    #case:2--performing a Transformation using field_validator

    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()

    #---exploring before mode and after mode----This means validator runs before Pydantic converts type--(not int yet)   After validator passes, Pydantic converts to int.

    @field_validator('age',mode='before')
    @classmethod
    def validate_age(cls,value):
        if 0< value <100:
            return value
        else:
            raise ValueError('age should be in between 0 & 100')
    





def insert_data(patient:patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

patient2=patient(**patient_info)

insert_data(patient2)
