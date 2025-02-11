import joblib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

# Charger les données nettoyées
train_df = pd.read_csv("clean_train_reduced.csv")

# Rééchantillonnage SMOTE
X = train_df.drop(columns=["SalePrice"])
y = train_df["SalePrice"]

# Normalisation de la variable cible pour SMOTE
y_bins = pd.qcut(y, q=3, labels=False)

# Appliquer SMOTE
smote = SMOTE(sampling_strategy="auto", random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y_bins)

# Diviser les données après rééchantillonnage
X_train, X_test, y_train, y_test = train_test_split(
    X_resampled, y_resampled, test_size=0.2, random_state=42
)

# Charger les modèles entraînés
rf_model = joblib.load('rf_model.pkl')
dt_model = joblib.load('dt_model.pkl')  # Charger le modèle Decision Tree
ann_model = joblib.load('ann_model.pkl')  # Charger le modèle ANN

# Prédictions après rééchantillonnage
y_pred_rf = rf_model.predict(X_test)
y_pred_dt = dt_model.predict(X_test)  # Prédictions pour le modèle Decision Tree
y_pred_ann = ann_model.predict(X_test)  # Prédictions pour le modèle ANN

# Évaluation des modèles après rééchantillonnage
accuracy = {
    "Random Forest": accuracy_score(y_test, y_pred_rf),
    "Decision Tree": accuracy_score(y_test, y_pred_dt),
    "Artificial Neural Network": accuracy_score(y_test, y_pred_ann)
}

# Affichage des résultats
results_df = pd.DataFrame(list(accuracy.items()), columns=["Modèle", "Accuracy"])
print("Résultats après rééchantillonnage :\n", results_df)

# Optionnel: Visualisation des résultats
sns.barplot(x="Modèle", y="Accuracy", data=results_df)
plt.title("Précision des modèles après rééchantillonnage")
plt.show()



