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

        neighbor = req_data['neighborhood']
        room = req_data['room-type']
        bed = req_data['bedroom']
        bath = req_data['bathroom']
        min_night = req_data['minimum_nights']
        descript = req_data['description']
    
    # Example from sklearn LinearRegression() docs
       # X = np.array([[one, one], [one, two], [two, two], [two, three]])
       # y = np.dot(X, np.array([one, two])) + three
       # reg = LinearRegression().fit(X, y)
       # score = reg.score(X, y)
       # predict = reg.predict(np.array([[three, five]]))

        # return {'price': predict[0], 'score': score}
        return {'hood': neighbor, 'live': room, 'sleep': bed, 'lavatory': bath}
    

    return APP
