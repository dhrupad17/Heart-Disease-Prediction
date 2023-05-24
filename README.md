# Heart Disease Prediction

This is a web application component built with Streamlit that allows users to predict the presence of heart disease. The application utilizes a machine learning model trained on a heart disease dataset to provide accurate predictions based on user input.

## About the Project

This machine learning project focuses on predicting the presence of heart disease in individuals based on various medical attributes. The project utilizes a dataset containing information about patients and their heart health, and employs a predictive model to classify individuals as having heart disease or not.

- ### Dataset
The heart disease prediction model is trained on the [Heart Disease dataset](https://github.com/dhrupad17/Heart-Disease-Prediction/blob/main/heart_disease_data.csv) obtained from the UCI Machine Learning Repository. This dataset consists of 303 instances, with each instance containing 14 attributes such as age, sex, chest pain type, cholesterol level, and more. The target variable indicates the presence or absence of heart disease.

- ### Methodology
   - Data Preprocessing: The dataset is preprocessed by handling missing values, encoding categorical variables, and performing feature scaling if necessary.
   - Feature Selection: Relevant features are selected to train the prediction model. This step involves exploring correlations, conducting statistical analyses, or      employing feature importance techniques.
   - Model Selection and Training: Machine learning algorithm such as logistic regression is used to train on the preprocessed dataset to create a predictive model.
   - Model Evaluation: The trained model is evaluated using appropriate evaluation metrics such as accuracy, precision, recall, and F1-score. Cross-validation            techniques may be employed to assess the model's generalization performance.
   - Hyperparameter Tuning: If necessary, hyperparameter tuning techniques such as grid search or random search are utilized to optimize the model's performance by        fine-tuning the hyperparameters.
   - Deployment: The final trained model is deployed in a user-friendly web application using Streamlit, allowing users to input their attributes and receive a           prediction regarding the presence of heart disease.

- ### Features
  - Users can input their attributes such as age, sex, chest pain type, resting blood pressure, cholesterol level, and more into the web application.
  - The application employs the trained model to predict the likelihood of heart disease based on the provided information.
  - The prediction result is displayed, indicating whether the individual is likely to have heart disease or not.

## Website OverView:-

### ```Click Here to Visit the Website 👉``` [Tap to Diagonise](https://dhrupad17-heart-disease-prediction-app-9n6wv2.streamlit.app/)


