pipeline {
    agent any

    environment {
        DATA_PATH = ""  // Les fichiers sont à la racine, donc pas de sous-dossier
        MODEL_PATH = "models/"
        DOCKER_IMAGE_NAME = 'mini-projet'
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

        stage('Construire l\'image Docker pour l\'application') {
            steps {
                script {
                    // Créer l'image Docker à partir du Dockerfile
                    sh 'docker build -t $DOCKER_IMAGE_NAME:latest .'
                }
            }
        }

        stage('Prétraitement des données avec Docker') {
            steps {
                script {
                    // Lancer le conteneur pour le prétraitement des données
                    sh 'docker run --rm -v $(pwd):/app $DOCKER_IMAGE_NAME:latest python preprocessing.py'
                }
            }
        }

        stage('Entraînement du modèle') {
            steps {
                script {
                    // Lancer le conteneur pour l'entraînement du modèle
                    sh 'docker run --rm -v $(pwd):/app $DOCKER_IMAGE_NAME:latest python train.py'
                }
            }
        }

        stage('Évaluation du modèle') {
            steps {
                script {
                    // Lancer le conteneur pour l'évaluation du modèle
                    sh 'docker run --rm -v $(pwd):/app $DOCKER_IMAGE_NAME:latest python evaluate.py'
                }
            }
        }

        stage('Pousser l\'image Docker sur DockerHub') {
            steps {
                script {
                    // Se connecter à DockerHub avec les identifiants Jenkins
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                        // Pousser l'image Docker sur DockerHub
                        sh 'docker push $DOCKER_USERNAME/$DOCKER_IMAGE_NAME:latest'
                    }
                }
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
