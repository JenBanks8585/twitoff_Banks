import basilica
import os
from dotenv import load_dotenv

load_dotenv()

basilica_apikey= os.getenv("BASILICA_API_KEY", default="BASILICA_api_key")

connection = basilica.Connection(basilica_apikey)
print('CONNECTION', type(connection))

tweets = ["hey hey Monday", "The world is not enough #bond", "goodbye Corona, go away"]
embeddings = connection.embed_sentences(tweets, model='twitter')
for embed in embeddings:
    print("_______")
    print(len(embed))
