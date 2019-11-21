from flask import Flask, request
import tensorflow as tf


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
        accom = req_data['accomodates']
        bed = req_data['bedrooms']
        bath = req_data['bathrooms']
        room = req_data['room_type']
        wifi = req_data['wifi']
        tv = req_data['tv']
        laptop = req_data['Laptop_friendly_workspace']
        family = req_data['family_kid_friendly']
        smoke = req_data['smoking_allowed']
        min_night = req_data['minimum_nights']
        ex_ppl = req_data['extra_people']
        clean = req_data['cleaning_fee']
        
        z = [clean, accom, min_night, bed, bath, neighbor, room, ex_ppl, laptop, tv, wifi, family, smoke]
        model1 = tf.keras.models.load_model('model.h5')
        pred = model1.predict([[z]])
        # pred = model1.predict([clean, accom, min_night, bed, bath, neighbor, room, ex_ppl, laptop, tv, wifi, family, smoke])
        return {'optimal_price': round(float(pred[0][0]), 2)}
    
    return APP
