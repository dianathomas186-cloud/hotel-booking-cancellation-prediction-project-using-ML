# hotel-booking-cancellation-prediction-project-using-ML
Machine Learning Project to predict hotel booking cancellations using EDA,feature engineering, and model building.


#  Hotel Booking Cancellation Prediction using Machine Learning

---

##  Project Title

**Hotel Booking Cancellation Prediction using Machine Learning**

---

##  Objective

The objective of this project is to build a Machine Learning model that can predict whether a hotel booking will be canceled or not. This helps hotels reduce losses and make better decisions.

---

##  Dataset Used

* **Dataset Name:** Hotel Booking Demand Dataset
* **Source:** Kaggle
* **Link:** https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand

### Description:

The dataset contains booking information such as:

* Lead Time
* Arrival Date
* Customer Type
* Deposit Type
* Booking Status (Canceled / Not Canceled)

---

##  Models Used

### 1. Logistic Regression

* Used as a baseline model
* Simple and efficient for classification

### 2. Decision Tree

* Easy to understand and visualize
* Handles non-linear relationships

### 3. Random Forest (Best Performing Model)

* Reduces overfitting
* Provides better accuracy compared to other models

---

##  Key Results

* **Best Model:** Random Forest
* **Accuracy:** 85% (approx)
* **F1 Score:** 0.82 (approx)

### Key Factors Affecting Cancellation:

* Lead Time
* Deposit Type
* Customer Type

---

##  Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Flask

---


##  How to Run the Project

### Step 1: Clone the Repository

```
git clone https://github.com/dianathomas186-cloud/hotel-booking-cancellation-prediction-project-using-ML
```

### Step 2: Navigate to Project Folder

```
cd hotel-booking-cancellation-prediction-project-using-ML
```

### Step 3: Install Required Libraries

```
pip install -r requirements.txt
```

### Step 4: Run the Application

```
python app.py
```

### Step 5: Open in Browser

```
http://127.0.0.1:5000/
```

---

##  Output

The system takes user input and predicts whether a hotel booking is likely to be canceled or not.

---

##  Conclusion

This project successfully uses Machine Learning to predict hotel booking cancellations. Among all models, Random Forest performed the best with higher accuracy. This model can help hotels minimize cancellations and improve revenue management.

---

##  References

* https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand
* https://scikit-learn.org/
* https://docs.python.org/

---

