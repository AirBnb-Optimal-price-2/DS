<div align="center">
  <img src="https://github.com/AirBnb-Optimal-price-2/DS/blob/master/header/airplane.jpg"><br>
</div>

# **AIR BNB Price Optimizer**

A webb app for predicting price of an Air BNB dependant on user inputs. Currently using a test Linear Regression model to test.

---
# **Datasets**
The data used was scraped on November 7, 2018 and contained detailed listing data, review data, and calendar data of current lisintgs in Berlin

The data used for the model can be found [here](https://www.kaggle.com/brittabettendorf/berlin-airbnb-data#listings.csv).

The data that was cleaned and filtered can be found [here](https://github.com/AirBnb-Optimal-price-2/DS/tree/master/Data_analysis_visualisation)

---

# **How to Use**

[Homepage](https://pred-airbnb.herokuapp.com/): This is the landing page for the pred-airbnb web app.

#### Using JSON: https://pred-airbnb.herokuapp.com/json
Currently in test mode and only accepting the following:

#### **input**: 

`{
   "neighborhood": 1,
   "room-type": 15,
   "bedroom": 3,
   "bathroom": 2.5,
   "minimun_nights": 3,
   "description": "It's a 3 bedroom apartment"
}`

#### **Expected test output**:
`{
    "hood": 1,
    "lavatory": 2.5,
    "live": 15,
    "sleep": 3
}`


----

# **Dependencies**

-[Flask](https://flask.palletsprojects.com/en/1.1.x/#)
-[Green Unicorn](https://gunicorn.org/)


---

# **License**

[MIT License](https://opensource.org/licenses/MIT)

---
