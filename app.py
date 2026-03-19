from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load trained model
with open("models/hotel_booking_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load scaler
with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Home route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            # Get input values
            hotel = int(request.form.get("hotel"))
            lead_time = float(request.form.get("lead_time"))
            adults = int(request.form.get("adults"))
            children = int(request.form.get("children"))
            previous_cancellations = int(request.form.get("previous_cancellations"))

            # Prepare input data
            input_data = np.array([[hotel, lead_time, adults, children, previous_cancellations]])

            # Scale input
            input_scaled = scaler.transform(input_data)

            # Predict
            prediction = model.predict(input_scaled)[0]

            # Output message
            if prediction == 1:
                result = "Booking is likely to be CANCELLED."
            else:
                result = "Booking is likely to be COMPLETED."

            return render_template("index.html", result=result)

        except Exception as e:
            return render_template("index.html", result=f"Error: {str(e)}")

    # GET request → no result
    return render_template("index.html", result=None)


# Run app
if __name__ == "__main__":
    app.run(debug=True)