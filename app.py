import streamlit as st
import pandas as pd
import joblib

# Load the model
Model = joblib.load("random_forest_pipeline.pkl")


def predict(gender, own_car, own_realty, children, income, income_type, education,
            family_status, housing, work_phone, phone, email,
            occupation, family_members, age, years_employed): 
    # Prepare data for prediction
    client_data = pd.DataFrame({
        'CODE_GENDER': [gender],
        'FLAG_OWN_CAR': [own_car],
        'FLAG_OWN_REALTY': [own_realty],
        'CNT_CHILDREN': [children],
        'AMT_INCOME_TOTAL': [income],
        'NAME_INCOME_TYPE': [income_type],
        'NAME_EDUCATION_TYPE': [education],
        'NAME_FAMILY_STATUS': [family_status],
        'NAME_HOUSING_TYPE': [housing],
        'FLAG_WORK_PHONE': [work_phone],
        'FLAG_PHONE': [phone],
        'FLAG_EMAIL': [email],
        'OCCUPATION_TYPE': [occupation],
        'CNT_FAM_MEMBERS': [family_members],
        'AGE': [age],
        'YEAR_EMPLOYED': [years_employed]
    })
    
    # Predict the result using the model
    result = Model.predict(client_data)[0]
    return result


def main():
    # Streamlit App Title
    st.title("Credit Card Risk Assessment")

    # User input form
    st.header("Enter Client Details")
    gender = st.selectbox("Gender", ["M", "F"])
    own_car = st.selectbox("Owns Car?", ["Y", "N"])
    own_realty = st.selectbox("Owns Realty?", ["Y", "N"])
    children = st.number_input("Number of Children", min_value=0, step=1)
    income = st.number_input("Income", min_value=0.0, step=0.1)

    income_type = st.selectbox("Income Type", ['Working', 'Commercial associate', 'State servant', 'Student'])
    
    education = st.selectbox("Education Level", ['Higher education', 'Secondary / secondary special',
       'Incomplete higher', 'Lower secondary', 'Academic degree'])
    
    family_status = st.selectbox("Family Status", ['Civil marriage', 'Married', 'Single / not married', 'Separated','Widow'])
    
    housing = st.selectbox("Housing Type", ['Rented apartment', 'House / apartment', 'Municipal apartment','With parents', 'Co-op apartment', 'Office apartment'])
    
    work_phone = st.selectbox("Has Work Phone?", ["Yes", "No"])
    phone = st.selectbox("Has Phone?", ["Yes", "No"])
    email = st.selectbox("Has Email?", ["Yes", "No"])
    
    occupation = st.selectbox(
        "Occupation",
        [
            'Others', 'Security staff', 'Sales staff', 'Accountants',
            'Laborers', 'Managers', 'Drivers', 'Core staff',
            'High skill tech staff', 'Cleaning staff', 'Private service staff',
            'Cooking staff', 'Low-skill Laborers', 'Medicine staff',
            'Secretaries', 'Waiters/barmen staff', 'HR staff', 'Realty agents',
            'IT staff'
        ]
    )
    
    family_members = st.number_input("Number of Family Members", min_value=1.0, step=0.1)
    age = st.number_input("Age", min_value=18.0, step=1.0)
    years_employed = st.number_input("Years Employed", min_value=0.0, step=0.1)



    income = np.log(income)
    # Convert "Yes"/"No" to 1/0
    work_phone = 1 if work_phone == "Yes" else 0
    phone = 1 if phone == "Yes" else 0
    email = 1 if email == "Yes" else 0


    

    # Prediction button
    if st.button("Predict"):
        # Call the predict function
        result = predict(gender, own_car, own_realty, children, income, income_type, education,
                         family_status, housing, work_phone, phone, email,
                         occupation, family_members, age, years_employed)
        
        # Display the result
        list_res = ["High Risk", "Low Risk"]
        st.text(f"Your Debt is {list_res[result]}")


if __name__ == '__main__':
    main()
