import numpy as np
import pandas as pd
from joblib import load

model = load('diabetes_model.joblib')
def Predict(inputs):
    input_data = np.array(inputs).reshape(1, -1)  

    feature_names = [
        'Pregnancies',
        'Glucose',
        'BloodPressure',
        'SkinThickness',
        'Insulin',
        'BMI',
        'DiabetesPedigreeFunction',
        'Age'
    ]

    input_data_df = pd.DataFrame(input_data, columns=feature_names)
    probabilities = model.predict_proba(input_data_df)
    predicted_class = model.predict(input_data_df)

    return predicted_class[0], probabilities[0]
