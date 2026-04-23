import json
import os
from openai import OpenAI


# SET API KEY

# export OPENAI_API_KEY

client = OpenAI(api_key=os.getenv("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"))

# BARBERSHOP DATA FROM THE POSTER

spa_data = {
    "haircuts": {
        "kids_bald": 50,
        "kids_styling": 100,
        "adult_bald": 150,
        "adult_styling": 200,
        "cut_only": 50
