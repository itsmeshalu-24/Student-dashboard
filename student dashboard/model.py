import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pickle

# Load data
df = pd.read_csv("students.csv")

# Features & target
X = df[['sessions_attended','avg_time_spent','last_activity_days','quiz_score']]
y = df['is_active']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline (scaling + balanced model)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(class_weight='balanced', max_iter=1000))
])

# Train
pipeline.fit(X_train, y_train)

# Accuracy
print("Accuracy:", pipeline.score(X_test, y_test))

# Save model
pickle.dump(pipeline, open("model.pkl", "wb"))