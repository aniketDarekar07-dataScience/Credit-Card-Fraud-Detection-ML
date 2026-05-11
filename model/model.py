import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def load_model():
    df = pd.read_csv("data/fraud.csv")
    X = df.drop("Fraud", axis=1)
    y = df["Fraud"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    return model, X_test, y_test

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    return accuracy_score(y_test, preds) * 100
