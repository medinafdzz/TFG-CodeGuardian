pipeline {
    // Declaramos el agente que se encargará de ejecutar las etapas del pipeline
    agent any

    // Declaracion de las variables de entorno necesarias para la ejecución del pipeline
    environment {
        SONARQUBE_HOST_URL = 'http://sonarqube-server:9000' // URL del servidor de SonarQube
        SONAR_ORG = 'medinafdzz' // en caso de usar SonarQube cloud

        //Tokens de autenticación
        SONARQUBE_AUTH_TOKEN = credentials('sonarqube-token')
        GITHUB_AUTH_TOKEN = credentials('github-token')
    }

    // Definicion de las etapas del pipeline
    stages {
        stage('Stage 0 - Preparación del entorno') {
            steps {
                //Verificar la instalacion correcta
                sh 'python3 --version'
                sh 'node --version'
            }
        }
        stage('Stage 1 - Descarga del repositorio y analisis con SonarQube') {
            steps {
                echo 'En esta etapa se descarga el repositorio que hizo el webhook'
                checkout scm

                echo 'Compilando el código de ejemplo Java para el análisis de SonarQube'
                sh 'javac src/*.java'
                echo 'Analisis con SonarQube'
                script {
                    echo 'Se ejecuta SonarQube Scanner para analizar el código'
                    withSonarQubeEnv('SonarQube-Server') {
                        sh 'sonar-scanner -Dsonar.projectKey=TFG-CodeGuardian -Dsonar.sources=. -Dsonar.java.binaries=src'
                    }
                    echo 'Aqui SonarQube medira la calidad del codigo'

                    timeout(time: 5, unit: 'MINUTES') {
                        waitForQualityGate abortPipeline: true
                    }
                }
            }
        }
    }
        //Borra los archivos temporales generados por el pipeline
        post {
            always {
                echo 'Limpiando los archivos temporales generados por el pipeline'
                deleteDir()
            }
        }
}
