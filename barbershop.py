import json
import os
from openai import OpenAI


# SET API KEY

# export OPENAI_API_KEY

client = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))

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
         if "dread" in text:
        total += spa_data["dreadlocks"]["retouch"]
        matched_services.append("Dreadlocks Retouch")

    if "braid" in text:
        total += spa_data["braids"]["knotless"]
        matched_services.append("Knotless Braids")

    return total, matched_services# AI RESPONSE FUNCTION

def generate_response(user_input):
    total, services = calculate_total(user_input)

    prompt = f"""
    ROLE: RULES:
    - Be short and clear
    - Use Kenyan Shillings (KES)
    - If services are mentioned, confirm and show total
    - Suggest related services if helpful

    EXTRA DATA:
    Detected services: {services}
    Pre-calculated total: {total} KES
    You are a professional and friendly barber assistant for Exotic Barbershop in Kenya.

    TASK:
    Answer customer questions about services and prices.

    CONTEXT:
    Here is the price list:
    {json.dumps(spa_data, indent=2)}
 RULES:
    - Be short and clear
    - Use Kenyan Shillings (KES)
    - If services are mentioned, confirm and show total
    - Suggest related services if helpful

    EXTRA DATA:
    Detected services: {services}
    Pre-calculated total: {total} KES
       USER QUESTION:
    {user_input}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    return response.choices[0].message.content



# DISPLAY FULL MENU

def show_menu():
    print("\n FULL PRICE LIST:")
    for category, items in spa_data.items():
        print(f"\n--- {category.upper()} ---")
        for service, price in items.items():
            print(f"{service}: {price} KES")# LOOP

def main():
    print(" Welcome to Exotic Barbershop AI Assistant")
    print("Type 'menu' to see all prices")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Assistant: Thank you for visiting! ")
            break

        if user_input.lower() == "menu":
            show_menu()
            continue

        try:
            reply = generate_response(user_input)
            print(f"Assistant: {reply}\n")

        except Exception as e:
            print(f" Error: {e}")



# RUN APP

if _name_ == "_main_":
    main()


