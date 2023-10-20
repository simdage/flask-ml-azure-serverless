# Step 1: Import the necessary libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib


# Step 2: Load the Iris dataset
iris = datasets.load_iris()
X = iris.data  # Features
y = iris.target  # Target (labels)

# Step 3: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Choose a classifier (e.g., Decision Tree)
classifier = DecisionTreeClassifier()

# Step 5: Train the classifier on the training data
classifier.fit(X_train, y_train)

# Step 6: Make predictions on the testing data
y_pred = classifier.predict(X_test)

# Step 7: Evaluate the classifier's performance (e.g., accuracy)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

joblib.dump(classifier, "iris_prediction.joblib")
