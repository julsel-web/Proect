pipeline {
    agent any

    stages {
        stage('Подготовка окружения') {
            steps {
                checkout scm
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate && pip install -r requirements.txt'
                sh '. .venv/bin/activate && playwright install chromium'
            }
        }

        stage('API тесты') {
            steps {
                sh '. .venv/bin/activate && pytest -m api --alluredir=allure-results'
            }
        }

        stage('UI тесты') {
            steps {
                sh '. .venv/bin/activate && pytest -m ui --browser-name=chromium --alluredir=allure-results'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**/*', allowEmptyArchive: true
            archiveArtifacts artifacts: 'artifacts/**/*', allowEmptyArchive: true
        }
    }
}
