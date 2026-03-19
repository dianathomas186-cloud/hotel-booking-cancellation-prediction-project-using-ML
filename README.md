# hotel-booking-cancellation-prediction-project-using-ML
Machine Learning Project to predict hotel booking cancellations using EDA,feature engineering, and model building.
# Hotel Booking Cancellation Prediction Using Machine Learning

## Project Overview
Hotel booking cancellations cause significant revenue loss and operational challenges for hotels. This project uses machine learning to predict whether a hotel booking will be canceled based on historical booking and customer data. Predicting cancellations helps hotels optimize resources, reduce revenue loss, and improve customer service.

## Objective
- Build a machine learning model to predict hotel booking cancellations.  
- Analyze historical booking data to identify factors influencing cancellations.  
- Deploy a model to assist hotel management in decision-making.

## Dataset
- **Name:** Hotel Booking Demand Dataset  
- **Source:** [Kaggle - Hotel Booking Demand Dataset](https://www.kaggle.com/jessemostipak/hotel-booking-demand)  
- **Format:** CSV (`hotel-bookings.csv`)  
- **Target Variable:** `is_canceled`  
- **Features Include:** `hotel`, `lead_time`, `adults`, `children`, `country`, `meal`, `customer_type`, `adr`, etc.  

## Models Used
| Model | Reason |
|-------|--------|
| Logistic Regression | Baseline classification model |
| Decision Tree | Handles non-linear relationships |
| Random Forest | Ensemble model with high accuracy and robustness |

**Best Model:** Random Forest (after hyperparameter tuning)

## Key Steps
1. **Exploratory Data Analysis (EDA)**  
   - Count plots, pie charts, bar plots, KDE plots, pairplots, correlation heatmap.  
   - Identified features influencing cancellations.  

2. **Data Preprocessing**  
   - Handled missing values and dropped irrelevant columns.  
   - Encoded categorical features with LabelEncoder.  
   - Scaled numeric features using StandardScaler.  

3. **Model Building & Evaluation**  
   - Split data: 80% training, 20% testing.  
   - Evaluated models using Accuracy, Classification Report, Confusion Matrix, ROC-AUC.  

4. **Hyperparameter Tuning**  
   - Used GridSearchCV for Random Forest optimization.  
   - Achieved best performance with tuned Random Forest.  

5. **Model Deployment**  
   - Saved model (`hotel_booking_model.pkl`) and scaler (`scaler.pkl`) in the `models` folder.  
   - Integrated model into Flask app (`app.py`) for real-time predictions.  

## Key Results
- **Random Forest Accuracy:** ~0.87  
- **ROC-AUC Score:** ~0.88  
- Random Forest outperformed other models.  
- Insight: Longer lead times, city hotels, and certain customer types have higher cancellation rates.  

## Folder Structure

Hotel_Booking_Cancellation_Prediction/
│
├── models/
│   ├── hotel_booking_model.pkl
│   └── scaler.pkl
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   └── index.html
│
├── hotel-bookings.csv
├── hotel_booking_project.ipynb
├── app.py
├── README.md
├── requirements.txt  
│
├── images/              
│   └── bg.jpg
│
├── model.py            
│
└── .gitattributes       

## How to Run

1. Install required packages:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn flask

2. Run the Flask application:
python app.py

3. Open your browser and go to:
http://127.0.0.1:5000
Use the web interface to make predictions.

**##Conclusion**

- The project successfully predicts hotel booking cancellations using machine learning.  
- Random Forest is the best-performing model.  
- Hotels can use this model to anticipate cancellations and improve booking strategies.  

**## References**
1. Kaggle - Hotel Booking Demand Dataset  
2. Scikit-learn Documentation  
3. Pandas Documentation  
4. Seaborn Visualization Library  
