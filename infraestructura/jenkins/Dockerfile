# For Jenkins, I need the Dockerfile since I need to install things inside that don't come in the default image.
FROM jenkins/jenkins:2.541.1-jdk21
USER root
RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list

# Installation of Docker CLI + Node.js/NPM to use it in Jenkins pipelines
RUN apt-get update && apt-get install -y \
    docker-ce-cli \
    git \
    nodejs \
    npm

# Installation of Python and pip to use it in Jenkins pipelines
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# Installation of SonarScanner and MCP Servers for GitHub and SonarQube
RUN npm install -g \
    @modelcontextprotocol/server-github \
    @sonar/scan \
    mcp-sonarqube \
    bitbucket-mcp

# Installation of Jenkins plugins for the pipeline
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow json-path-api"

# Jenkins needs to run as the jenkins user
USER jenkins