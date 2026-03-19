# hotel-booking-cancellation-prediction-project-using-ML
Machine Learning Project to predict hotel booking cancellations using EDA,feature engineering, and model building.


#  Hotel Booking Cancellation Prediction using Machine Learning

##  Project Objective

The objective of this project is to build a machine learning model that predicts whether a hotel booking will be canceled or not. This helps hotels reduce revenue loss and improve planning by identifying potential cancellations in advance.

---

##  Dataset Used

* **Dataset Name:** Hotel Booking Demand Dataset
* **Source:** Kaggle
* **Link:** https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand

The dataset contains booking information such as lead time, customer type, room type, and cancellation status etc.

---

##  Models Used

The following machine learning models were used:

* **Logistic Regression**
  Used as a baseline model for binary classification.

* **Decision Tree Classifier**
  Helps understand decision rules and feature importance.

* **Random Forest Classifier**
  Chosen for better accuracy and handling of overfitting.

 **Why these models?**
These models are commonly used for classification problems and provide a balance between interpretability and performance.

---
##  Model Performance Comparison

The following machine learning models were trained and evaluated on the dataset:

1. Logistic Regression  
   - Accuracy: 80%  
   - F1 Score: 0.79  
   - Performance: Good baseline model, but struggles with complex patterns in data  

2. Decision Tree Classifier  
   - Accuracy: 82%  
   - F1 Score: 0.81  
   - Performance: Better than Logistic Regression, but prone to overfitting  

3. Random Forest Classifier  
   - Accuracy: 85%  
   - F1 Score: 0.84  
   - Performance: Best among all models with higher accuracy and better generalization  

---

##  Final Model Selection

The Random Forest Classifier was selected as the final model because it achieved the highest accuracy and F1 score among all models.

It reduces overfitting by combining multiple decision trees and provides better performance on complex datasets. Therefore, it is the most suitable model for predicting hotel booking cancellations.

---

##  Project Workflow

### 1. Data Collection

* Loaded dataset from CSV file

### 2. Data Preprocessing

* Handled missing values
* Removed irrelevant features
* Encoded categorical variables
* Feature scaling using StandardScaler

### 3. Exploratory Data Analysis (EDA)

* Analyzed booking trends
* Checked correlation between features
* Visualized important features like lead time and customer type

### 4. Model Building

* Split data into training and testing sets
* Trained multiple models

### 5. Model Evaluation

* Evaluated using accuracy, precision, recall, and F1-score

---

##  Key Results

The performance of different models was evaluated using multiple metrics such as Accuracy, F1 Score, and AUC Score.

### 🔹 Logistic Regression
- Accuracy: 80%
- F1 Score: 0.79
- AUC Score: 0.83

### 🔹 Decision Tree Classifier
- Accuracy: 82%
- F1 Score: 0.81
- AUC Score: 0.85

### 🔹 Random Forest Classifier
- Accuracy: 85%
- F1 Score: 0.84
- AUC Score: 0.88

---

##  Best Model

The **Random Forest Classifier** performed best among all models.

###  Outcome:
- Achieved highest accuracy and F1 score  
- Provided better generalization  
- Reduced overfitting compared to Decision Tree  

Therefore, Random Forest was selected as the final model for predicting hotel booking cancellations.
---


##  How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/hotel-booking-cancellation-prediction.git
```

### Step 2: Navigate to Project Folder

```bash
cd hotel-booking-cancellation-prediction
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python app.py
```

### Step 5: Open in Browser

Go to:

```
http://127.0.0.1:5000/
```

---

##  Conclusion

This project demonstrates how machine learning can be applied to predict hotel booking cancellations. The Random Forest model performed best, providing accurate predictions. This solution can help hotels reduce losses and improve customer management strategies.

---

##  References

* Kaggle Dataset: https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand
* Scikit-learn Documentation: https://scikit-learn.org
* Machine Learning Tutorials

---

