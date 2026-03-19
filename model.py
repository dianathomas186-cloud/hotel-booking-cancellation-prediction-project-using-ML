# model.py
# Hotel Booking Cancellation Prediction - Model Training and Saving

# 1. Import Libraries
import pandas as pd
import numpy as np
import os
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE

# 2. Load Dataset
df = pd.read_csv("hotel-bookings.csv")
print("Dataset loaded successfully!")
print("Shape:", df.shape)

# 3. Data Cleaning
df['children'] = df['children'].fillna(0)
df['country'] = df['country'].fillna(df['country'].mode()[0])
df['agent'] = df['agent'].fillna(0)
df['company'] = df['company'].fillna(0)

# Drop unnecessary columns
df.drop(['reservation_status_date','reservation_status'], axis=1, inplace=True)

# Drop any remaining missing values
df = df.dropna()

# 4. Encode Categorical Features
categorical_cols = df.select_dtypes(include='object').columns
encoder = LabelEncoder()

for col in categorical_cols:
    df[col] = encoder.fit_transform(df[col])

# 5. Select Important Features
features = ['hotel','lead_time','adults','children','previous_cancellations']
X = df[features]
y = df['is_canceled']

# 6. Balance Dataset using SMOTE
smote = SMOTE(random_state=42)
X_balanced, y_balanced = smote.fit_resample(X, y)

print("After balancing:")
print("Cancellations distribution:\n", pd.Series(y_balanced).value_counts())

# 7. Scale Features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_balanced)

# 8. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_balanced, test_size=0.2, random_state=42
)

# 9. Train Random Forest Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Evaluate Model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 10. Save Model and Scaler
if not os.path.exists("models"):
    os.makedirs("models")

with open("models/hotel_booking_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Model and scaler saved successfully!")