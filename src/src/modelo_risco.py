import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def treinar_modelo(df):

    features = ["IEG", "IPP", "IPS", "IAA", "IAN"]

    df_model = df[features + ["risco"]].dropna()

    X = df_model[features]
    y = df_model["risco"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train, y_train)

    return model