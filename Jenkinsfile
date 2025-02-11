pipeline {
    agent any

    environment {
        DATA_PATH = ""  // Les fichiers sont à la racine, donc pas de sous-dossier
        MODEL_PATH = "models/"
        DOCKER_IMAGE_NAME_PREPROCESSING = "mini-projet-preprocessing"
        DOCKER_IMAGE_NAME_TRAINING = "mini-projet-training"
        DOCKER_IMAGE_NAME_EVALUATION = "mini-projet-evaluation"
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

        stage('Construire et lancer le conteneur Docker pour le prétraitement') {
            steps {
                script {
                    // Construire l'image Docker pour le prétraitement
                    sh 'docker build -f Dockerfile-preprocessing -t $DOCKER_IMAGE_NAME_PREPROCESSING .'
                    
                    // Exécuter le conteneur Docker pour le prétraitement
                    sh 'docker run --rm -v $PWD:/app $DOCKER_IMAGE_NAME_PREPROCESSING python preprocessing.py'
                }
            }
        }

        stage('Construire et lancer le conteneur Docker pour l\'entraînement') {
            steps {
                script {
                    // Construire l'image Docker pour l'entraînement
                    sh 'docker build -f Dockerfile-train -t $DOCKER_IMAGE_NAME_TRAINING .'
                    
                    // Exécuter le conteneur Docker pour l'entraînement
                    sh 'docker run --rm -v $PWD:/app $DOCKER_IMAGE_NAME_TRAINING python train.py'
                }
            }
        }

        stage('Construire et lancer le conteneur Docker pour l\'évaluation') {
            steps {
                script {
                    // Construire l'image Docker pour l'évaluation
                    sh 'docker build -f Dockerfile-evaluate -t $DOCKER_IMAGE_NAME_EVALUATION .'
                    
                    // Exécuter le conteneur Docker pour l'évaluation
                    sh 'docker run --rm -v $PWD:/app $DOCKER_IMAGE_NAME_EVALUATION python evaluate.py'
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
