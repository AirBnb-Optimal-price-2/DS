from flask import Flask, request
import numpy as np 
from sklearn.linear_model import LinearRegression


def pred_airbnb():
    APP = Flask(__name__)
    
    @APP.route('/')
    def test():
        return "Air BnB Optimal Price Predictor"


# Put model in here. Unwrap objects here. Add and commit to DB here is needed
    @APP.route('/json', methods=['POST'])
    def test_json():
        req_data = request.get_json()

        one = req_data['one']
        two = req_data['two']
        three = req_data['three']
        four = req_data['four']
        five = req_data['five']
        mean = np.mean([one, two, five])
    
    # Example from sklearn LinearRegression() docs
        X = np.array([[one, one], [one, two], [two, two], [two, three]])
        y = np.dot(X, np.array([one, two])) + three
        reg = LinearRegression().fit(X, y)
        score = reg.score(X, y)
        predict = reg.predict(np.array([[three, five]]))

        return f"""You have successfully extracted {five/one} items the JSON object.
        \nThree mutiplied by four is {three *four}\n 
    
        Using numpy test {mean, 2}
    
        \n Linear Regression Prediction: {predict}


        {score} <== score
        """
    return APP
