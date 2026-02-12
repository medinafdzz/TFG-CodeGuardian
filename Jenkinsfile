pipeline {
    agent any

    stage('Stage 1') {
        steps {
            echo 'En esta etapa se prepara el entorno de Jenkins para la ejecución de los scripts de Python y NodeJS'
            image 'nikolaik/python-nodejs:python3.12-nodejs20'
            reuseNode true
        }
    }

    stage('Stage 2') {
        steps {
            echo 'A continuación se prepara la instalación de los MCP Servers de GitHub y SonarQube'

            sh 'npm install python3.9'
        }
    }
}
