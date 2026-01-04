import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load data
df = pd.read_csv("obesity_prediction.csv")

# Feature engineering (reuse from EDA)
df["BMI"] = df["Weight"] / (df["Height"] ** 2)

# Select features and target
X = df[["BMI", "Age", "Gender"]]
y = df["Obesity"]

print("X shape:", X.shape)
print("y shape:", y.shape)
# One-hot encode categorical features
X_encoded = pd.get_dummies(X, columns=["Gender"], drop_first=True)

print("Encoded X shape:", X_encoded.shape)
print("Encoded columns:", list(X_encoded.columns))



# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded,
    y,
    test_size=0.2,
    random_state=42
)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)



# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", round(accuracy, 3))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
