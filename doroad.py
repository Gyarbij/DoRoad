from flask import Flask, request, jsonify, render_template
import openai
import os
import datetime

app = Flask(__name__)

# OpenAI Azure API setup using environment variables for sensitive data
openai.api_type = os.getenv('OPENAI_API_TYPE', 'azure')
openai.api_version = os.getenv('OPENAI_API_VERSION', '2023-08-01-preview')
openai.api_key = os.getenv('OPENAI_API_KEY', '')
openai.api_base = os.getenv('OPENAI_API_BASE', '')
model_deployment_name = os.getenv('DEPLOYMENT_NAME', '')

@app.route('/')
def index():
    return render_template('doroad.html')

@app.route('/generate_itinerary', methods=['POST'])
def generate_itinerary():
    # Get variables from the request
    day = request.json.get('day')
    num_persons = request.json.get('number_of_persons')
    num_children = request.json.get('number_of_children')
    departure = request.json.get('departure')
    destination = request.json.get('destination')
    
    # Construct the prompt
    prompt = f"{day} {destination} {num_persons} {num_children} {departure}" #Construct the prompt
    
    try:
        # Get response from OpenAI API
        response = openai.ChatCompletion.create(
            engine=model_deployment_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.75,
            max_tokens=5000,
            top_p=0.86,
            frequency_penalty=0,
            presence_penalty=0
        )
        
        # Extract content safely
        if "choices" in response and len(response["choices"]) > 0 and "message" in response["choices"][0] and "content" in response["choices"][0]["message"]:
            itinerary = response["choices"][0]["message"]["content"].strip()
        else:
            itinerary = "Sorry, I couldn't generate an itinerary at the moment."

    except Exception as e:
        return jsonify({"error": str(e)})

    return jsonify({"itinerary": itinerary})

if __name__ == '__main__':
    app.run(host='0.0.0.0')