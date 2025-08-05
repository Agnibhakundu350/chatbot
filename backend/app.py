from flask import Flask, request, jsonify  
from flask_cors import CORS  
import openai  
import os  

app = Flask(__name__)  
CORS(app)  # Allow cross-origin requests from React frontend  

# Load your OpenAI API key from environment variable  
openai.api_key = os.getenv("OPENAI_API_KEY")  

@app.route("/chat", methods=["POST"])  
def chat():  
    data = request.get_json()  
    message = data.get("message", "")  

    if not message:  
        return jsonify({"error": "No message provided"}), 400  

    try:  
        response = openai.ChatCompletion.create(  
            model="gpt-3.5-turbo",  
            messages=[  
                {"role": "system", "content": "You are a helpful AI assistant like Jarvis."},  
                {"role": "user", "content": message}  
            ]  
        )  
        reply = response["choices"][0]["message"]["content"].strip()  
        return jsonify({"reply": reply})  

    except Exception as e:  
        return jsonify({"error": str(e)}), 500  

if __name__ == "__main__":  
    app.run(debug=True)

