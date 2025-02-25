from flask import Flask, request, jsonify

app = Flask(__name__)

questions = [
    "Do you like technology?",
    "Have you used AI tools before?",
    "Do you think AI can help in daily life?",
    "Would you trust AI for critical decisions?",
    "Would you recommend AI chatbots to others?"
]

user_responses = {}

@app.route("/", methods=["GET"])
def home():
    return "WhatsApp Bot is Running!"

@app.route("/webhook", methods=["POST"])
def whatsapp_webhook():
    data = request.get_json()
    
    sender = data["from"]  # Sender's WhatsApp number
    message = data["body"].strip().lower()  # User's response

    if sender not in user_responses:
        user_responses[sender] = {"index": 0, "answers": []}

    user_data = user_responses[sender]

    if user_data["index"] < len(questions):
        user_data["answers"].append((questions[user_data["index"]], message))
        user_data["index"] += 1

        if user_data["index"] < len(questions):
            return jsonify({"reply": questions[user_data["index"]]})
        else:
            return jsonify({"reply": "Thank you for doing this! 🎉"})

    return jsonify({"reply": "You've already completed the survey!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8504)
