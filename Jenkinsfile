pipeline {
    agent any

    environment {
        DATA_PATH = "."  // Les fichiers de données sont à la racine
        MODEL_PATH = "models/"
        DOCKER_IMAGE_NAME = "mini-projet-model"
        DOCKER_REGISTRY = "wassim33" // Ton Docker Hub
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
                    if (fileExists("${DATA_PATH}/train.csv") && fileExists("${DATA_PATH}/test.csv")) {
                        echo "✔️ Les fichiers de données existent."
                    } else {
                        error "❌ Les fichiers de données train.csv et test.csv sont manquants."
                    }
                }
            }
        }

        stage('Installer les dépendances') {
            steps {
                bat 'python -m pip install --no-cache-dir -r requirements.txt'
            }
        }

        stage('Prétraitement des données avec Docker') {
            steps {
                bat 'docker run --rm -v %CD%:/app -w /app python:3.9 python preprocessing.py'
            }
        }

        stage('Entraînement du modèle') {
            steps {
                bat 'python train.py'
            }
        }

        stage('Évaluation du modèle') {
            steps {
                bat 'python evaluate.py'
            }
        }

        stage('Stockage des artefacts') {
            steps {
                archiveArtifacts artifacts: 'models/*.pkl', fingerprint: true
            }
        }

        stage('Nettoyage des anciens conteneurs Docker') {
            steps {
                bat 'docker rm -f $(docker ps -aq) || echo "Aucun conteneur à supprimer"'
                bat 'docker rmi -f %DOCKER_REGISTRY%/%DOCKER_IMAGE_NAME% || echo "Aucune image à supprimer"'
            }
        }

        stage('Construire l\'image Docker avec le modèle') {
            steps {
                bat 'docker build -t %DOCKER_REGISTRY%/%DOCKER_IMAGE_NAME%:latest .'
            }
        }

        stage('Push l\'image Docker vers Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    bat "docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%"
                    bat "docker push %DOCKER_REGISTRY%/%DOCKER_IMAGE_NAME%:latest"
                }
            }
        }

        stage('Déploiement avec Docker Compose') {
            steps {
                bat 'docker-compose down || echo "Pas de services en cours"'
                bat 'docker-compose up -d --build'
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
