# DSF-PT08P5-GROUP6-CAPSTONE-PROJECT
# Loan Default Prediction

## Overview
Loan default prediction is a crucial task for financial institutions to assess credit risk and minimize losses. This project aims to develop a machine learning model to predict the likelihood of a borrower defaulting on a loan, which is crucial for banks and financial institutions as it enables proactive risk management, reduces financial losses, and improves lending policies. The target audience includes banks and financial institutions, credit risk analysts, regulatory bodies, and fintech companies. The model can reduce bad debt and loan write-offs, improve lending policies by identifying high-risk applicants, and enhance customer profiling, leading to personalized lending solutions.

## Project Structure
```
Loan-Default-Prediction/
│-- data/                  # Contains raw and processed datasets
│-- Index.ipynb            # Jupyter notebook for exploratory data analysis (EDA) and modeling
│-- Deployable/            # Flask/FastAPI application for deployment
│-- README.md              # Project documentation
│-- Group 6 Proposal _Loan Default Prediction.docx
│-- Loan Default Prediction Model.docx
```

## Business Problem
In Kenya's evolving financial sector, both lenders and borrowers have considerable obstacles. Challenges encountered by lenders include elevated default rates, political and economic volatility, and corruption.

Borrowers face challenges include limited access to credit, high and variable interest rates, rigorous loan qualification criteria, and cultural and societal barriers, particularly impacting women. 

Loan default constitutes a substantial challenge within Kenya's financial sector, impacting the profitability and sustainability of lending institutions. The execution of governmental initiatives like the Hustler Fund underscores the necessity of addressing this issue. Launched in late 2022, the Hustler Fund aimed to provide accessible credit to Kenyan residents, offering loans at an annual interest rate of 8%. As of August 2023, more than 29% of the outstanding loan portfolio was classified as at-risk, with nearly 3 billion shillings in defaults, indicating a default rate nearly twice that of commercial banks.


## Data Sources
The dataset comprises multiple sources:
- **Application Data:** Demographics, employment details, and loan purpose.
- **Contract Data:** Loan amount, tenure, and type.
- **CRB Data:** Credit scores and risk grades.
- **ContractsSnapshotData** Monthly data of the loan status
- **Current and Savings Account Data** - Current and Savings information of the loan applicants

## Features Used
After data cleaning, we utilized the following features for prediction:
- **Occupation_Professional_Category**
- **Age_at_Application**
- **Loan_Term**
- **Employment_Status**
- **Type_of_Business_Industry_of_Employment**
- **Monthly_Income**
- **CRB Score**
- **Loan_Purpose**
- **Total_Loan_Amount**
- **Time_at_Current_Employment_(Months)**
- **CRB Grade**

## Methodology
1. **Data Collection & Cleaning** – Merging multiple datasets, handling missing values, and feature engineering.
2. **Exploratory Data Analysis (EDA)** – Understanding data distributions and correlations.
3. **Model Selection** – Using Logistic Regression, Random Forest, XGBoost, and Neural Networks.
4. **Model Training & Tuning** – Hyperparameter optimization for best performance.
5. **Evaluation** – Measuring accuracy, precision, recall, F1-score, and ROC-AUC.
6. **Deployment** – Developing a web app for real-time predictions using Flask/FastAPI.

## Installation
### Prerequisites
- Python 3.8+
- Jupyter Notebook
- Flask or FastAPI (for deployment)
- Pandas, NumPy, Scikit-learn, XGBoost
### Setup
```sh
# Clone the repository
git clone https://github.com/Cheptoi-Millicent/DSF-PT08P5-GROUP6-CAPSTONE-PROJECT.git
cd Loan-Default-Prediction

# Create a virtual environment
cd Deployable
python -m venv Loan-env
source Loan-env/bin/activate  # On Windows use `Loan-env\Scripts\activate`



## Running the Project
### Exploratory Data Analysis and Train Model
```sh
jupyter notebook /Index.ipynb
```

### Run Web App
```sh
python Deployable/main.py
```

## Model Performance
| Metric    | Value |
|-----------|-------|
| Accuracy  | 95%   |
| Precision | 47%   |
| Recall    | 100%  |
| F1-Score  | 64%   |


## Future Improvements
- Improve feature selection and engineering
- Experiment with deep learning models
- Deploy on AWS/GCP for scalability
- Integrate real-time data streams
- Address class imbalance better

## Contributors
- **Mercy Ayub** - [GitHub](https://github.com/mercy-gh)
- **Daniel Kithinji** - [GitHub](https://github.com/DanielKithinji)
- **Carol Woto** - [GitHub](https://github.com/CWoto)
- **Millicent Cheptoi** - [GitHub](https://github.com/Cheptoi-Millicent)
- **Reagan SAF** - [GitHub](https://github.com/iDeal-DataViz)
- **Jesse Gitobu** - [GitHub](https://github.com/JesseGitobu)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

For any queries or collaboration, feel free to reach out!