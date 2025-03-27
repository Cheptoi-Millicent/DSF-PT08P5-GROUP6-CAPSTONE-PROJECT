from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model
# model = joblib.load("models/random_forest_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

# Dropdown options
occupation_categories = ["Employed", "Self-Employed", "Unemployed", "Student"]
business_industries = ["Finance", "Healthcare", "Education", "Technology", "Retail", "Other"]
employment_status_options = ["Full-Time", "Part-Time", "Unemployed", "Retired"]
loan_purposes = ["Personal", "Business", "Education", "Medical", "Other"]
account_types = ["Savings", "Checking", "Current"]
crb_grades = ["A", "B", "C", "D", "E"]
marital_status_options = ["Single", "Married", "Divorced", "Widowed"]
gender_options = ["Male", "Female", "Other"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Get form data
            form_data = request.form

            # Convert input data into correct format
            input_data = [
                form_data["Occupation_Professional_Category"],
                int(form_data["Number_of_Days_in_Debit"]),
                form_data["Gender"],
                form_data["Own_Rent_Home"],
                form_data["Type_of_Business_Industry_of_Employment"],
                int(form_data["Key"]),
                int(form_data["CRB_Score"]),
                int(form_data["Time_at_Current_Employment"]),
                int(form_data["Number_of_Cheque_Debit_Transactions"]),
                int(form_data["Number_of_ATM_Deposits"]),
                int(form_data["Age_at_Application"]),
                int(form_data["Number_of_Dependents"]),
                int(form_data["Number_of_Over_the_Counter_withdrawals"]),
                float(form_data["Monthly_Income"]),
                float(form_data["Minimum_End_of_Day_Balance"]),
                float(form_data["Average_Balance"]),
                float(form_data["Sum_of_Monthly_Debit_Transactions"]),
                float(form_data["Sum_of_Monthly_Credit_Transactions"]),
                int(form_data["Number_of_Debit_Card_POS_Transactions"]),
                float(form_data["Maximum_End_of_Day_Balance"]),
                int(form_data["Government_Employee"]),
                form_data["Account_Type"],
                form_data["CRB_Grade"],
                form_data["Loan_Purpose"],
                int(form_data["Number_of_ATM_Withdrawals"]),
                form_data["Marital_Status"],
                float(form_data["Total_Loan_Amount"]),
                int(form_data["Number_of_Days_in_Credit"]),
                int(form_data["Number_of_Joint_Holders"]),
                int(form_data["Loan_Term"]),
                form_data["Employment_Status"],
                float(form_data["Overdraft_Limit"]),
                int(form_data["Number_of_Bounced_Cheques"]),
            ]

            # Convert categorical variables to numerical values if necessary
            # (You need to ensure that your model was trained with encoded categorical values)

            # # Convert to numpy array
            # input_array = np.array(input_data).reshape(1, -1)


            # # Make prediction
            # prediction = model.predict(input_array)[0]
            # Convert to DataFrame
            input_df = pd.DataFrame([input_data])

            # Ensure column order
            input_df = input_df[preprocessor.feature_names_in_]

            # Preprocess input
            processed_input = preprocessor.transform(input_df)

            # Predict
            prediction = model.predict(processed_input)

            # Convert prediction to human-readable format
            result = "Default" if prediction == 1 else "No Default"

            return render_template("index.html", result=result)

        except Exception as e:
            return render_template("index.html", result="Error: " + str(e))

    return render_template(
        "index.html",
        occupation_categories=occupation_categories,
        business_industries=business_industries,
        employment_status_options=employment_status_options,
        loan_purposes=loan_purposes,
        account_types=account_types,
        crb_grades=crb_grades,
        marital_status_options=marital_status_options,
        gender_options=gender_options,
    )

if __name__ == "__main__":
    app.run(debug=True)
