pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'
    }

	stage('Limpiar workspace') {
            steps {
                deleteDir()
            }
        }
	
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
                // Ejecuta el contenedor como está definido en Dockerfile (CMD ["python", "main.py"])
                sh 'docker run --rm dataops-etl'
            }
        }
    }
}
