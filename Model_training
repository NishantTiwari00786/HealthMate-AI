
# Import necessary libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Initialize the Random Forest model
rf_model = RandomForestClassifier(random_state=42)

# Train the model using the training data
rf_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the trained model to a file
joblib.dump(rf_model, 'at-home-doctor.pkl')

# Check feature importance
feature_importances = rf_model.feature_importances_
for feature, importance in zip(symptom_columns, feature_importances):
    print(f"{feature}: {importance:.4f}")
