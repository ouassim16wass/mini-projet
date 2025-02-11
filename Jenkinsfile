pipeline {
    agent any

    environment {
        DATA_PATH = ""  // Les fichiers sont à la racine, donc pas de sous-dossier
        MODEL_PATH = "models/"
    }

    stages {
        stage('Cloner le code') {
            steps {
                git branch: 'main', url: 'https://github.com/ouassim16wass/mini-projet.git'
            }
        }

        stage('Vérifier les fichiers de données') {
            steps {
                script {
                    if (fileExists('train.csv') && fileExists('test.csv')) {
                        echo "✔️ Les fichiers de données existent, traitement lancé."
                    } else {
                        error "❌ Les fichiers de données train.csv et test.csv sont manquants."
                    }
                }
            }
        }

        stage('Installer les dépendances') {
            steps {
                bat 'python -m pip install --no-cache-dir -r requirements.txt || exit 1'
            }
        }

        stage('Prétraitement des données avec Docker') {
            steps {
                bat '''
                echo "🚀 Début du prétraitement des données..."
                python preprocessing.py || echo "❌ Erreur lors du prétraitement des données" && exit 1
                '''
            }
        }

        stage('Entraînement du modèle') {
            steps {
                bat '''
                echo "🚀 Début de l'entraînement du modèle..."
                python train.py || echo "❌ Erreur lors de l'entraînement" && exit 1
                '''
            }
        }

        stage('Évaluation du modèle') {
            steps {
                bat '''
                echo "📊 Évaluation des performances du modèle..."
                python evaluate.py || echo "❌ Erreur lors de l'évaluation" && exit 1
                '''
            }
        }

        stage('Stockage des artefacts') {
            steps {
                archiveArtifacts artifacts: 'rf_model.pkl, dt_model.pkl, ann_model.pkl', fingerprint: true
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
