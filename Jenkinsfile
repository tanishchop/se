pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: '<your-repo-url>'  // Replace with your repository URL
            }
        }
        stage('Install Dependencies') {
            steps {
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage('Run Migrations') {
            steps {
                bat 'venv\\Scripts\\activate && python manage.py migrate'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\activate && python manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                // Add your deployment steps here, e.g., rsync files to server, restart service
                echo 'Deployment placeholder - customize for your environment'
            }
        }
    }
    post {
        always {
            bat 'venv\\Scripts\\activate && python manage.py collectstatic --noinput'
        }
    }
}