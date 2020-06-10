import basilica
import os
from dotenv import load_dotenv

load_dotenv()

basilica_apikey= os.getenv("BASILICA_API_KEY", default="BASILICA_api_key")

connection = basilica.Connection(basilica_apikey)
print('CONNECTION', type(connection))




if __name__=="__main__":
    
    embedding = connection.embed_sentences("hey this is great", model = "twitter")
    print(type(embedding))
    

    tweets = ["Hello World", " The quick brown fox", "such a great world"]
    embeddings = connection.embed_sentences(tweets, model ="twitter")
    for embed in embeddings:
        print("___________________")
        print(len(embed))




