pipeline {
    agent any

    environment {
        DATA_PATH = "data/"
        MODEL_PATH = "models/"
        TRAIN_FILE = "train.csv" // Spécifie le chemin absolu ou relatif
        TEST_FILE = "test.csv"   // Spécifie le chemin absolu ou relatif
    }

    stages {
        stage('Cloner le code') {
            steps {
                git branch: 'main', url: 'https://github.com/ouassim16wass/mini-projet.git'
            }
        }

        stage('Installer les dépendances') {
            steps {
                bat 'python -m pip install --no-cache-dir -r requirements.txt'
            }
        }

        stage('Prétraitement des données') {
            steps {
                echo "🚀 Début du prétraitement des données..."
                bat "python preprocessing.py ${TRAIN_FILE} ${TEST_FILE}"
            }
        }

        stage('Entraînement du modèle') {
            steps {
                echo "🚀 Début de l'entraînement du modèle..."
                bat '''
                chcp 65001
                python train.py || echo "❌ Erreur lors de l'entraînement" && exit 1
                '''
            }
        }

        stage('Évaluation du modèle') {
            steps {
                echo "📊 Évaluation des performances du modèle..."
                bat '''
                chcp 65001
                python evaluate.py || echo "❌ Erreur lors de l'évaluation" && exit 1
                '''
            }
        }

        stage('Stockage des artefacts') {
            steps {
                archiveArtifacts artifacts: 'models/*.pkl', fingerprint: true
            }
        }
    }

    post {
        success {
            echo "🎉 Pipeline terminé avec succès ! ✅"
        }
        failure {
            echo "🚨 Le pipeline a échoué ! Vérifie les logs Jenkins."
        }
    }
}
