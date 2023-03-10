# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the training and test datasets
train_data = pd.read_csv('internship_train.csv')
test_data = pd.read_csv('internship_hidden_test.csv')

# Separate the target variable from the training data
X_train = train_data.drop('target', axis=1)
y_train = train_data['target']

# Preprocess the data
numeric_features = X_train.select_dtypes(include=['int64', 'float64']).columns.tolist()
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_features = X_train.select_dtypes(include=['object']).columns.tolist()
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Fit the preprocessor on training data and transform training data
X_train_preprocessed = preprocessor.fit_transform(X_train)

# Transform test data using preprocessor
X_test_preprocessed = preprocessor.transform(test_data)

# Split the training data into training and validation sets
X_train_split, X_val_split, y_train_split, y_val_split = train_test_split(X_train_preprocessed, y_train, test_size=0.2, random_state=42)

# Define the regression model
model = Pipeline(steps=[
    ('regressor', LinearRegression())
])

# Fit the model to the training data
model.fit(X_train_split, y_train_split)

# Evaluate the model's performance on the validation data
y_val_pred = model.predict(X_val_split)
val_rmse = np.sqrt(mean_squared_error(y_val_split, y_val_pred))
print('Validation RMSE:', val_rmse)

# Use the trained model to predict the target variable for the test data
test_preds = model.predict(X_test_preprocessed)

# Save the predictions to a CSV file
submission_df = pd.DataFrame({
    'target': test_preds
})
submission_df.to_csv('internship_predictions.csv', index=False)
