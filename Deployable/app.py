from flask import Flask, render_template, request
import pandas as pd
import joblib  # Import joblib for loading

app = Flask(__name__)

# Load the trained pipeline
model_pipeline = joblib.load("models/random_forest_model.pkl")

# Define your category mappings
occupation_categories = {
    'unknown': 0, 'Employee': 1, 'Clerical Support Worker': 2,
    'Professional': 3, 'Officer': 4, 'Semi-Professional': 5,
    'Service and Sales Worker': 6, 'Plant and Machine Operators': 7,
    'Armed Forces Occupation': 8, 'Elementary Occupation': 9,
    'Technician and Associate Professional': 10, 'Self Employed': 11,
    'Blue Collar': 12, 'Skilled Agricultural, Forestry': 13, 'Pensioner': 14
}

employment_status_categories = {
    'unknown': 0, 'Retired': 1, 'Part-Time': 2, 'Contract': 3,
    'Self Employed': 4, 'Full-Time': 5
}

crb_grade_categories = {'X': 0, 'E': 1, 'D': 2, 'C': 3, 'B': 4, 'A': 5}

loan_purpose_categories = {
    'unknown': 0, 'Other': 1, 'Education': 2,
    'Home Improvement': 3, 'Debt Consolidation': 4
}

business_industry_categories = {
    'Unknown': 0, 'Financial': 1, 'Civil Service': 2, 'Tourism': 3,
    'Education': 4, 'Energy, Electricity & Water': 5, 'Private Security Services': 6,
    'Manufacturing': 7, 'Mining & Quarrying': 8, 'Retailing': 9,
    'Construction & Installation': 10, 'Transportation & Communication': 11,
    'Micro & Small Enterprise': 12, 'Science & Technology': 13,
    'Business Process Outsourcing': 14, 'Professional & Other Services': 15,
    'Environment & Sustainable Dev.': 16, 'Agriculture': 17, 'Distribution': 18,
    'Retiree/Pensioner': 19, 'Other': 20
}

# Create inverse mappings for displaying category names
occupation_categories_inverse = {v: k for k, v in occupation_categories.items()}
employment_status_categories_inverse = {v: k for k, v in employment_status_categories.items()}
crb_grade_categories_inverse = {v: k for k, v in crb_grade_categories.items()}
loan_purpose_categories_inverse = {v: k for k, v in loan_purpose_categories.items()}
business_industry_categories_inverse = {v: k for k, v in business_industry_categories.items()}


@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get data from the form, handling potential errors
            occupation_category = int(request.form['occupation_category'])
            age = int(request.form['age'])
            loan_term = int(request.form['loan_term'])
            employment_status = int(request.form['employment_status'])
            business_industry = int(request.form['business_industry'])
            monthly_income = int(request.form['monthly_income'])
            crb_score = int(request.form['crb_score'])
            loan_purpose = int(request.form['loan_purpose'])
            total_loan_amount = int(request.form['total_loan_amount'])
            employment_length = int(request.form['employment_length'])
            crb_grade = int(request.form['crb_grade'])



            # Create a DataFrame from the input data
            new_data = pd.DataFrame({
                'Occupation_Professional_Category': [occupation_category],
                'Age_at_Application': [age],
                'Loan_Term': [loan_term],
                'Employment_Status': [employment_status],
                'Type_of_Business_Industry_of_Employment': [business_industry],
                'Monthly_Income': [monthly_income],
                'CRB Score': [crb_score],
                'Loan_Purpose': [loan_purpose],
                'Total_Loan_Amount': [total_loan_amount],
                'Time_at_Current_Employment_(Months)': [employment_length],
                'CRB Grade': [crb_grade]
            })

            # Ensure column names match your training data exactly (this is redundant, but good practice)
            new_data.columns = [
                'Occupation_Professional_Category',
                'Age_at_Application',
                'Loan_Term',
                'Employment_Status',
                'Type_of_Business_Industry_of_Employment',
                'Monthly_Income',
                'CRB Score',
                'Loan_Purpose',
                'Total_Loan_Amount',
                'Time_at_Current_Employment_(Months)',
                'CRB Grade'
            ]


            # Make the prediction
            
            predicted_class = model_pipeline.predict(new_data)[0]  # Access the first element of the array

            # Translate prediction to "Default" or "No Default"
            prediction_text = "Default" if predicted_class == 1 else "No Default"


            # Convert numerical values back to category names for display
            occupation_name = occupation_categories_inverse.get(occupation_category, 'Unknown') #Handles out-of-range values
            employment_status_name = employment_status_categories_inverse.get(employment_status, 'Unknown')
            crb_grade_name = crb_grade_categories_inverse.get(crb_grade, 'Unknown')
            loan_purpose_name = loan_purpose_categories_inverse.get(loan_purpose, 'Unknown')
            business_industry_name = business_industry_categories_inverse.get(business_industry, 'Unknown')


            # Return the prediction to the template
            return render_template('index.html',
                                   
                                   prediction_text=prediction_text, #Pass the translated text
                                   occupation_name=occupation_name,
                                   age=age,
                                   loan_term=loan_term,
                                   employment_status_name=employment_status_name,
                                   business_industry_name=business_industry_name,
                                   monthly_income=monthly_income,
                                   crb_score=crb_score,
                                   loan_purpose_name=loan_purpose_name,
                                   total_loan_amount=total_loan_amount,
                                   employment_length=employment_length,
                                   crb_grade_name=crb_grade_name,
                                   occupation_categories=occupation_categories,
                                   employment_status_categories=employment_status_categories,
                                   crb_grade_categories=crb_grade_categories,
                                   loan_purpose_categories=loan_purpose_categories,
                                   business_industry_categories=business_industry_categories)


        except Exception as e:
            return render_template('index.html', error=str(e),
                                   occupation_categories=occupation_categories,
                                   employment_status_categories=employment_status_categories,
                                   crb_grade_categories=crb_grade_categories,
                                   loan_purpose_categories=loan_purpose_categories,
                                   business_industry_categories=business_industry_categories)


    # If it's a GET request, just render the form
    return render_template('index.html',
                           occupation_categories=occupation_categories,
                           employment_status_categories=employment_status_categories,
                           crb_grade_categories=crb_grade_categories,
                           loan_purpose_categories=loan_purpose_categories,
                           business_industry_categories=business_industry_categories)


if __name__ == '__main__':
    app.run(debug=True)