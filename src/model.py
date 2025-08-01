from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, r2_score

def train_model(X, y):
    model = XGBRegressor()
    model.fit(X, y)

    preds = model.predict(X)
    mae = mean_absolute_error(y, preds)
    r2 = r2_score(y, preds)

    return model, mae, r2
