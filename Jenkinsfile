pipeline {
    agent any

    environment {
        DATA_PATH = "data/"
        MODEL_PATH = "models/"
    }

    stages {
        stage('Cloner le code') {
            steps {
                git branch: 'main', url: 'https://github.com/ouassim16wass/mini-projet.git'
            }
        }

        stage('Installer les dépendances') {
            steps {
                sh 'python3 -m pip install --no-cache-dir -r requirements.txt'
            }
        }

        stage('Prétraitement des données avec Docker') {
            steps {
                sh '''
                echo "🚀 Construction de l'image Docker pour le prétraitement..."
                docker build -t mini-projet-preprocessing . || { echo "⚠️ Erreur lors du build Docker"; exit 1; }

                echo "⚡ Exécution du conteneur de prétraitement..."
                docker run --rm -v $PWD/data:/app/data mini-projet-preprocessing || { echo "⚠️ Erreur lors de l'exécution Docker"; exit 1; }
                '''
            }
        }

        stage('Entraînement du modèle') {
            steps {
                sh '''
                echo "🚀 Début de l'entraînement du modèle..."
                python3 train.py || { echo "❌ Erreur lors de l'entraînement"; exit 1; }
                '''
            }
        }

        stage('Évaluation du modèle') {
            steps {
                sh '''
                echo "📊 Évaluation des performances du modèle..."
                python3 evaluate.py || { echo "❌ Erreur lors de l'évaluation"; exit 1; }
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
