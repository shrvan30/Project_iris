from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Here Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# For Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Saved the model to file
with open("model/iris_model.pkl", "wb") as f:
    pickle.dump(clf, f)

print("Model trained and saved to model/iris_model.pkl")
