from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample data for demonstration purposes
data = {
    "courses": {
        "course_1": {
            "name": "Computer Science",
            "fees": "$1000",
            "facilities": "Lab access, Online resources"
        },
        "course_2": {
            "name": "Mechanical Engineering",
            "fees": "$1500",
            "facilities": "Workshops, Lab access"
        },
        "course_3": {
            "name": "Business Administration",
            "fees": "$2000",
            "facilities": "Library access, Case studies"
        }
    },
    "hostel": {
        "single_room": {
            "fees": "$500 per month",
            "facilities": "Single bed, Study table, Wi-Fi"
        },
        "double_room": {
            "fees": "$300 per month",
            "facilities": "Two beds, Study tables, Wi-Fi"
        }
    },
    "infrastructure": "Our college has state-of-the-art labs, libraries, sports facilities, and more.",
    "location": "123 College St, College Town, CT 12345",
    "application_link": "https://college.edu/apply",
    "contact": {
        "admissions_office": "admissions@college.edu",
        "support": "support@college.edu",
        "phone": "123-456-7890"
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    query = request.form.get('query').lower()
    response = get_response(query)
    return jsonify(response)

def get_response(query):
    if "course fees" in query:
        return get_course_fees(query)
    elif "course facilities" in query:
        return get_course_facilities(query)
    elif "hostel fees" in query:
        return get_hostel_fees(query)
    elif "hostel facilities" in query:
        return get_hostel_facilities(query)
    elif "infrastructure" in query:
        return data['infrastructure']
    elif "location" in query:
        return data['location']
    elif "apply" in query or "admission" in query:
        return data['application_link']
    elif "contact" in query:
        return data['contact']
    else:
        return "Sorry, I don't understand that question."

def get_course_fees(query):
    for course_key, course_info in data['courses'].items():
        if course_info['name'].lower() in query:
            return {course_info['name']: course_info['fees']}
    return "Course not found."

def get_course_facilities(query):
    for course_key, course_info in data['courses'].items():
        if course_info['name'].lower() in query:
            return {course_info['name']: course_info['facilities']}
    return "Course not found."

def get_hostel_fees(query):
    return {room_type: info['fees'] for room_type, info in data['hostel'].items()}

def get_hostel_facilities(query):
    return {room_type: info['facilities'] for room_type, info in data['hostel'].items()}

if __name__ == '__main__':
    app.run(debug=True)
