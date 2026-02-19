from mcp import ClientSession, StdioServerParameters # this library is used to create a client that can communicate with the MCP server using standard input and output
from mcp.client.stdio import stdio_client #this library is used to create a client that can communicate with the MCP server using standard input and output
from contextlib import AsyncExitStack # this library is used to manage multiple connections at the same time
from google import genai # this library is used to access the Google Gemini LLM
import asyncio # this library is used to run the client asynchronously
import os # this library is used to access environment variables
import sys # this library is used to access command line arguments


# Load environment variables
GITHUB_TOKEN = os.getenv("GITHUB_AUTH_TOKEN")
SONARQUBE_TOKEN = os.getenv("SONARQUBE_AUTH_TOKEN")
BITCBUCKET_TOKEN = os.getenv("BITBUCKET_AUTH_TOKEN") #TODO: need to be configured in jenkins
LLM_TOKEN = os.getenv("LLM_AUTH_TOKEN")

SONAR_URL = os.getenv("SONARQUBE_HOST_URL", "http://sonarqube-server:9000")

#Gemini LLM configuration
#genai.Client(api_key=LLM_TOKEN) #TODO: need the API token

# Commands needed to bring up the MCP servers by npx
mcp_servers = {
    "bitbucket": StdioServerParameters
    (
        command="npx",
        args=["-y", "bitbucket-mcp"],
        env={**os.environ} # Pass all the enviroment variables to the MCP server to get the credentials
    ),
    "sonarqube": StdioServerParameters
    (
        command="npx",
        args=["-y", "mcp-sonarqube"], 
        env={**os.environ}
    )
}

# List the tools of the sonarqube MCP server
async def list_sonar_tools():
    # Start the MCP server and create a client to communicate with it using standard input and output
    async with stdio_client(mcp_servers["sonarqube"]) as (read, write):
        #Establish a session with the MCP server using the client
        async with ClientSession(read, write) as session:
            # Initialize the session, the initial handshake
            await session.initialize()
            # List the tools of the sonarqube MCP server
            response = await session.list_tools()
            
            print("SonarQube MCP Server Tools:")
            for tool in response.tools:
                print(f"- {tool.name}")
                
# Main function to run the client
if __name__ == "__main__":
    try:
        # Run the list_sonar_tools function asynchronously
        asyncio.run(list_sonar_tools())
    except Exception as e:
        print(f"An error occurred while trying to list the tools of the SonarQube MCP server: {e}")