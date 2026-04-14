from typing import List, Dict, Optional,Annotated
from  pydantic import BaseModel, EmailStr,AnyUrl,Field


patient_info={'name':'Nitishh','age':30, 'email':'xyz@gmail.com','height': 75.2, 'contact_details':{'phone':'2353462'},'profile_url': 'https://www.github.com/redhead-coffee'}

class patient(BaseModel):
    #name:str =Field(max_length=7) #without Annotated
    name:Annotated[str,Field(max_length=7,title= "Name", description="Enter Name",examples= ['modi','trump'])] #adding metaData using Annotated
    email: EmailStr #emailStr
    age:int =Field(gt=18, le=90) #more constraints gt,ge (greater than,greate equal to) & lt,le(less than,less equal to)
    #height: float = Field(gt=0) #without Annotated
    height:Annotated[float,Field(gt=0,strict=True)] #restrict type incursion using strict (Annotated)
    #married: bool = False  #without Annotated
    married:Annotated[bool,Field(default=None,description='someone please fkin stop the warrr!!!')] #default values using Annotated
    #allergies: Optional[list[str]]=None #default value=None #without Annotated
    allergies: Annotated[Optional[list[str]],Field(default=None,max_length=5)] #with Annotated default value & max_length
    contact_details: Dict[str,str]
    profile_url: AnyUrl #anyUrl
    


def insert_data(patient: patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.height)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print(patient.profile_url)
    print('inserted')




patient1= patient(**patient_info)

insert_data(patient1)
