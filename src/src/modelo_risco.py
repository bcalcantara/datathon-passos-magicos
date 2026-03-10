import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score


def treinar_modelo(df: pd.DataFrame):
    df = df.copy()

    # definição de risco exatamente como no notebook
    df["risco"] = (df["IDA"] < 5).astype(int)

    # escolha de variáveis preditoras exatamente como no notebook
    features = ["IEG", "IPP", "IPS", "IAA", "IAN"]

    df_model = df[features + ["risco"]].dropna()

    X = df_model[features]
    y = df_model["risco"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    pred = model.predict(X_test)
    proba = model.predict_proba(X_test)[:, 1]

    report = classification_report(y_test, pred, output_dict=False)
    auc = roc_auc_score(y_test, proba)
    coeficientes = pd.Series(model.coef_[0], index=features).sort_values(ascending=False)

    return {
        "model": model,
        "features": features,
        "report": report,
        "auc": auc,
        "coeficientes": coeficientes,
        "n_linhas_modelo": len(df_model),
    }