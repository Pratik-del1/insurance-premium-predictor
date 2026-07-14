from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel , Field , computed_field
from typing import Literal , Annotated
import pickle
import pandas as pd

with open('ML/model.pkl' , 'rb') as f:
    model = pickle.load(f)

app = FastAPI()

tier_1 = ['Chennai' , 'Delhi' , 'Mumbai' , 'Kolkata' , 'Pune' , 'Hyderabad' , 'Bangalore']
tier_2 = ['Jaipur' , 'Indore' , 'Kota' , 'Lucknow' , 'Chandigarh' , 'Jalandhar' , 'Mysore']

class Userinput(BaseModel):

    age : Annotated[int , Field(... , gt = 0 , lt = 120 , description= 'Age of the user')]
    weight: Annotated[float , Field(... , gt = 0 , description= 'Weight of the user')]
    height: Annotated[float , Field(... , gt = 0 , lt = 2.5 , description= 'Height of the user')]
    income_lpa: Annotated[float , Field(... , gt = 0 , description= 'Annual income of the user')]
    smoker: Annotated[bool , Field(..., description= 'Smoking status of the user')]
    city: Annotated[str , Field(... , description= 'City of the user')]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'] , Field(... , description= 'Age of the user')]
    
    @computed_field
    @property

    def city_tier(self) -> int:
        if self.city in tier_1:
            return 1
        elif self.city in tier_2:
            return 2
        else:
            return 3
        
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)
        
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return 'high risk'
        elif self.smoker or self.bmi > 27:
            return 'medium risk'
        else:
            return 'low risk'
        
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return 'young'
        elif self.age < 45:
            return 'adult'
        elif self.age < 60:
            return 'middle_aged'
        else:
            return 'senior'

@app.post('/predict')
def predict_premium(data : Userinput):

    input_df = pd.DataFrame([{
        'bmi' : data.bmi ,  
        'age_group' : data.age_group , 
        'lifestyle_risk' : data.lifestyle_risk , 
        'city_tier' : data.city_tier , 
        'income_lpa' : data.income_lpa , 
        'occupation' :   data.occupation , 
        }])
    
    prediction = model.predict(input_df)[0]

    return JSONResponse(status_code = 200 , content = {'predicted_category' : prediction})