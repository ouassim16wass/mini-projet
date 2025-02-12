# evaluate.py
import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

# Charger les données nettoyées
test_df = pd.read_csv("clean_train_reduced.csv")

# Séparation des données
X = test_df.drop(columns=["SalePrice"])
y = test_df["SalePrice"]

# Charger les modèles sauvegardés
rf_model = joblib.load('rf_model.pkl')
dt_model = joblib.load('dt_model.pkl')
ann_model = joblib.load('ann_model.pkl')

# Prédictions avec chaque modèle
rf_preds = rf_model.predict(X)
dt_preds = dt_model.predict(X)
ann_preds = ann_model.predict(X)

# Évaluation des modèles
rf_mae = mean_absolute_error(y, rf_preds)
dt_mae = mean_absolute_error(y, dt_preds)
ann_mae = mean_absolute_error(y, ann_preds)

rf_mse = mean_squared_error(y, rf_preds)
dt_mse = mean_squared_error(y, dt_preds)
ann_mse = mean_squared_error(y, ann_preds)

# Affichage des résultats
print(f"Random Forest MAE: {rf_mae}, MSE: {rf_mse}")
print(f"Decision Tree MAE: {dt_mae}, MSE: {dt_mse}")
print(f"ANN MAE: {ann_mae}, MSE: {ann_mse}")

# Comparaison des prédictions
plt.figure(figsize=(10, 6))
plt.plot(y.values, label='Vraies valeurs', alpha=0.7)
plt.plot(rf_preds, label='Prédictions Random Forest', alpha=0.7)
plt.plot(dt_preds, label='Prédictions Decision Tree', alpha=0.7)
plt.plot(ann_preds, label='Prédictions ANN', alpha=0.7)
plt.legend()
plt.show()
