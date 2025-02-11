pipeline {
    agent any

    environment {
        // Définir les variables d'environnement si nécessaire
        PYTHON_ENV = "venv"
    }

    stages {
        stage('Installation des dépendances') {
            steps {
                script {
                    // Créer un environnement virtuel pour Python
                    bat 'python -m venv ${env.PYTHON_ENV}'
                    bat '.\\${env.PYTHON_ENV}\\Scripts\\pip install --upgrade pip'
                    bat '.\\${env.PYTHON_ENV}\\Scripts\\pip install -r requirements.txt' // Assurez-vous que requirements.txt contient les dépendances nécessaires
                }
            }
        }

        stage('Prétraitement des données') {
            steps {
                script {
                    // Exécuter le script preprocessing.py
                    bat '.\\${env.PYTHON_ENV}\\Scripts\\python preprocessing.py'
                }
            }
        }

        stage('Entraînement des modèles') {
            steps {
                script {
                    // Exécuter le script d'entraînement des modèles
                    bat '.\\${env.PYTHON_ENV}\\Scripts\\python train.py'
                }
            }
        }

        stage('Évaluation des modèles') {
            steps {
                script {
                    // Exécuter le script d'évaluation des modèles
                    bat '.\\${env.PYTHON_ENV}\\Scripts\\python evaluate.py'
                }
            }
        }

        stage('Sauvegarde des artefacts') {
            steps {
                script {
                    // Sauvegarder les modèles en tant qu'artefacts de Jenkins
                    archiveArtifacts artifacts: '**/*.pkl', allowEmptyArchive: true
                    // Si vous avez un fichier de résultats, vous pouvez également l'archiver
                    archiveArtifacts artifacts: 'clean_train_reduced.csv', allowEmptyArchive: true
                }
            }
        }
    }

    post {
        always {
            // Nettoyage après exécution (supprimer l'environnement virtuel par exemple)
            cleanWs()
        }

        success {
            echo 'Pipeline exécuté avec succès !'
        }

        failure {
            echo 'Une erreur est survenue dans la pipeline.'
        }
    }
}
