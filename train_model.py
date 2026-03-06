import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from feature_extractor import extract_features


# Load dataset
df = pd.read_csv("dataset/phishing_dataset.csv", header=None)

df.columns = ["url","label"]


# Clean labels
df["label"] = df["label"].astype(str)
df["label"] = df["label"].str.strip()
df["label"] = df["label"].str.lower()


# Convert labels to numbers
df["label"] = df["label"].map({
    "phishing": 1,
    "safe": 0
})


# Remove invalid rows
df = df.dropna(subset=["label"])


# Convert to integer
df["label"] = df["label"].astype(int)


# Extract features from URLs
features = df["url"].apply(lambda x: extract_features(x))

X = pd.DataFrame(features.tolist())
y = df["label"]


# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Train model
model = RandomForestClassifier(n_estimators=200)

model.fit(X_train, y_train)


# Save model
joblib.dump(model, "phishing_model.pkl")


print("Model trained successfully")
print("Dataset size:", len(df))
print("Labels:", y.unique())