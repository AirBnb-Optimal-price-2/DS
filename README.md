<div align="center">
  <img src="https://github.com/AirBnb-Optimal-price-2/DS/blob/master/header/airplane.jpg"><br>
</div>

# **AIR BNB Price Optimizer**

A webb app for predicting price of an Air BNB dependant on user inputs. Currently using a test Linear Regression model to test.

---
# **Datasets**
The data used was scraped on November 7, 2018 and contained detailed listing data, review data, and calendar data of current lisintgs in Berlin

The data used for the model can be found [here](https://www.kaggle.com/brittabettendorf/berlin-airbnb-data#listings.csv).

---

# **How to Use**

[Homepage](https://pred-airbnb.herokuapp.com/): This is the landing page for the pred-airbnb web app.

#### Using JSON: https://pred-airbnb.herokuapp.com/json
Currently in test mode and only accepting the following:

#### **input**: 

`{
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5
}`

#### **Expected test output**:
`{
    "price": 15.999999999999996,
    "score": 1.0
}`


----

# **Dependencies**

-[Flask](https://flask.palletsprojects.com/en/1.1.x/#)

---

# **License**

[MIT License](https://opensource.org/licenses/MIT)

---
