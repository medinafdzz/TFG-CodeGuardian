import requests #Para hacer llamadas a las APIs de SonarQube, GitHub, y el LLM
import sys # Para manejar argumentos de linea de comandos, como el repositorio a analizar, etc
import os # Para cargar las variables de entorno con las credenciales necesarias para el agente IA (GitHub, SonarQube, LLM)
import abc # Este modulo permite hacer clases abstractas, que usare para elegir un LLM

# Carga las variables de entorno
GITHUB_TOKEN = os.getenv("GITHUB_AUTH_TOKEN")
SONARQUBE_TOKEN = os.getenv("SONARQUBE_AUTH_TOKEN")
LLM_TOKEN = os.getenv("LLM_AUTH_TOKEN")

# Conectar con el SonarQube Server
SONAR_URL = os.getenv("SONARQUBE_HOST_URL", "http://sonarqube-server:9000")

# Definicion del LLM abstracto, que luego se implementara para cada LLM concreto (Gemini, ChatGPT, etc)
class LLM(abc.ABC):
        # Metodo abstracto para generar respuestas, cada LLM concreto implementara este metodo
        @abc.abstractmethod
        def generar_respuesta(self, prompt):
                pass

class Gemini(LLM):
        
        def __init__(self,api_key):
                self.api_key = api_key
                
        def generar_respuesta(self, prompt):
                return "Aqui me falta implementar la llamada con el prompt"
        
class ChatGPT(LLM):
        
        def __init__(self,api_key):
                self.api_key = api_key
                
        def generar_respuesta(self, prompt):
                return "Aqui me falta implementar la llamada con el prompt"

#selector del LLM
def configurar_llm():
        # Aqui podria cambiarse por otros LLM
        return Gemini(LLM_TOKEN)
        
# Clase para interactuar con el SonarQube Server, que luego se usara en el agente para obtener los resultados del analisis de codigo
class SonarClient:
        
        def __init__(self,url,token):
                self.url = url
                self.token = (token, '') # SonarQube usa autenticacion basica, el token se pasa como usuario y la contraseña se deja vacia
        
        # Metodo para probar la conexion con el SonarQube Server
        def probar_conexion(self):
                endpoint = f"{self.url}/api/system/ping"
                response = requests.get(endpoint, auth=self.token)
                if response.status_code == 200:
                        print("Conexion con SonarQube exitosa")
                else:
                        print(f"Error al conectar con SonarQube: {response.status_code} - {response.text}")
       
        # TODO: Get the issues of a project, filtering by severity and status (only open issues with high or blocker severity)                
        def list_issues(self, project_key):
                endpoint = f"{self.url}/api/issues/search"
                params = {
                        "componentKeys": project_key,
                        "severities": "CRITICAL,BLOCKER",
                        "statuses": "OPEN"
                }
                
                response = requests.get(endpoint, auth=self.token, params=params)

                if response.status_code == 200:
                        data = response.json()
                        return data
                else:
                        print(f"Error al obtener las issues de SonarQube: {response.status_code} - {response.text}")
                        return None
# main
def main():
        
        llm = configurar_llm()
        
        mcp_sonar = SonarClient(SONAR_URL, SONARQUBE_TOKEN)
        
        mcp_sonar.probar_conexion()
        
        if (len(sys.argv) < 2):
                print("Por favor, proporciona el project key de SonarQube como argumento manualmente")
                sys.exit(1)
                
        resultados =mcp_sonar.list_issues(sys.argv[1])
        print(resultados)

# Entrypoint of the script 
if __name__ == "__main__":
        main()