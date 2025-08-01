from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, r2_score

def train_model(X, y):
    model = XGBRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    y_pred = model.predict(X)
    mae = mean_absolute_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    return model, mae, r2
