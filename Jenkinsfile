pipeline {
    agent any

    stages {
        stage('Installation des dépendances') {
            steps {
                // Créer un environnement virtuel pour Python
                bat 'python -m venv venv'
                bat '.\\venv\\Scripts\\pip install --upgrade pip'
                bat '.\\venv\\Scripts\\pip install -r requirements.txt' // Assurez-vous que requirements.txt contient les dépendances nécessaires
            }
        }

        stage('Prétraitement des données') {
            steps {
                // Exécuter le script preprocessing.py
                bat '.\\venv\\Scripts\\python preprocessing.py'
            }
        }

        stage('Entraînement des modèles') {
            steps {
                // Exécuter le script d'entraînement des modèles
                bat '.\\venv\\Scripts\\python train.py'
            }
        }

        stage('Évaluation des modèles') {
            steps {
                // Exécuter le script d'évaluation des modèles
                bat '.\\venv\\Scripts\\python evaluate.py'
            }
        }

        stage('Sauvegarde des artefacts') {
            steps {
                // Sauvegarder les modèles en tant qu'artefacts de Jenkins
                archiveArtifacts artifacts: '**/*.pkl', allowEmptyArchive: true
                // Si vous avez un fichier de résultats, vous pouvez également l'archiver
                archiveArtifacts artifacts: 'clean_train_reduced.csv', allowEmptyArchive: true
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
