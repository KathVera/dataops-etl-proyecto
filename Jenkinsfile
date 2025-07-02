pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Limpiar workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Clonar repositorio') {
            steps {
                git branch: 'main', url: 'https://github.com/KathVera/dataops-etl-proyecto.git'
            }
        }

        stage('Construir imagen Docker') {
            steps {
                sh 'docker build --no-cache -t dataops-etl .'
            }
        }

        stage('Verificar archivos dentro del contenedor') {
            steps {
                sh 'docker run --rm dataops-etl ls -R /app'
            }
        }

        stage('Ejecutar contenedor') {
            steps {
                sh 'docker run --rm dataops-etl'
            }
        }
    }
}

