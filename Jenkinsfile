pipeline {
    agent any

    environment {
        DATA_PATH = ""  // Les fichiers sont à la racine, donc pas de sous-dossier
        MODEL_PATH = "models/"
        DOCKER_IMAGE_NAME = "mini-projet-model"  // Nom de l'image Docker
        DOCKER_REGISTRY = "yourdockerhubusername"  // Remplace par ton nom d'utilisateur Docker Hub
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
                bat 'chcp 65001' // Définit l'encodage en UTF-8
                bat 'python -m pip install --no-cache-dir -r requirements.txt || exit 1'
            }
        }

        stage('Prétraitement des données avec Docker') {
            steps {
                bat 'chcp 65001' // Définit l'encodage en UTF-8
                bat 'python preprocessing.py'
            }
        }

        stage('Entraînement du modèle') {
            steps {
                bat 'chcp 65001' // Définit l'encodage en UTF-8
                bat 'python train.py'
            }
        }

        stage('Évaluation du modèle') {
            steps {
                bat 'chcp 65001' // Définit l'encodage en UTF-8
                bat 'python evaluate.py'
            }
        }

        stage('Construire l\'image Docker avec le modèle') {
            steps {
                bat 'docker build -t %DOCKER_REGISTRY%/%DOCKER_IMAGE_NAME%:latest .'
            }
        }

        stage('Push l\'image Docker vers Docker Hub') {
            steps {
                bat 'docker login -u yourdockerhubusername -p yourpassword'  // Remplace par tes credentials Docker Hub
                bat 'docker push %DOCKER_REGISTRY%/%DOCKER_IMAGE_NAME%:latest'
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
