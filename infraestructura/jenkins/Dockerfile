#En el caso de Jenkins, necesito el dockerfile, ya que necesitaré instalarle cosas dentro que no vienen en la iimagen por defecto.
FROM jenkins/jenkins:2.541.1-jdk21
USER root
RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list

# Instalacion de Docker CLI para poder usarlo en los pipelines de Jenkins
RUN apt-get update && apt-get install -y docker-ce-cli

# Instalacion de Python y pip para poder usarlo en los pipelines de Jenkins
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

USER jenkins

RUN npm install -g \
    @modelcontextprotocol/server-github \
    github:SonarSource/sonarqube-mcp-server \
    @sonar/scan

RUN jenkins-plugin-cli --plugins "blueocean docker-workflow json-path-api"