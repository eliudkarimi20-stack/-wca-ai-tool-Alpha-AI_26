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
           },
    "haircut_dye": {
        "kids_black": 300,
        "kids_colour": 500,
        "adult_black": 400,
        "adult_colour": 800
        "beard": {
        "beard_trim": 50,
        "eyebrow": 50
    },
    "care": {
        "hair_wash": 100,
        "face_scrub": 100,
        "full_face_scrub": 300,
        "straightening": 100,
        "wash_straight": 200,
        "blowdry": 250
    },
  "dreadlocks": {
        "natural": 3000,
        "retouch": 500,
        "artificial": 1500
    },  "braids": {
        "knotless": 800,
        "under_6": 600,
        "extensions_knotless": 1000,
        "extensions_normal": 900
    }, "extras": {
        "school_lines": 150,
        "needle_lines": 200,
        "back_to_school": 350,
        "other_styles": 450
    },
"weaves": {
        "weaving": 400,
        "pedicure": 500
    }
}


# PRICE CALCULATOR

def calculate_total(user_input):
    text = user_input.lower()
    total = 0
    matched_services = []

    if "kids" in text and "style" in text:
        total += spa_data["haircuts"]["kids_styling"]
        matched_services.append("Kids Styling")
  if "adult" in text and "cut" in text:
        total += spa_data["haircuts"]["adult_bald"]
        matched_services.append("Adult Haircut")

    if "beard" in text:
        total += spa_data["beard"]["beard_trim"]
        matched_services.append("Beard Trim")
