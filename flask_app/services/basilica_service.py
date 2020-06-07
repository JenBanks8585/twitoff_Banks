import basilica
import os
from dotenv import load_dotenv

load_dotenv()

basilica_apikey= os.getenv("BASILICA_API_KEY", default="BASILICA_api_key")

connection = basilica.Connection(basilica_apikey)
print('CONNECTION', type(connection))

#if __name__=="__main__":


