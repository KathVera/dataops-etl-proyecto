pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                git branch: 'main', url: 'https://github.com/KathVera/dataops-etl-proyecto.git'
            }
        }

        stage('Construir imagen Docker') {
            steps {
                sh 'docker build -t dataops-etl .'
            }
        }

        stage('Ejecutar contenedor') {
            steps {
                sh 'docker run --rm dataops-etl'
            }
        }
    }
}

