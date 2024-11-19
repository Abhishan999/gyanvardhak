from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", "")
    
    # Detect language and prepare response
    doc = nlp(user_input)
    lang = "hindi" if any(token.text in ["नमस्ते", "भारत", "संविधान"] for token in doc) else "english"
    
    if lang == "hindi":
        response = f"आपने पूछा: '{user_input}'. यह भारतीय संविधान के लिए मेरी प्रतिक्रिया है।"
    else:
        response = f"You asked: '{user_input}'. Here's my response for the Indian Constitution."
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
