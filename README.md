# DS

# **AIR BNB Price Optimizer**

A webb app for predicting price of an Air BNB dependant on user inputs.

---
# **Datasets**
The data used was scraped on November 7, 2018 and contained detailed listing data, review data, and calendar data of current lisintgs in Berlin

The data that was used for the model can be found [here](https://www.kaggle.com/brittabettendorf/berlin-airbnb-data#listings.csv).

---

# **How to Use**

[Homepage](https://pred-airbnb.herokuapp.com/): This is the landing page for the pred-airbnb web app.

#### Using JSON:
Currently in test mode and only accepting the following:

#### **input**: 

`{
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 6
}`

#### **Expected test output**:
`You have successfully extracted 6.0 items the JSON object.
Three mutiplied by four is 12
Using numpy test (3.0, 2)
Linear Regression Prediction: [18.]
1.0 <== score`


----

# **Dependencies**

-[Flask](https://flask.palletsprojects.com/en/1.1.x/#)

---

# **License**

[MIT License](https://opensource.org/licenses/MIT)

---
