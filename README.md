# **AIR BNB Price Optimizer**

A prediction model that helps you determine the best price to pay based on key features. Find our model [here](https://github.com/AirBnb-Optimal-price-2/Models/blob/master/Models/Notebooks/MLP.ipynb)

<div align="center">
  <img src="https://github.com/AirBnb-Optimal-price-2/DS/blob/master/header/heatmap.png"><br>
</div>


---
# **Datasets**
The data used was scraped on November 7, 2018 and contained detailed listing data, review data, and calendar data of current lisintgs in Berlin

The data used for the model can be found [here](https://www.kaggle.com/brittabettendorf/berlin-airbnb-data#listings.csv).

The data that was cleaned and filtered can be found [here](https://github.com/AirBnb-Optimal-price-2/Models/tree/master/Models)

---

# **How to Use**

Find our Flask API [here](https://github.com/AirBnb-Optimal-price-2/DS/tree/master/pred-airbnb)

[Homepage](https://pred-airbnb.herokuapp.com/): This is the landing page for the pred-airbnb web app.

#### Using JSON: https://pred-airbnb.herokuapp.com/json

#### **input**: 

`{
  "cleaning_fee": 30.0,
  "accomodates": 3,
  "minimum_nights": 4,
  "bedrooms": 1,
  "bathrooms": 1,
  "neighborhood": 1,
  "room_type": 15,
  "extra_people": 28,
  "Laptop_friendly_workspace": 1,
  "tv": 1,
  "wifi": 1,
  "family_kid_friendly": 1,
  "smoking_allowed": 0
}`

#### **Expected test output**:
`{
    "optimal_price": 74.08
}`


----

# **Dependencies**

- [Flask](https://flask.palletsprojects.com/en/1.1.x/#)
- [Green Unicorn](https://gunicorn.org/)
- [Tensorflow](https://www.tensorflow.org/api_docs/python/tf)


---

# **License**

[MIT License](https://opensource.org/licenses/MIT)

---

# **Additional Visuals**

Find visuals like these and many others that help explain the data in meaningful ways [here](https://github.com/AirBnb-Optimal-price-2/DS/blob/master/Data_analysis_visualisation/Unit3_build_airbnb_visualisation.ipynb)

<div align="center">
  <img src="https://github.com/AirBnb-Optimal-price-2/DS/blob/master/header/location:price.png"><br>
</div>
