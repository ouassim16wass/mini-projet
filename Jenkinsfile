pipeline {
    agent any

    environment {
        DATA_PATH = "data/"  // Assure-toi que les fichiers train.csv et test.csv se trouvent dans ce dossier
        MODEL_PATH = "models/"
    }

    stages {
        stage('Cloner le repository') {
            steps {
                script {
                    // Cloner ton repository GitHub
                    echo "🛠️ Clonage du repository..."
                    git branch: 'main', url: 'https://github.com/ouassim16wass/mini-projet.git'
                }
            }
        }

        stage('Installer les dépendances') {
            steps {
                script {
                    // Installer les dépendances avec pip à partir du fichier requirements.txt
                    echo "📦 Installation des dépendances..."
                    bat 'python -m pip install --no-cache-dir -r requirements.txt || echo "❌ Erreur lors de l\'installation des dépendances" && exit 1'
                }
            }
        }

        stage('Prétraitement des données') {
            steps {
                script {
                    // Vérifie que les fichiers de données existent dans le dossier "data"
                    echo "🚀 Démarrage du prétraitement des données..."
                    if (fileExists("${DATA_PATH}train.csv") && fileExists("${DATA_PATH}test.csv")) {
                        echo "✔️ Les fichiers de données existent, traitement lancé."
                        // Lancer le prétraitement des données avec preprocessing.py
                        bat 'python preprocessing.py || echo "❌ Erreur lors du prétraitement des données" && exit 1'
                    } else {
                        error "❌ Les fichiers de données train.csv et test.csv sont manquants."
                    }
                }
            }
        }

        stage('Entraînement du modèle') {
            steps {
                script {
                    // Lancer l'entraînement du modèle
                    echo "🚀 Début de l'entraînement du modèle..."
                    bat 'python train.py || echo "❌ Erreur lors de l\'entraînement du modèle" && exit 1'
                }
            }
        }

        stage('Évaluation du modèle') {
            steps {
                script {
                    // Évaluer les performances du modèle
                    echo "📊 Évaluation des performances du modèle..."
                    bat 'python evaluate.py || echo "❌ Erreur lors de l\'évaluation du modèle" && exit 1'
                }
            }
        }

        stage('Stockage des artefacts') {
            steps {
                script {
                    // Archiver les modèles générés (par exemple, rf_model.pkl, dt_model.pkl)
                    echo "🔐 Sauvegarde des artefacts du modèle..."
                    archiveArtifacts artifacts: 'rf_model.pkl, dt_model.pkl, ann_model.pkl', fingerprint: true
                }
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
