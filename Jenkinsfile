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
        stage('Stage 2') {
                // Declaramos un agente específico para esta etapa, que utilizará una imagen de Docker con Python y NodeJS preinstalados
                agent {
                    docker {
                        image 'nikolaik/python-nodejs:python3.12-nodejs20'
                        reuseNode true

                        // Conectar a la red de servicios para que los contenedores puedan comunicarse entre sí, la que definí en el compose
                        args '--network services-net'
                    }
                }
            // El steps se situa despues porque una vez termine, el contenedor se destruye y no se pueden ejecutar comandos en él
            steps {
                echo 'En esta etapa se preparó el entorno de Jenkins para la ejecución de los scripts de Python y NodeJS'
                echo 'A continuación se prepara la instalación de los MCP Servers de GitHub y SonarQube'

                //Verifico que se han instalado correctamente Python y NodeJS
                sh 'python --version'
                sh 'node --version'

                //Instalación del MCP Server de GitHub
                sh 'npm install -g @modelcontextprotocol/server-github'

                //Instalación del MCP Server de SonarQube
                sh 'npm install -g github:SonarSource/sonarqube-mcp-server'

                //Instalación del MCP Server de SonarQube
                sh 'npm install -g @sonar/scan'
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
