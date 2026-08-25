"""
Baseline model training with MLflow tracking.

Swap `load_data()` and the model in `train()` for your chosen use case
(fraud detection, churn, sentiment, etc). Keep the ML simple — the point
of this project is everything around the model, not the model itself.
"""
import mlflow
import mlflow.sklearn
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

MLFLOW_EXPERIMENT = "model-serving-platform"


def load_data():
    # Replace with your real dataset loader.
    X, y = make_classification(n_samples=2000, n_features=4, random_state=42)
    return train_test_split(X, y, test_size=0.2, random_state=42)


def train():
    mlflow.set_experiment(MLFLOW_EXPERIMENT)
    X_train, X_test, y_train, y_test = load_data()

    with mlflow.start_run():
        params = {"n_estimators": 100, "max_depth": 6, "random_state": 42}
        mlflow.log_params(params)

        model = RandomForestClassifier(**params)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        metrics = {
            "accuracy": accuracy_score(y_test, preds),
            "f1": f1_score(y_test, preds),
        }
        mlflow.log_metrics(metrics)

        mlflow.sklearn.log_model(model, artifact_path="model", registered_model_name="serving-model")

        print(f"Run logged. Metrics: {metrics}")
        return mlflow.active_run().info.run_id


if __name__ == "__main__":
    train()
