from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin_code:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address 


address_info={'city':'Bangalore','state':'Karnataka','pin_code':'560001'}

address1=Address(**address_info)

patient_dict={'name':'Nitishh','gender':'Male','age':67,'address':address1}

patient1=Patient(**patient_dict)

#XYZ = patient1.model_dump()

XYZ = patient1.model_dump(include={'name','age'}) # include={'name','age'} will give us a dictionary representation of the model, which is useful for serialization and data exchange purposes. We can use this dictionary to transmit the data over a network or store it in a file, and then we can deserialize it back into a Pydantic model when needed.

XYZ = patient1.model_dump(exclude={'gender': True, 'address': {'city': True}}) # exclude name, gender, and nested address.city from the output dictionary.

xYZ_nested = patient1.model_dump_json(exclude={'gender','address'}) # this will give us a JSON string representation of the model, which is useful for serialization and data exchange purposes. We can use this JSON string to transmit the data over a network or store it in a file, and then we can deserialize it back into a Pydantic model when needed. 

print(XYZ)
print(type(XYZ))

print(xYZ_nested)
print(type(xYZ_nested)) #this will give us a string representation of the JSON data.
