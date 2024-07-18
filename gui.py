import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests

# Function to send query to the Flask backend
def send_query():
    query = user_input.get()
    response = requests.post("http://127.0.0.1:5000/chat", data={"query": query})
    response_data = response.json()
    chatbot_response = response_data.get("message", "No response from server.")
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"You: {query}\n")
    chat_log.insert(tk.END, f"Bot: {chatbot_response}\n\n")
    chat_log.config(state=tk.DISABLED)
    user_input.delete(0, tk.END)

# Function to send WhatsApp message using the Flask backend
def send_whatsapp():
    phone_number = phone_entry.get()
    message_body = message_entry.get()
    response = requests.post("http://127.0.0.1:5000/send_whatsapp", data={"phone_number": phone_number, "message": message_body})
    response_data = response.json()
    if response_data["status"] == "Message sent":
        messagebox.showinfo("Success", "Message sent successfully")
    else:
        messagebox.showerror("Error", f"Failed to send message: {response_data.get('error', 'Unknown error')}")

# Initialize the main window
root = tk.Tk()
root.title("University Chatbot")
root.geometry("600x700")

# Chat log
chat_log = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD)
chat_log.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# User input field
user_input_frame = tk.Frame(root)
user_input_frame.pack(pady=10)

user_input = tk.Entry(user_input_frame, width=70)
user_input.pack(side=tk.LEFT, padx=10)

send_button = tk.Button(user_input_frame, text="Send", command=send_query)
send_button.pack(side=tk.RIGHT)

# WhatsApp message section
whatsapp_frame = tk.Frame(root)
whatsapp_frame.pack(pady=20)

tk.Label(whatsapp_frame, text="Phone Number (with country code):").pack(anchor=tk.W)
phone_entry = tk.Entry(whatsapp_frame, width=50)
phone_entry.pack(anchor=tk.W)

tk.Label(whatsapp_frame, text="Message:").pack(anchor=tk.W)
message_entry = tk.Entry(whatsapp_frame, width=50)
message_entry.pack(anchor=tk.W)

send_whatsapp_button = tk.Button(whatsapp_frame, text="Send WhatsApp Message", command=send_whatsapp)
send_whatsapp_button.pack(pady=10)

root.mainloop()
