from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os

app = Flask(__name__)

# Load environment variables (optional)
from dotenv import load_dotenv
load_dotenv()

# Twilio credentials (replace with your own or use environment variables)
account_sid = os.getenv('TWILIO_ACCOUNT_SID', 'your_account_sid')
auth_token = os.getenv('TWILIO_AUTH_TOKEN', 'your_auth_token')
twilio_number = os.getenv('TWILIO_WHATSAPP_NUMBER', 'whatsapp:+14155238886')  # Twilio Sandbox number

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Route to handle incoming messages from WhatsApp
@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_message = request.values.get('Body', '').lower()
    response_message = process_message(incoming_message)
    response = MessagingResponse()
    response.message(response_message)
    return str(response)

def process_message(message):
    # Example logic to process incoming message and generate response
    if 'fees' in message:
        return "The course fees are $1000 per semester."
    elif 'facilities' in message:
        return "We offer state-of-the-art facilities including labs, libraries, and sports complexes."
    else:
        return "Sorry, I didn't understand that. Please ask about fees or facilities."

if __name__ == '__main__':
    app.run(debug=True)
