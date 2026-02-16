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
        stage('Stage 1 - Descarga del repositorio') {
            steps {
                echo 'En esta etapa se descarga el repositorio que hizo el webhook'
                checkout scm
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
