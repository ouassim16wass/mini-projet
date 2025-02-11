pipeline {
    agent any

    environment {
        DATA_PATH = "data/"  // Répertoire pour les fichiers de données
        MODEL_PATH = "models/"  // Répertoire pour les modèles entraînés
    }

    stages {
        // Cloner le code depuis le repository Git
        stage('Cloner le code') {
            steps {
                echo "🚀 Clonage du repository..."
                git branch: 'main', url: 'https://github.com/ouassim16wass/mini-projet.git' || { echo "❌ Erreur lors du clonage du repository"; exit 1; }
            }
        }

        // Installer les dépendances nécessaires à partir du fichier requirements.txt
        stage('Installer les dépendances') {
            steps {
                echo "🔧 Installation des dépendances..."
                bat 'python -m pip install --no-cache-dir -r requirements.txt || exit 1' // Arrêt en cas d'erreur
            }
        }

        // Prétraiter les données
        stage('Prétraitement des données') {
            steps {
                echo "🧹 Début du prétraitement des données..."
                bat '''
                chcp 65001  // Permet d'assurer la gestion correcte des caractères
                python preprocess.py --train_file train.csv --test_file test.csv || { echo "❌ Erreur lors du prétraitement"; exit 1; }
                '''
            }
        }

        // Entraînement du modèle
        stage('Entraînement du modèle') {
            steps {
                echo "🚀 Début de l'entraînement du modèle..."
                bat '''
                chcp 65001  // Permet d'assurer la gestion correcte des caractères
                python train.py --train_file train.csv --test_file test.csv || { echo "❌ Erreur lors de l'entraînement"; exit 1; }
                '''
            }
        }

        // Évaluation du modèle
        stage('Évaluation du modèle') {
            steps {
                echo "📊 Évaluation des performances du modèle..."
                bat '''
                chcp 65001  // Permet d'assurer la gestion correcte des caractères
                python evaluate.py --train_file train.csv --test_file test.csv || { echo "❌ Erreur lors de l'évaluation"; exit 1; }
                '''
            }
        }

        // Stockage des artefacts (modèle entraîné, etc.)
        stage('Stockage des artefacts') {
            steps {
                echo "📦 Stockage des artefacts..."
                archiveArtifacts artifacts: 'models/*.pkl', fingerprint: true || { echo "❌ Erreur lors du stockage des artefacts"; exit 1; }
            }
        }
    }

    post {
        success {
            echo "🎉 Pipeline terminé avec succès ! ✅"
        }
        failure {
            echo "🚨 Le pipeline a échoué ! Vérifie les logs Jenkins pour plus de détails."
        }
    }
}
