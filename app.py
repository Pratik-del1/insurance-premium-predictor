from fastapi import FastAPI
from fastapi.responses import JSONResponse 
from ML.schema.user_input import Userinput
from ML.model.predict import predict_output , model , Model_version
from ML.schema.prediction_response import PredictionResponse

app = FastAPI()

@app.get('/')
def home():
    return {'message' : 'Insurance Premium Prediction'}
    
@app.get('/health')
def health_check():
    return {
            'status' : 'OK' ,
            'Version' : Model_version ,
            'model_loaded' : model is not None 
        }

@app.post('/predict' , response_model = PredictionResponse)
def predict_premium(data : Userinput):

    user_input = {
        'bmi' : data.bmi ,  
        'age_group' : data.age_group , 
        'lifestyle_risk' : data.lifestyle_risk , 
        'city_tier' : data.city_tier , 
        'income_lpa' : data.income_lpa , 
        'occupation' :   data.occupation , 
        }
    

    try:

        prediction = predict_output(user_input)

        return JSONResponse(status_code = 200 , content = {'predicted_category' : prediction})
    
    except Exception as e:

        return JSONResponse(status_code = 500 , content = str(e))